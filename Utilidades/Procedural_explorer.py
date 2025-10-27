#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Seeds Aura - Procedural Explorer - Versão Melhorada
--------------------------------------
GUI em PyQt5 com preview Matplotlib para explorar algoritmos
de geração procedural com controles específicos e descrições educativas.
"""

import sys
import math
import random
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox, QCheckBox,
    QGroupBox, QFormLayout, QSlider, QFileDialog, QTextEdit
)

# ------------------------
# Utilidades matemáticas
# ------------------------

def clamp01(x):
    return max(0.0, min(1.0, x))

def lerp(a, b, t):
    return a + t * (b - a)

def smoothstep(t):
    return t*t*(3.0 - 2.0*t)

# ------------------------
# PERLIN NOISE (2D / 3D)
# ------------------------

class Perlin2D:
    def __init__(self, w, h, seed=0):
        self.w = w
        self.h = h
        rng = np.random.RandomState(seed)
        self.grad = rng.rand(w+1, h+1, 2)*2 - 1
        norms = np.linalg.norm(self.grad, axis=2, keepdims=True)
        norms[norms == 0] = 1.0
        self.grad /= norms

    def dot_grid(self, ix, iy, x, y):
        ix = int(min(ix, self.w))
        iy = int(min(iy, self.h))
        dx, dy = x - ix, y - iy
        g = self.grad[ix, iy]
        return dx*g[0] + dy*g[1]

    def sample(self, x, y):
        x0 = int(math.floor(x))
        y0 = int(math.floor(y))
        x1 = x0 + 1
        y1 = y0 + 1
        sx = smoothstep(x - x0)
        sy = smoothstep(y - y0)
        n00 = self.dot_grid(x0, y0, x, y)
        n10 = self.dot_grid(x1, y0, x, y)
        n01 = self.dot_grid(x0, y1, x, y)
        n11 = self.dot_grid(x1, y1, x, y)
        ix0 = lerp(n00, n10, sx)
        ix1 = lerp(n01, n11, sx)
        return lerp(ix0, ix1, sy)

def perlin_noise_2d_map(width=256, height=256, scale=60.0, octaves=4, persistence=0.5, lacunarity=2.0, seed=0):
    perlin = Perlin2D(int(width/scale)+2, int(height/scale)+2, seed=seed)
    noise = np.zeros((height, width), dtype=np.float32)
    amplitude = 1.0
    frequency = 1.0
    max_amp = 0.0
    for _ in range(octaves):
        for y in range(height):
            for x in range(width):
                sx = x / scale * frequency
                sy = y / scale * frequency
                noise[y, x] += perlin.sample(sx, sy) * amplitude
        max_amp += amplitude
        amplitude *= persistence
        frequency *= lacunarity
    if max_amp > 0:
        noise = (noise + max_amp) / (2.0 * max_amp)
    return np.clip(noise, 0, 1)

def domain_warping_map(width=256, height=256, base_scale=60.0, warp_scale=30.0, warp_strength=1.5, seed=0):
    warp_u = perlin_noise_2d_map(width, height, scale=warp_scale, octaves=3, seed=seed)
    warp_v = perlin_noise_2d_map(width, height, scale=warp_scale*1.1, octaves=3, seed=seed+1337)
    du = (warp_u * 2.0 - 1.0) * warp_strength
    dv = (warp_v * 2.0 - 1.0) * warp_strength
    base = Perlin2D(int(width/base_scale)+2, int(height/base_scale)+2, seed=seed+7)
    out = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            sx = (x + du[y, x]) / base_scale
            sy = (y + dv[y, x]) / base_scale
            out[y, x] = base.sample(sx, sy)
    out = (out - out.min()) / (out.max() - out.min() + 1e-8)
    return out

# ------------------------
# WORLEY (CELL) NOISE
# ------------------------

def worley_noise_2d(width=256, height=256, num_points=50, seed=0, mode=1):
    rng = np.random.RandomState(seed)
    pts = rng.rand(num_points, 2)
    pts[:, 0] *= width
    pts[:, 1] *= height
    img = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            d = np.sqrt((pts[:,0] - x)**2 + (pts[:,1] - y)**2)
            d.sort()
            val = d[0] if mode == 1 else d[min(1, len(d)-1)]
            img[y, x] = val
    img = (img - img.min()) / (img.max() - img.min() + 1e-8)
    return img

# ------------------------
# VORONOI
# ------------------------

def voronoi_distance_map(width=256, height=256, num_points=30, seed=0):
    rng = np.random.RandomState(seed)
    pts = rng.rand(num_points, 2)
    pts[:, 0] *= width
    pts[:, 1] *= height
    img = np.zeros((height, width), dtype=np.float32)
    for y in range(height):
        for x in range(width):
            d = np.sqrt((pts[:,0] - x)**2 + (pts[:,1] - y)**2)
            img[y, x] = np.min(d)
    img = (img - img.min()) / (img.max() - img.min() + 1e-8)
    return img

# ------------------------
# MAZE
# ------------------------

def maze_recursive_backtracker(w=30, h=20, seed=0):
    rng = np.random.RandomState(seed)
    W, H = w*2+1, h*2+1
    grid = np.ones((H, W), dtype=np.uint8)
    visited = np.zeros((h, w), dtype=bool)
    stack = []
    cr, cc = rng.randint(0, h), rng.randint(0, w)
    stack.append((cr, cc))
    visited[cr, cc] = True
    grid[cr*2+1, cc*2+1] = 0

    def get_neighbors(r, c):
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        rng.shuffle(dirs)
        result = []
        for dr, dc in dirs:
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and not visited[nr, nc]:
                result.append((nr, nc, dr, dc))
        return result

    while stack:
        r, c = stack[-1]
        neighbors = get_neighbors(r, c)
        if neighbors:
            nr, nc, dr, dc = neighbors[0]
            visited[nr, nc] = True
            grid[r*2+1+dr, c*2+1+dc] = 0
            grid[nr*2+1, nc*2+1] = 0
            stack.append((nr, nc))
        else:
            stack.pop()
    return grid

# ------------------------
# DLA
# ------------------------

def dla(grid_size=256, num_particles=1500, seed=0):
    rng = np.random.RandomState(seed)
    grid = np.zeros((grid_size, grid_size), dtype=np.uint8)
    cx, cy = grid_size//2, grid_size//2
    grid[cy, cx] = 1
    spawn_radius = max(2, grid_size//2 - 3)

    for _ in range(num_particles):
        ang = rng.rand() * 2*math.pi
        x = int(cx + spawn_radius * math.cos(ang))
        y = int(cy + spawn_radius * math.sin(ang))
        x = np.clip(x, 1, grid_size-2)
        y = np.clip(y, 1, grid_size-2)
        
        max_steps = grid_size * 4
        steps = 0
        while steps < max_steps:
            steps += 1
            dx = rng.randint(-1, 2)
            dy = rng.randint(-1, 2)
            nx, ny = x+dx, y+dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if (grid[max(0,ny-1):min(grid_size,ny+2), max(0,nx-1):min(grid_size,nx+2)]).any():
                    grid[y, x] = 1
                    break
                x, y = nx, ny
    return grid

# ------------------------
# K-MEANS
# ------------------------

def k_means_demo(n_points=200, k=5, seed=0):
    rng = np.random.RandomState(seed)
    pts = rng.randn(n_points, 2) * 2 + rng.randn(k, 2)[rng.randint(0, k, n_points)]
    centroids = pts[rng.choice(n_points, k, replace=False)]
    for _ in range(20):
        d = np.linalg.norm(pts[:, None] - centroids, axis=2)
        labels = np.argmin(d, axis=1)
        for i in range(k):
            if (labels == i).any():
                centroids[i] = pts[labels == i].mean(axis=0)
    return pts, labels, centroids

# ------------------------
# QUADTREE
# ------------------------

class Rect:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    def contains(self, pt):
        return (self.x <= pt[0] < self.x+self.w and self.y <= pt[1] < self.y+self.h)

class Quadtree:
    def __init__(self, boundary, cap=4, max_depth=8, depth=0):
        self.boundary = boundary
        self.cap = cap
        self.max_depth = max_depth
        self.depth = depth
        self.points = []
        self.divided = False
        self.children = [None, None, None, None]
    
    def subdivide(self):
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.w, self.boundary.h
        hw, hh = w/2, h/2
        self.children[0] = Quadtree(Rect(x, y, hw, hh), self.cap, self.max_depth, self.depth+1)
        self.children[1] = Quadtree(Rect(x+hw, y, hw, hh), self.cap, self.max_depth, self.depth+1)
        self.children[2] = Quadtree(Rect(x, y+hh, hw, hh), self.cap, self.max_depth, self.depth+1)
        self.children[3] = Quadtree(Rect(x+hw, y+hh, hw, hh), self.cap, self.max_depth, self.depth+1)
        self.divided = True
    
    def insert(self, pt):
        if not self.boundary.contains(pt):
            return False
        if len(self.points) < self.cap or self.depth >= self.max_depth:
            self.points.append(pt)
            return True
        if not self.divided:
            self.subdivide()
            for p in self.points:
                for child in self.children:
                    if child.insert(p):
                        break
            self.points = []
        for child in self.children:
            if child.insert(pt):
                return True
        return False
    
    def collect_rects(self, out):
        out.append(self.boundary)
        if self.divided:
            for child in self.children:
                child.collect_rects(out)

# ------------------------
# CIRCLE PACKING
# ------------------------

def circle_packing(container_r=100, n=100, rmin=2, rmax=20, seed=0):
    rng = np.random.RandomState(seed)
    circles = []
    max_attempts = n * 100
    attempts = 0
    while len(circles) < n and attempts < max_attempts:
        attempts += 1
        r = rng.uniform(rmin, rmax)
        ang = rng.rand() * 2*math.pi
        max_d = container_r - r
        d = rng.rand() * max_d
        x = d * math.cos(ang)
        y = d * math.sin(ang)
        dist_origin = math.sqrt(x*x + y*y)
        if dist_origin + r > container_r:
            continue
        valid = True
        for (cx, cy, cr) in circles:
            dd = math.sqrt((x-cx)**2 + (y-cy)**2)
            if dd < r + cr:
                valid = False
                break
        if valid:
            circles.append((x, y, r))
    return circles

# ------------------------
# TERRENO 3D
# ------------------------

def diamond_square(n=129, roughness=0.6, seed=0):
    rng = np.random.RandomState(seed)
    hm = np.zeros((n, n), dtype=np.float32)
    hm[0, 0] = rng.rand()
    hm[0, n-1] = rng.rand()
    hm[n-1, 0] = rng.rand()
    hm[n-1, n-1] = rng.rand()
    step = n - 1
    scale = 1.0
    while step > 1:
        hs = step // 2
        for y in range(0, n-1, step):
            for x in range(0, n-1, step):
                avg = (hm[y, x] + hm[y, x+step] + hm[y+step, x] + hm[y+step, x+step]) / 4.0
                hm[y+hs, x+hs] = avg + (rng.rand()*2-1) * scale
        for y in range(0, n, hs):
            for x in range((y+hs)%step, n, step):
                s = []
                if y >= hs: s.append(hm[y-hs, x])
                if y+hs < n: s.append(hm[y+hs, x])
                if x >= hs: s.append(hm[y, x-hs])
                if x+hs < n: s.append(hm[y, x+hs])
                if s:
                    hm[y, x] = sum(s)/len(s) + (rng.rand()*2-1) * scale
        step = hs
        scale *= roughness
    return hm

def fault_formation(size=100, iterations=1000, min_h=-0.01, max_h=0.01, seed=0):
    rng = np.random.RandomState(seed)
    hm = np.zeros((size, size), dtype=np.float32)
    for _ in range(iterations):
        x1, y1 = rng.rand(2) * size
        ang = rng.rand() * 2*math.pi
        dx = math.cos(ang)
        dy = math.sin(ang)
        dh = rng.uniform(min_h, max_h)
        for y in range(size):
            for x in range(size):
                cross = (x - x1)*dy - (y - y1)*dx
                if cross > 0:
                    hm[y, x] += dh
    return hm

# ------------------------
# VOXEL
# ------------------------

def voxel_grid_sphere(n=20, r=8):
    grid = np.zeros((n, n, n), dtype=bool)
    c = n // 2
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if (x-c)**2 + (y-c)**2 + (z-c)**2 <= r**2:
                    grid[x, y, z] = True
    return grid

# ------------------------
# SUPERFICIE 3D
# ------------------------

def sphere_parametric(n=80, radius=1.0):
    u = np.linspace(0, 2*np.pi, n)
    v = np.linspace(0, np.pi, n)
    X = radius * np.outer(np.cos(u), np.sin(v))
    Y = radius * np.outer(np.sin(u), np.sin(v))
    Z = radius * np.outer(np.ones_like(u), np.cos(v))
    return X, Y, Z

# ------------------------
# DESCRIÇÕES DOS ALGORITMOS
# ------------------------

ALGORITHM_DESCRIPTIONS = {
    "2D - Perlin Noise": """PERLIN NOISE - Ruído coerente e orgânico

Criado por Ken Perlin em 1983, gera padrões suaves e naturais.
Usado em texturas de nuvens, terrenos e efeitos procedurais.

Parâmetros:
• Escala: Tamanho das características (10-200)
• Oitavas: Níveis de detalhe (1-8)
• Seed: Semente para variação""",

    "2D - Worley F1": """WORLEY NOISE (F1) - Distância ao ponto mais próximo

Também chamado de Cellular Noise, cria padrões celulares.
F1 mede a distância ao primeiro ponto mais próximo.
Útil para texturas de pedra, células e padrões orgânicos.

Parâmetros:
• Pontos: Número de células (10-200)
• Seed: Semente para distribuição""",

    "2D - Worley F2": """WORLEY NOISE (F2) - Distância ao segundo ponto

Similar ao F1, mas usa o segundo ponto mais próximo.
Cria padrões mais complexos e interessantes.
Bom para texturas de mármore e padrões venosos.

Parâmetros:
• Pontos: Número de células (10-200)
• Seed: Semente para distribuição""",

    "2D - Voronoi": """VORONOI DIAGRAM - Partição espacial

Divide o espaço em regiões baseadas em pontos.
Cada região contém todos os pontos mais próximos de um centro.
Usado em mapeamento, análise espacial e arte generativa.

Parâmetros:
• Pontos: Número de centros (10-150)
• Seed: Semente para posições""",

    "2D - Maze (Recursive Backtracker)": """LABIRINTO - Geração por retrocesso recursivo

Algoritmo que cria labirintos perfeitos (solução única).
Usa pilha para backtracking quando encontra becos sem saída.
Gera padrões orgânicos com muitos corredores longos.

Parâmetros:
• Células X/Y: Tamanho do labirinto (5-50)
• Seed: Semente para variação""",

    "2D - DLA": """DLA - Diffusion-Limited Aggregation

Simula crescimento de estruturas fractais.
Partículas se movem aleatoriamente até aderir à estrutura.
Modela cristais, corais, relâmpagos e crescimento natural.

Parâmetros:
• Tamanho: Resolução da grade (64-512)
• Partículas: Quantidade simulada (100-5000)
• Seed: Semente para movimento""",

    "2D - K-Means": """K-MEANS - Clustering e agrupamento

Algoritmo de aprendizado não-supervisionado.
Agrupa pontos em K clusters por proximidade.
Usado em análise de dados, compressão e segmentação.

Parâmetros:
• Pontos: Quantidade de dados (100-1000)
• K: Número de clusters (2-15)
• Seed: Semente para distribuição""",

    "2D - Quadtree": """QUADTREE - Particionamento espacial hierárquico

Estrutura de dados que divide recursivamente o espaço.
Cada nó tem 4 filhos representando quadrantes.
Otimiza buscas espaciais e detecção de colisão.

Parâmetros:
• Pontos: Objetos a indexar (50-1000)
• Capacidade: Pontos por nó (1-20)
• Prof. Máx: Níveis de subdivisão (3-12)
• Seed: Semente para distribuição""",

    "2D - Circle Packing": """CIRCLE PACKING - Empacotamento de círculos

Algoritmo que posiciona círculos sem sobreposição.
Gera padrões orgânicos e visualmente interessantes.
Usado em design, visualização de dados e arte.

Parâmetros:
• Círculos: Quantidade a empacotar (20-300)
• Raio Min/Máx: Tamanho dos círculos (2-50)
• Seed: Semente para posições""",

    "2D - Domain Warping": """DOMAIN WARPING - Distorção de domínio

Técnica que distorce coordenadas antes de amostrar ruído.
Cria padrões muito mais complexos e orgânicos.
Usado para texturas avançadas, nuvens e terrenos.

Parâmetros:
• Escala Base: Frequência do ruído (20-150)
• Força Warp: Intensidade da distorção (0.5-5.0)
• Seed: Semente para variação""",

    "3D - Esfera Parametrica": """ESFERA PARAMÉTRICA - Superfície 3D matemática

Gerada por equações paramétricas usando seno e cosseno.
Demonstra como criar formas 3D perfeitamente regulares.
Base para modelagem procedural de objetos.

Parâmetros:
• Resolução: Densidade da malha (20-150)""",

    "3D - Terreno (Diamond-Square)": """TERRENO DIAMOND-SQUARE - Heightmap fractal

Algoritmo clássico para gerar terrenos realistas.
Divide recursivamente e perturba o heightmap.
Usado em jogos desde os anos 80, rápido e eficiente.

Parâmetros:
• Rugosidade: Variação da altura (0.1-1.5)
• Seed: Semente para variação""",

    "3D - Terreno (Fault Formation)": """TERRENO FAULT FORMATION - Simulação geológica

Simula formação de terreno por falhas tectônicas.
Cada iteração adiciona uma linha de falha aleatória.
Cria montanhas e vales de aparência natural.

Parâmetros:
• Tamanho: Resolução da grade (40-200)
• Iterações: Número de falhas (100-5000)
• Seed: Semente para falhas""",

    "3D - Voxel (Esfera)": """VOXEL GRID - Representação volumétrica 3D

Estrutura 3D de cubos (pixels volumétricos).
Usada em Minecraft, simulações e modelagem.
Permite manipulação simples de geometria complexa.

Parâmetros:
• Grid N: Tamanho da grade (10-40)
• Raio: Tamanho da esfera (3-20)""",

    "3D - Superficie Perlin (Heightmap)": """HEIGHTMAP PERLIN - Terreno com ruído coerente

Usa Perlin Noise para gerar elevações suaves.
Cria terrenos mais orgânicos que Diamond-Square.
Controle fino através de oitavas e escala.

Parâmetros:
• Resolução: Tamanho da malha (40-220)
• Escala: Frequência do ruído (10-150)
• Oitavas: Níveis de detalhe (1-8)
• Seed: Semente para variação"""
}

# ------------------------
# LISTA DE ALGORITMOS
# ------------------------

ALGOS = [
    "2D - Perlin Noise",
    "2D - Worley F1",
    "2D - Worley F2",
    "2D - Voronoi",
    "2D - Maze (Recursive Backtracker)",
    "2D - DLA",
    "2D - K-Means",
    "2D - Quadtree",
    "2D - Circle Packing",
    "2D - Domain Warping",
    "3D - Esfera Parametrica",
    "3D - Terreno (Diamond-Square)",
    "3D - Terreno (Fault Formation)",
    "3D - Voxel (Esfera)",
    "3D - Superficie Perlin (Heightmap)"
]

# ------------------------
# PAINEL DE CONTROLE DINÂMICO
# ------------------------

class DynamicControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.controls = {}
        
    def clear_controls(self):
        """Remove todos os controles"""
        for control in self.controls.values():
            if isinstance(control, QWidget):
                control.deleteLater()
        self.controls.clear()
        # Limpa o layout
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
    
    def add_spinbox(self, name, label, min_val, max_val, default, step=1):
        """Adiciona um SpinBox"""
        spinbox = QSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setValue(default)
        spinbox.setSingleStep(step)
        self.layout.addRow(label, spinbox)
        self.controls[name] = spinbox
        return spinbox
    
    def add_doublespinbox(self, name, label, min_val, max_val, default, step=0.1, decimals=2):
        """Adiciona um DoubleSpinBox"""
        spinbox = QDoubleSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setValue(default)
        spinbox.setSingleStep(step)
        spinbox.setDecimals(decimals)
        self.layout.addRow(label, spinbox)
        self.controls[name] = spinbox
        return spinbox
    
    def get_value(self, name):
        """Retorna o valor de um controle"""
        if name in self.controls:
            return self.controls[name].value()
        return None

# ------------------------
# JANELA PRINCIPAL
# ------------------------

class ProceduralExplorer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seeds Aura - Procedural Explorer - Versão Melhorada")
        self.setGeometry(100, 100, 1400, 900)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout(central)
        
        # Painel esquerdo
        left = QVBoxLayout()
        
        # Seletor de algoritmo
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(ALGOS)
        self.algo_combo.currentTextChanged.connect(self.on_algorithm_changed)
        
        # Descrição do algoritmo
        self.description_box = QTextEdit()
        self.description_box.setReadOnly(True)
        self.description_box.setMaximumHeight(200)
        self.description_box.setStyleSheet("""
            QTextEdit {
                background-color: #f0f0f0;
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 10px;
                font-family: Arial;
                font-size: 11px;
            }
        """)
        
        # Painel de controles dinâmico
        self.control_panel = DynamicControlPanel()
        control_scroll = QWidget()
        control_scroll_layout = QVBoxLayout(control_scroll)
        control_scroll_layout.addWidget(self.control_panel)
        control_scroll_layout.addStretch()
        
        # Botões
        self.btn_run = QPushButton("▶ Executar")
        self.btn_run.setStyleSheet("QPushButton { font-size: 14px; padding: 8px; background-color: #4CAF50; color: white; }")
        self.btn_save = QPushButton("💾 Salvar imagem...")
        
        left.addWidget(QLabel("<b>Selecione o Algoritmo:</b>"))
        left.addWidget(self.algo_combo)
        left.addWidget(QLabel("<b>Descrição:</b>"))
        left.addWidget(self.description_box)
        left.addWidget(QLabel("<b>Parâmetros:</b>"))
        left.addWidget(control_scroll)
        left.addWidget(self.btn_run)
        left.addWidget(self.btn_save)
        
        # Canvas matplotlib
        self.fig = plt.figure(figsize=(8, 7))
        self.canvas = FigureCanvas(self.fig)
        
        layout.addLayout(left, 2)
        layout.addWidget(self.canvas, 5)
        
        # Conectar eventos
        self.btn_run.clicked.connect(self.run_current)
        self.btn_save.clicked.connect(self.save_image)
        
        # Inicializar com primeiro algoritmo
        self.on_algorithm_changed(ALGOS[0])
    
    def on_algorithm_changed(self, algo_name):
        """Atualiza descrição e controles quando algoritmo muda"""
        # Atualizar descrição
        description = ALGORITHM_DESCRIPTIONS.get(algo_name, "Sem descrição disponível.")
        self.description_box.setPlainText(description)
        
        # Limpar controles anteriores
        self.control_panel.clear_controls()
        
        # Adicionar controles específicos para cada algoritmo
        if algo_name == "2D - Perlin Noise":
            self.control_panel.add_spinbox('width', 'Largura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('height', 'Altura:', 64, 1024, 512, step=64)
            self.control_panel.add_doublespinbox('scale', 'Escala:', 10.0, 200.0, 60.0, step=10.0)
            self.control_panel.add_spinbox('octaves', 'Oitavas:', 1, 8, 4)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name in ["2D - Worley F1", "2D - Worley F2"]:
            self.control_panel.add_spinbox('width', 'Largura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('height', 'Altura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('points', 'Pontos:', 10, 200, 50, step=10)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - Voronoi":
            self.control_panel.add_spinbox('width', 'Largura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('height', 'Altura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('points', 'Pontos:', 10, 150, 30, step=10)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - Maze (Recursive Backtracker)":
            self.control_panel.add_spinbox('maze_w', 'Células X:', 5, 50, 20, step=5)
            self.control_panel.add_spinbox('maze_h', 'Células Y:', 5, 50, 15, step=5)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - DLA":
            self.control_panel.add_spinbox('grid_size', 'Tamanho:', 64, 512, 256, step=64)
            self.control_panel.add_spinbox('particles', 'Partículas:', 100, 5000, 1500, step=100)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - K-Means":
            self.control_panel.add_spinbox('points', 'Pontos:', 100, 1000, 300, step=50)
            self.control_panel.add_spinbox('k', 'K (clusters):', 2, 15, 5)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - Quadtree":
            self.control_panel.add_spinbox('width', 'Largura:', 100, 1000, 400, step=50)
            self.control_panel.add_spinbox('height', 'Altura:', 100, 1000, 400, step=50)
            self.control_panel.add_spinbox('points', 'Pontos:', 50, 1000, 200, step=50)
            self.control_panel.add_spinbox('capacity', 'Capacidade:', 1, 20, 4)
            self.control_panel.add_spinbox('max_depth', 'Prof. Máx:', 3, 12, 8)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - Circle Packing":
            self.control_panel.add_spinbox('container_r', 'Raio Container:', 50, 300, 150, step=25)
            self.control_panel.add_spinbox('circles', 'Círculos:', 20, 300, 80, step=10)
            self.control_panel.add_spinbox('rmin', 'Raio Min:', 2, 20, 3)
            self.control_panel.add_spinbox('rmax', 'Raio Máx:', 5, 50, 15, step=5)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "2D - Domain Warping":
            self.control_panel.add_spinbox('width', 'Largura:', 64, 1024, 512, step=64)
            self.control_panel.add_spinbox('height', 'Altura:', 64, 1024, 512, step=64)
            self.control_panel.add_doublespinbox('base_scale', 'Escala Base:', 20.0, 150.0, 60.0, step=10.0)
            self.control_panel.add_doublespinbox('warp_strength', 'Força Warp:', 0.5, 5.0, 1.5, step=0.5)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "3D - Esfera Parametrica":
            self.control_panel.add_spinbox('resolution', 'Resolução:', 20, 150, 60, step=10)
        
        elif algo_name == "3D - Terreno (Diamond-Square)":
            self.control_panel.add_doublespinbox('roughness', 'Rugosidade:', 0.1, 1.5, 0.6, step=0.1)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "3D - Terreno (Fault Formation)":
            self.control_panel.add_spinbox('size', 'Tamanho:', 40, 200, 100, step=20)
            self.control_panel.add_spinbox('iterations', 'Iterações:', 100, 5000, 1000, step=100)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
        
        elif algo_name == "3D - Voxel (Esfera)":
            self.control_panel.add_spinbox('grid_n', 'Grid N:', 10, 40, 20, step=5)
            self.control_panel.add_spinbox('radius', 'Raio:', 3, 20, 8, step=2)
        
        elif algo_name == "3D - Superficie Perlin (Heightmap)":
            self.control_panel.add_spinbox('resolution', 'Resolução:', 40, 220, 100, step=20)
            self.control_panel.add_doublespinbox('scale', 'Escala:', 10.0, 150.0, 40.0, step=10.0)
            self.control_panel.add_spinbox('octaves', 'Oitavas:', 1, 8, 4)
            self.control_panel.add_spinbox('seed', 'Seed:', 0, 99999, 0, step=100)
    
    def run_current(self):
        """Executa o algoritmo atual"""
        try:
            algo = self.algo_combo.currentText()
            p = self.control_panel
            self.fig.clf()
            
            if algo == "2D - Perlin Noise":
                img = perlin_noise_2d_map(
                    width=p.get_value('width'),
                    height=p.get_value('height'),
                    scale=p.get_value('scale'),
                    octaves=p.get_value('octaves'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='viridis')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - Worley F1":
                img = worley_noise_2d(
                    width=p.get_value('width'),
                    height=p.get_value('height'),
                    num_points=p.get_value('points'),
                    seed=p.get_value('seed'),
                    mode=1
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='viridis')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - Worley F2":
                img = worley_noise_2d(
                    width=p.get_value('width'),
                    height=p.get_value('height'),
                    num_points=p.get_value('points'),
                    seed=p.get_value('seed'),
                    mode=2
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='viridis')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - Voronoi":
                img = voronoi_distance_map(
                    width=p.get_value('width'),
                    height=p.get_value('height'),
                    num_points=p.get_value('points'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='viridis')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - Maze (Recursive Backtracker)":
                grid = maze_recursive_backtracker(
                    w=p.get_value('maze_w'),
                    h=p.get_value('maze_h'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(grid, cmap='binary', origin='upper')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - DLA":
                img = dla(
                    grid_size=p.get_value('grid_size'),
                    num_particles=p.get_value('particles'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='hot')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - K-Means":
                pts, labels, cent = k_means_demo(
                    n_points=p.get_value('points'),
                    k=p.get_value('k'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.scatter(pts[:,0], pts[:,1], c=labels, s=8, cmap='tab10', alpha=0.6)
                ax.scatter(cent[:,0], cent[:,1], s=200, marker='X', c='red', 
                          linewidths=2, edgecolors='black', zorder=10)
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.set_aspect('equal', 'box')
            
            elif algo == "2D - Quadtree":
                W = p.get_value('width')
                H = p.get_value('height')
                rect = Rect(0, 0, W, H)
                qt = Quadtree(rect, cap=p.get_value('capacity'), 
                             max_depth=p.get_value('max_depth'))
                rng = np.random.RandomState(p.get_value('seed'))
                pts = (rng.rand(p.get_value('points'), 2) * np.array([W, H])).tolist()
                for pt in pts:
                    qt.insert(pt)
                rects = []
                qt.collect_rects(rects)
                ax = self.fig.add_subplot(111)
                for r in rects:
                    xs = [r.x, r.x+r.w, r.x+r.w, r.x, r.x]
                    ys = [r.y, r.y, r.y+r.h, r.y+r.h, r.y]
                    ax.plot(xs, ys, 'b-', linewidth=0.8)
                px = [pt[0] for pt in pts]
                py = [pt[1] for pt in pts]
                ax.scatter(px, py, s=6, c='red', zorder=5)
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.set_xlim(0, W)
                ax.set_ylim(0, H)
                ax.set_aspect('equal', 'box')
                ax.invert_yaxis()
            
            elif algo == "2D - Circle Packing":
                circles = circle_packing(
                    container_r=p.get_value('container_r'),
                    n=p.get_value('circles'),
                    rmin=p.get_value('rmin'),
                    rmax=p.get_value('rmax'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.set_aspect('equal', 'box')
                R = p.get_value('container_r')
                ax.set_xlim(-R-10, R+10)
                ax.set_ylim(-R-10, R+10)
                # Container circle
                container = plt.Circle((0, 0), R, fill=False, edgecolor='black', linewidth=2)
                ax.add_patch(container)
                # Packed circles
                for (cx, cy, cr) in circles:
                    c = plt.Circle((cx, cy), cr, fill=True, facecolor='lightblue', 
                                  edgecolor='blue', linewidth=1)
                    ax.add_patch(c)
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "2D - Domain Warping":
                img = domain_warping_map(
                    width=p.get_value('width'),
                    height=p.get_value('height'),
                    base_scale=p.get_value('base_scale'),
                    warp_scale=p.get_value('base_scale') * 0.6,
                    warp_strength=p.get_value('warp_strength'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111)
                ax.imshow(img, origin='upper', cmap='viridis')
                ax.set_title(algo, fontsize=14, fontweight='bold')
                ax.axis('off')
            
            elif algo == "3D - Esfera Parametrica":
                ax = self.fig.add_subplot(111, projection='3d')
                X, Y, Z = sphere_parametric(n=p.get_value('resolution'), radius=1.0)
                ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=True)
                ax.set_title(algo, fontsize=14, fontweight='bold')
            
            elif algo == "3D - Terreno (Diamond-Square)":
                hm = diamond_square(n=129, roughness=p.get_value('roughness'), 
                                   seed=p.get_value('seed'))
                ax = self.fig.add_subplot(111, projection='3d')
                X, Y = np.meshgrid(np.arange(hm.shape[0]), np.arange(hm.shape[1]))
                ax.plot_surface(X, Y, hm, cmap='terrain', linewidth=0, antialiased=True)
                ax.set_title(algo, fontsize=14, fontweight='bold')
            
            elif algo == "3D - Terreno (Fault Formation)":
                hm = fault_formation(
                    size=p.get_value('size'),
                    iterations=p.get_value('iterations'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111, projection='3d')
                X, Y = np.meshgrid(np.arange(hm.shape[0]), np.arange(hm.shape[1]))
                ax.plot_surface(X, Y, hm, cmap='terrain', linewidth=0, antialiased=True)
                ax.set_title(algo, fontsize=14, fontweight='bold')
            
            elif algo == "3D - Voxel (Esfera)":
                n = p.get_value('grid_n')
                r = min(p.get_value('radius'), n//2-1)
                grid = voxel_grid_sphere(n=n, r=r)
                ax = self.fig.add_subplot(111, projection='3d')
                ax.voxels(grid, edgecolor='k', facecolors='cyan', alpha=0.7)
                ax.set_title(algo, fontsize=14, fontweight='bold')
            
            elif algo == "3D - Superficie Perlin (Heightmap)":
                n = p.get_value('resolution')
                hm = perlin_noise_2d_map(
                    width=n,
                    height=n,
                    scale=p.get_value('scale'),
                    octaves=p.get_value('octaves'),
                    seed=p.get_value('seed')
                )
                ax = self.fig.add_subplot(111, projection='3d')
                X, Y = np.meshgrid(np.arange(hm.shape[1]), np.arange(hm.shape[0]))
                ax.plot_surface(X, Y, hm, cmap='viridis', linewidth=0, antialiased=True)
                ax.set_title(algo, fontsize=14, fontweight='bold')
            
            self.canvas.draw()
            
        except Exception as e:
            print(f"Erro ao executar algoritmo: {e}")
            import traceback
            traceback.print_exc()
    
    def save_image(self):
        """Salva a imagem atual"""
        path, _ = QFileDialog.getSaveFileName(
            self, "Salvar imagem", "", 
            "PNG (*.png);;JPG (*.jpg);;SVG (*.svg)"
        )
        if path:
            try:
                self.fig.savefig(path, bbox_inches='tight', dpi=300)
                print(f"✓ Imagem salva em: {path}")
            except Exception as e:
                print(f"✗ Erro ao salvar imagem: {e}")

def main():
    app = QApplication(sys.argv)
    win = ProceduralExplorer()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
