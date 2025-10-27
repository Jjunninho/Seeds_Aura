#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seeds Aura - Criador de Malhas Exóticas
--------------------------------------------------
GUI em PyQt5 com preview Matplotlib para gerar malhas "não comuns":
 - Voronoi Poisson-Disk
 - Colmeia Curvilínea ("rounded-hex")
 - Malha Topológica com arcos alternados
 - Quasicristal (soma de ondas + contornos)
 - Grade Senoidal Distorcida (warp)

Recursos:
 - Preview em tempo real
 - Semente aleatória controlável
 - Parâmetros específicos por padrão
 - Exportar PNG ou PDF (alta resolução)

Requisitos:
  Python 3.9+
  PyQt5
  numpy
  matplotlib
  scipy

Instalação (exemplo):
  pip install PyQt5 numpy matplotlib scipy

Execução:
  python seeds_aura_malhas_exoticas.py
"""
import sys
import os
import math
import json
import random
from dataclasses import dataclass
from typing import Dict, Any, Tuple

import numpy as np
import matplotlib
matplotlib.use("Agg")  # backend não-interativo para preparar a Figure antes de embed
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QSpinBox, QDoubleSpinBox, QCheckBox,
    QPushButton, QFileDialog, QGridLayout, QGroupBox, QFormLayout, QHBoxLayout, QVBoxLayout,
    QLineEdit
)

# Opcional SciPy (melhora Voronoi). Se não houver, desabilitamos esse padrão.
try:
    from scipy.spatial import Voronoi, voronoi_plot_2d
    SCIPY_OK = True
except Exception:
    SCIPY_OK = False


# ---------------------------- Utilidades ----------------------------

def set_ax_clean(ax):
    ax.set_aspect("equal")
    ax.axis("off")
    for spine in ax.spines.values():
        spine.set_visible(False)


def seed_everything(seed: int):
    random.seed(seed)
    np.random.seed(seed)


# ------------------------ Padrão: Voronoi Poisson ------------------------

def poisson_disk_sampling(width, height, r, k=30):
    """
    Amostragem Poisson-Disk simples (Bridson) em bbox [0,width]x[0,height].
    """
    cell_size = r / np.sqrt(2)
    grid_width = int(np.ceil(width / cell_size))
    grid_height = int(np.ceil(height / cell_size))
    grid = -np.ones((grid_width, grid_height), dtype=int)

    points = []
    active = []

    # primeiro ponto
    p0 = np.array([np.random.uniform(0, width), np.random.uniform(0, height)])
    points.append(p0)
    gx = int(p0[0] / cell_size)
    gy = int(p0[1] / cell_size)
    grid[gx, gy] = 0
    active.append(0)

    while active:
        idx = random.choice(active)
        point = points[idx]
        found = False
        for _ in range(k):
            ang = 2*np.pi*np.random.random()
            dist = np.random.uniform(r, 2*r)
            npnt = point + dist * np.array([np.cos(ang), np.sin(ang)])

            if not (0 <= npnt[0] < width and 0 <= npnt[1] < height):
                continue

            gx = int(npnt[0] / cell_size)
            gy = int(npnt[1] / cell_size)

            ok = True
            for ix in range(max(gx-2,0), min(gx+3, grid_width)):
                for iy in range(max(gy-2,0), min(gy+3, grid_height)):
                    j = grid[ix,iy]
                    if j >= 0:
                        if np.hypot(*(npnt - points[j])) < r:
                            ok = False
                            break
                if not ok:
                    break
            if ok:
                points.append(npnt)
                grid[gx,gy] = len(points)-1
                active.append(len(points)-1)
                found = True
                break
        if not found:
            active.remove(idx)

    return np.array(points)


def plot_voronoi_poisson(ax, W=10.0, H=10.0, r=0.45, lw=0.6):
    if not SCIPY_OK:
        ax.text(0.5, 0.5, "SciPy ausente\n(Voronoi indisponível)", ha="center", va="center")
        set_ax_clean(ax); return

    pts = poisson_disk_sampling(W, H, r=r)
    vor = Voronoi(pts)
    # desenha segmentos finitos apenas (evita os infinitos nas bordas)
    for (v0, v1) in vor.ridge_vertices:
        if v0 != -1 and v1 != -1:
            p0 = vor.vertices[v0]
            p1 = vor.vertices[v1]
            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], linewidth=lw)
    ax.set_xlim(0, W); ax.set_ylim(0, H)
    set_ax_clean(ax)


# ---------------------- Padrão: Colmeia Curvilínea ----------------------

def arc_between(p0, p1, bulge=0.25, outward_normal=None, npts=24):
    p0 = np.asarray(p0); p1 = np.asarray(p1)
    mid = 0.5*(p0+p1)
    v = p1-p0
    L = np.linalg.norm(v)
    if L < 1e-9:
        return np.vstack([p0, p1])

    n = np.array([-v[1], v[0]])
    n /= (np.linalg.norm(n) + 1e-12)
    if outward_normal is not None and np.dot(n, outward_normal) < 0:
        n = -n

    s = bulge * L
    r = (L**2)/(8*s) + s/2 if s>1e-9 else 1e9
    center = mid + n*(r - s)
    a0 = np.arctan2(p0[1]-center[1], p0[0]-center[0])
    a1 = np.arctan2(p1[1]-center[1], p1[0]-center[0])
    da = a1 - a0
    if da > np.pi: a1 -= 2*np.pi
    if da < -np.pi: a1 += 2*np.pi

    ang = np.linspace(a0, a1, npts)
    return np.c_[center[0]+np.cos(ang)*r, center[1]+np.sin(ang)*r]


def curved_hex_edges(center=(0,0), R=1.0, bulge=0.25, rotation=0.0, n_per_edge=24):
    angles = np.deg2rad(np.arange(0, 360, 60) + rotation)
    verts = np.stack([R*np.cos(angles), R*np.sin(angles)], axis=1) + np.asarray(center)
    c = np.asarray(center)
    segs = []
    for i in range(6):
        p0 = verts[i]; p1 = verts[(i+1)%6]
        v = p1 - p0
        ang = (np.degrees(np.arctan2(v[1], v[0])) % 180.0)
        is_verticalish = np.isclose(ang, 90.0, atol=2.5)
        if is_verticalish:
            seg = np.linspace(p0, p1, n_per_edge)
        else:
            outward = (p0+p1)/2 - c
            seg = arc_between(p0, p1, bulge=bulge, outward_normal=outward, npts=n_per_edge)
        segs.append(seg)
    return segs


def plot_curvy_honeycomb(ax, nx=16, ny=12, R=18.0, bulge=0.22, lw=0.7):
    H = np.sqrt(3)*R
    for row in range(ny):
        y = row*H
        x_offset = 0 if row%2==0 else 1.5*R
        for col in range(nx):
            cx = col*3*R + x_offset
            cy = y
            for seg in curved_hex_edges(center=(cx,cy), R=R, bulge=bulge, rotation=0.0, n_per_edge=28):
                ax.plot(seg[:,0], seg[:,1], linewidth=lw)
    ax.set_aspect("equal"); ax.axis("off")
    set_ax_clean(ax)


# ------------------- Padrão: Malha Topológica com Arcos -------------------

def arc_through(p0, p1, bow_to, sag_frac=0.35, n=40):
    p0 = np.asarray(p0); p1 = np.asarray(p1)
    v = p1 - p0
    L = np.linalg.norm(v)
    if L < 1e-9:
        return np.vstack([p0, p1])

    t = v / L
    nrm = np.array([-t[1], t[0]])
    mid = 0.5*(p0+p1)
    if np.dot(nrm, bow_to - mid) < 0:
        nrm = -nrm
    s = sag_frac * L
    r = (L**2)/(8*s) + s/2 if s > 1e-9 else 1e9
    center = mid + nrm*(r - s)

    a0 = np.arctan2(p0[1]-center[1], p0[0]-center[0])
    a1 = np.arctan2(p1[1]-center[1], p1[0]-center[0])
    da = a1 - a0
    if da > np.pi: a1 -= 2*np.pi
    elif da < -np.pi: a1 += 2*np.pi

    ang = np.linspace(a0, a1, n)
    return np.c_[center[0]+np.cos(ang)*r, center[1]+np.sin(ang)*r]


def generate_topology(nx=14, ny=20, sx=1.2, sy=1.0, sag_frac=0.35):
    verticals, arcs = [], []
    for k in range(nx):
        x = k*sx
        y_offset = (k % 2) * (sy/2)
        ys = [m*sy + y_offset for m in range(ny)]
        for m in range(ny-1):
            y0, y1 = ys[m], ys[m+1]
            verticals.append(np.array([[x,y0],[x,y1]]))
        for m,y in enumerate(ys):
            parity = (k+m) % 2
            if parity == 0 and k+1 < nx:
                x2 = (k+1)*sx
                y2 = m*sy + ((k+1)%2)*(sy/2)
                bow = np.array([(x+x2)/2, (y+y2)/2])
                arcs.append(arc_through([x,y],[x2,y2], bow, sag_frac, 60))
            elif parity == 1 and k-1 >= 0:
                x2 = (k-1)*sx
                y2 = m*sy + ((k-1)%2)*(sy/2)
                bow = np.array([(x+x2)/2, (y+y2)/2])
                arcs.append(arc_through([x,y],[x2,y2], bow, sag_frac, 60))
    return verticals, arcs


def plot_topology(ax, nx=16, ny=22, sx=1.2, sy=1.0, sag_frac=0.42, lw=0.6):
    verticals, arcs = generate_topology(nx, ny, sx, sy, sag_frac)
    for seg in verticals:
        ax.plot(seg[:,0], seg[:,1], linewidth=lw)
    for poly in arcs:
        ax.plot(poly[:,0], poly[:,1], linewidth=lw)
    set_ax_clean(ax)


# ------------------- Padrão: Quasicristal (ondas + contorno) -------------------

def quasicrystal_field(W=800, H=800, k=7, scale=0.012, phases=None):
    """
    Soma k ondas planas em ângulos uniformes. O resultado é quase-periódico.
    """
    y, x = np.mgrid[0:H, 0:W]
    xx = x - W/2.0
    yy = y - H/2.0
    r = np.hypot(xx, yy)
    th = np.arctan2(yy, xx)

    if phases is None:
        phases = np.random.uniform(0, 2*np.pi, size=k)

    field = np.zeros_like(xx, dtype=np.float64)
    for i in range(k):
        ang = 2*np.pi*i/k
        # vetor k orientado por ang
        kx = np.cos(ang); ky = np.sin(ang)
        field += np.cos(scale * (kx*xx + ky*yy) + phases[i])
    field /= k
    return field


def plot_quasicrystal(ax, W=900, H=900, k=9, scale=0.018, levels=14, lw=0.6):
    f = quasicrystal_field(W, H, k=k, scale=scale)
    # escolhe níveis de contorno próximos da média
    vmin, vmax = np.percentile(f, 10), np.percentile(f, 90)
    lv = np.linspace(vmin, vmax, levels)
    # desenha apenas contornos (linhas)
    CS = ax.contour(f, lv, linewidths=lw)
    ax.set_aspect("equal"); ax.axis("off")
    set_ax_clean(ax)


# ------------------ Padrão: Grade Senoidal Distorcida (warp) ------------------

def plot_warped_grid(ax, W=900, H=900, n=22, amp=24.0, freq=0.06, lw=0.6):
    """
    Grade base (linhas verticais/horizontais) com deslocamento senoidal 2D.
    """
    phases = np.random.uniform(0, 2*np.pi, size=4)
    # linhas verticais
    xs = np.linspace(0, W, n)
    ys = np.linspace(0, H, n)

    t = np.linspace(0, 1, 1000)
    for x in xs:
        X = np.full_like(t, x) + amp*np.sin(2*np.pi*freq*(t*H) + phases[0]) \
            + 0.6*amp*np.sin(2*np.pi*(freq*0.53)*(t*H) + phases[1])
        Y = t*H + amp*np.sin(2*np.pi*(freq*0.77)*(t*H) + phases[2])
        ax.plot(X, Y, linewidth=lw)

    for y in ys:
        Y = np.full_like(t, y) + amp*np.sin(2*np.pi*freq*(t*W) + phases[1]) \
            + 0.5*amp*np.sin(2*np.pi*(freq*1.17)*(t*W) + phases[0])
        X = t*W + amp*np.sin(2*np.pi*(freq*0.66)*(t*W) + phases[3])
        ax.plot(X, Y, linewidth=lw)

    ax.set_xlim(0, W); ax.set_ylim(0, H)
    set_ax_clean(ax)


# ------------------------------ GUI ------------------------------

PATTERNS = [
    "Voronoi Poisson-Disk",
    "Colmeia Curvilínea",
    "Malha Topológica (Arcos)",
    "Quasicristal (contornos)",
    "Grade Senoidal Distorcida"
]

@dataclass
class PatternParams:
    # parâmetros genéricos + específicos (guardados em dict)
    seed: int = 1234
    linewidth: float = 0.7
    extras: Dict[str, Any] = None


DEFAULTS: Dict[str, PatternParams] = {
    "Voronoi Poisson-Disk": PatternParams(
        seed=1234, linewidth=0.65,
        extras=dict(W=10.0, H=10.0, r=0.45)
    ),
    "Colmeia Curvilínea": PatternParams(
        seed=1234, linewidth=0.7,
        extras=dict(nx=16, ny=12, R=18.0, bulge=0.22)
    ),
    "Malha Topológica (Arcos)": PatternParams(
        seed=42, linewidth=0.65,
        extras=dict(nx=16, ny=22, sx=1.2, sy=1.0, sag_frac=0.42)
    ),
    "Quasicristal (contornos)": PatternParams(
        seed=2025, linewidth=0.6,
        extras=dict(W=900, H=900, k=9, scale=0.018, levels=14)
    ),
    "Grade Senoidal Distorcida": PatternParams(
        seed=2024, linewidth=0.65,
        extras=dict(W=900, H=900, n=22, amp=24.0, freq=0.06)
    ),
}


class SeedsAuraApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seeds Aura - Criador de Malhas Exóticas")
        self.fig = Figure(figsize=(6,6), dpi=120)
        self.canvas = FigureCanvas(self.fig)

        # Seletores
        self.combo = QComboBox()
        for p in PATTERNS:
            self.combo.addItem(p)
        self.combo.currentTextChanged.connect(self.reload_controls)

        self.seed_spin = QSpinBox(); self.seed_spin.setRange(0, 2_000_000_000)
        self.seed_spin.setValue(1234)
        self.seed_spin.valueChanged.connect(self.update_preview)

        self.lw_spin = QDoubleSpinBox(); self.lw_spin.setDecimals(2)
        self.lw_spin.setRange(0.05, 3.0); self.lw_spin.setSingleStep(0.05)
        self.lw_spin.setValue(0.7); self.lw_spin.valueChanged.connect(self.update_preview)

        # Caixa de parâmetros específicos
        self.params_box = QGroupBox("Parâmetros do Padrão")
        self.form = QFormLayout()
        self.params_box.setLayout(self.form)

        # Botões
        self.btn_random = QPushButton("Nova semente")
        self.btn_random.clicked.connect(self.randomize_seed)

        self.btn_refresh = QPushButton("Atualizar Preview")
        self.btn_refresh.clicked.connect(self.update_preview)

        self.btn_save_png = QPushButton("Salvar PNG")
        self.btn_save_png.clicked.connect(lambda: self.save_figure("png"))

        self.btn_save_pdf = QPushButton("Salvar PDF")
        self.btn_save_pdf.clicked.connect(lambda: self.save_figure("pdf"))

        # Layout esquerdo (controles)
        left = QVBoxLayout()
        left.addWidget(QLabel("Escolha o padrão:"))
        left.addWidget(self.combo)
        grid_basic = QGridLayout()
        grid_basic.addWidget(QLabel("Semente:"), 0, 0)
        grid_basic.addWidget(self.seed_spin, 0, 1)
        grid_basic.addWidget(QLabel("Espessura (lw):"), 1, 0)
        grid_basic.addWidget(self.lw_spin, 1, 1)
        left.addLayout(grid_basic)
        left.addWidget(self.params_box)
        btns = QHBoxLayout()
        btns.addWidget(self.btn_random); btns.addWidget(self.btn_refresh)
        left.addLayout(btns)
        left.addWidget(self.btn_save_png)
        left.addWidget(self.btn_save_pdf)
        left.addStretch()

        # Layout principal
        main = QHBoxLayout()
        main.addLayout(left, 0)
        main.addWidget(self.canvas, 1)
        self.setLayout(main)

        # inicializa
        self.dynamic_widgets: Dict[str, Any] = {}
        self.reload_controls()
        self.update_preview()

    # ----- Dinâmica de parâmetros específicos -----
    def clear_dynamic(self):
        while self.form.rowCount():
            self.form.removeRow(0)
        self.dynamic_widgets.clear()

    def add_spin(self, key, label, vmin, vmax, step, val, is_float=True):
        if is_float:
            w = QDoubleSpinBox(); w.setDecimals(4)
            w.setRange(vmin, vmax); w.setSingleStep(step); w.setValue(val)
            w.valueChanged.connect(self.update_preview)
        else:
            w = QSpinBox(); w.setRange(int(vmin), int(vmax)); w.setSingleStep(int(step)); w.setValue(int(val))
            w.valueChanged.connect(self.update_preview)
        self.form.addRow(QLabel(label), w)
        self.dynamic_widgets[key] = w

    def reload_controls(self):
        p = self.combo.currentText()
        defs = DEFAULTS[p]
        self.seed_spin.setValue(defs.seed)
        self.lw_spin.setValue(defs.linewidth)

        self.clear_dynamic()
        if p == "Voronoi Poisson-Disk":
            self.add_spin("W", "Largura (W)", 2.0, 40.0, 0.5, defs.extras["W"], True)
            self.add_spin("H", "Altura (H)", 2.0, 40.0, 0.5, defs.extras["H"], True)
            self.add_spin("r", "Raio mínimo (r)", 0.1, 2.0, 0.05, defs.extras["r"], True)
        elif p == "Colmeia Curvilínea":
            self.add_spin("nx", "Nx células", 4, 64, 1, defs.extras["nx"], False)
            self.add_spin("ny", "Ny células", 4, 64, 1, defs.extras["ny"], False)
            self.add_spin("R", "Raio R", 4.0, 64.0, 0.5, defs.extras["R"], True)
            self.add_spin("bulge", "Curvatura (bulge)", 0.0, 0.75, 0.02, defs.extras["bulge"], True)
        elif p == "Malha Topológica (Arcos)":
            self.add_spin("nx", "Nx", 4, 64, 1, defs.extras["nx"], False)
            self.add_spin("ny", "Ny", 4, 64, 1, defs.extras["ny"], False)
            self.add_spin("sx", "Passo X", 0.4, 3.0, 0.05, defs.extras["sx"], True)
            self.add_spin("sy", "Passo Y", 0.4, 3.0, 0.05, defs.extras["sy"], True)
            self.add_spin("sag_frac", "Flecha (sag_frac)", 0.05, 0.9, 0.01, defs.extras["sag_frac"], True)
        elif p == "Quasicristal (contornos)":
            self.add_spin("W", "Largura px", 400, 2200, 50, defs.extras["W"], False)
            self.add_spin("H", "Altura px", 400, 2200, 50, defs.extras["H"], False)
            self.add_spin("k", "Nº ondas (k)", 3, 19, 1, defs.extras["k"], False)
            self.add_spin("scale", "Escala k-esp.", 0.004, 0.08, 0.002, defs.extras["scale"], True)
            self.add_spin("levels", "Contornos", 4, 64, 1, defs.extras["levels"], False)
        elif p == "Grade Senoidal Distorcida":
            self.add_spin("W", "Largura px", 400, 2200, 50, defs.extras["W"], False)
            self.add_spin("H", "Altura px", 400, 2200, 50, defs.extras["H"], False)
            self.add_spin("n", "Linhas por eixo", 4, 120, 1, defs.extras["n"], False)
            self.add_spin("amp", "Amplitude", 0.0, 120.0, 1.0, defs.extras["amp"], True)
            self.add_spin("freq", "Frequência base", 0.005, 0.2, 0.001, defs.extras["freq"], True)

    # ----- Renderização -----
    def collect_params(self) -> Tuple[str, Dict[str, Any]]:
        p = self.combo.currentText()
        d = {k: (w.value()) for k,w in self.dynamic_widgets.items()}
        # coerção para int onde necessário
        if p in ("Colmeia Curvilínea", "Malha Topológica (Arcos)"):
            d["nx"] = int(d.get("nx", 16)); d["ny"] = int(d.get("ny", 12))
        if p in ("Quasicristal (contornos)", "Grade Senoidal Distorcida"):
            d["W"] = int(d.get("W", 900)); d["H"] = int(d.get("H", 900))
            if p == "Quasicristal (contornos)":
                d["k"] = int(d.get("k", 9)); d["levels"] = int(d.get("levels", 14))
            else:
                d["n"] = int(d.get("n", 22))
        return p, d

    def update_preview(self):
        seed_everything(int(self.seed_spin.value()))
        self.fig.clf()
        ax = self.fig.add_subplot(111)
        lw = float(self.lw_spin.value())
        pattern, d = self.collect_params()

        # CORREÇÃO: Passar apenas os parâmetros esperados por cada função
        if pattern == "Voronoi Poisson-Disk":
            plot_voronoi_poisson(ax, W=d.get('W', 10.0), H=d.get('H', 10.0), r=d.get('r', 0.45), lw=lw)
        elif pattern == "Colmeia Curvilínea":
            plot_curvy_honeycomb(ax, nx=d.get('nx', 16), ny=d.get('ny', 12), 
                                R=d.get('R', 18.0), bulge=d.get('bulge', 0.22), lw=lw)
        elif pattern == "Malha Topológica (Arcos)":
            plot_topology(ax, nx=d.get('nx', 16), ny=d.get('ny', 22), 
                         sx=d.get('sx', 1.2), sy=d.get('sy', 1.0), 
                         sag_frac=d.get('sag_frac', 0.42), lw=lw)
        elif pattern == "Quasicristal (contornos)":
            plot_quasicrystal(ax, W=d.get('W', 900), H=d.get('H', 900), 
                            k=d.get('k', 9), scale=d.get('scale', 0.018), 
                            levels=d.get('levels', 14), lw=lw)
        elif pattern == "Grade Senoidal Distorcida":
            plot_warped_grid(ax, W=d.get('W', 900), H=d.get('H', 900), 
                           n=d.get('n', 22), amp=d.get('amp', 24.0), 
                           freq=d.get('freq', 0.06), lw=lw)

        self.canvas.draw_idle()

    # ----- Utilidades de GUI -----
    def randomize_seed(self):
        self.seed_spin.setValue(random.randint(0, 2_000_000_000))

    def save_figure(self, fmt: str = "png"):
        # caixa de diálogo
        pattern, params = self.collect_params()
        fname_sug = f"seeds_aura_{pattern.replace(' ','_').replace('(','').replace(')','').lower()}.{fmt}"
        path, _ = QFileDialog.getSaveFileName(self, f"Salvar como {fmt.upper()}", fname_sug, f"*.{fmt}")
        if not path:
            return
        # renderizar em figura "limpa" para export com alta DPI
        seed_everything(int(self.seed_spin.value()))
        fig = Figure(figsize=(8,8), dpi=300)
        ax = fig.add_subplot(111)
        lw = float(self.lw_spin.value())
        
        # CORREÇÃO: Passar apenas os parâmetros esperados por cada função
        if pattern == "Voronoi Poisson-Disk":
            plot_voronoi_poisson(ax, W=params.get('W', 10.0), H=params.get('H', 10.0), 
                               r=params.get('r', 0.45), lw=lw)
        elif pattern == "Colmeia Curvilínea":
            plot_curvy_honeycomb(ax, nx=params.get('nx', 16), ny=params.get('ny', 12), 
                                R=params.get('R', 18.0), bulge=params.get('bulge', 0.22), lw=lw)
        elif pattern == "Malha Topológica (Arcos)":
            plot_topology(ax, nx=params.get('nx', 16), ny=params.get('ny', 22), 
                         sx=params.get('sx', 1.2), sy=params.get('sy', 1.0), 
                         sag_frac=params.get('sag_frac', 0.42), lw=lw)
        elif pattern == "Quasicristal (contornos)":
            plot_quasicrystal(ax, W=params.get('W', 900), H=params.get('H', 900), 
                            k=params.get('k', 9), scale=params.get('scale', 0.018), 
                            levels=params.get('levels', 14), lw=lw)
        elif pattern == "Grade Senoidal Distorcida":
            plot_warped_grid(ax, W=params.get('W', 900), H=params.get('H', 900), 
                           n=params.get('n', 22), amp=params.get('amp', 24.0), 
                           freq=params.get('freq', 0.06), lw=lw)

        fig.tight_layout(pad=0)
        # salva
        if fmt.lower() == "png":
            fig.savefig(path, dpi=300, bbox_inches="tight", pad_inches=0)
        elif fmt.lower() == "pdf":
            fig.savefig(path, bbox_inches="tight", pad_inches=0)

        # Atualiza preview para manter consistência visual
        self.update_preview()


def main():
    # Para embed correto do Matplotlib em PyQt5
    import matplotlib
    matplotlib.use("Qt5Agg")
    app = QApplication(sys.argv)
    w = SeedsAuraApp()
    w.resize(1150, 720)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
