import sys, os, math
import numpy as np
import cv2
from scipy.spatial import distance_matrix

from PyQt5 import QtCore, QtGui, QtWidgets

# -------------------------
# Utilidades de processamento
# -------------------------

def load_image_any(path):
    """Lê PNG com/sem alpha. Retorna (img_rgba uint8 HxWx4)."""
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Não foi possível abrir: {path}")
    if img.ndim == 2:  # grayscale -> RGBA
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
    if img.shape[2] == 3:  # BGR -> BGRA
        b,g,r = cv2.split(img)
        a = np.full_like(b, 255)
        img = cv2.merge([b,g,r,a])
    return img

def to_qpixmap(img_rgba):
    """Converte RGBA (OpenCV/BGRA) para QPixmap."""
    h, w = img_rgba.shape[:2]
    img_rgba_qt = cv2.cvtColor(img_rgba, cv2.COLOR_BGRA2RGBA)
    qimg = QtGui.QImage(img_rgba_qt.data, w, h, 4*w, QtGui.QImage.Format_RGBA8888)
    return QtGui.QPixmap.fromImage(qimg)

def binarize_edges(img_rgba):
    """Extrai as linhas da malha."""
    a = img_rgba[:,:,3]
    if np.any(a < 255):
        mask = (a > 0).astype(np.uint8)
    else:
        gray = cv2.cvtColor(img_rgba, cv2.COLOR_BGRA2GRAY)
        thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 31, 10)
        edges = cv2.Canny(thr, 60, 160, apertureSize=3, L2gradient=True)
        mask = (edges > 0).astype(np.uint8)
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
    return mask

def good_corners(mask, max_corners=800, min_dist=7):
    """Detecção de cantos com Shi-Tomasi."""
    img8 = (mask*255).astype(np.uint8)
    c = cv2.goodFeaturesToTrack(img8, maxCorners=max_corners,
                                qualityLevel=0.01, minDistance=min_dist,
                                blockSize=5, useHarrisDetector=True, k=0.06)
    if c is None:
        return np.empty((0,2), dtype=float)
    return c.reshape(-1,2)

def aggressive_clustering(points, eps=8.0):
    """Clustering iterativo: mescla pontos próximos até estabilizar."""
    if len(points) == 0:
        return np.empty((0,2), dtype=float)
    
    clusters = [[p] for p in points]
    
    changed = True
    iterations = 0
    max_iterations = 10
    
    while changed and iterations < max_iterations:
        changed = False
        iterations += 1
        
        centers = [np.mean(cluster, axis=0) for cluster in clusters]
        n = len(centers)
        
        merged = [False] * n
        new_clusters = []
        
        for i in range(n):
            if merged[i]:
                continue
                
            to_merge = [i]
            merged[i] = True
            
            for j in range(i+1, n):
                if merged[j]:
                    continue
                    
                dist = np.linalg.norm(centers[i] - centers[j])
                if dist <= eps:
                    to_merge.append(j)
                    merged[j] = True
                    changed = True
            
            merged_points = []
            for idx in to_merge:
                merged_points.extend(clusters[idx])
            
            new_clusters.append(merged_points)
        
        clusters = new_clusters
    
    final_centers = [np.mean(cluster, axis=0) for cluster in clusters]
    return np.array(final_centers, dtype=float)

def remove_close_points_strict(vertices, min_distance=5.0):
    """Remove vértices duplicados que estão muito próximos."""
    if len(vertices) <= 1:
        return vertices
    
    indices = np.lexsort((vertices[:,0], vertices[:,1]))
    sorted_verts = vertices[indices]
    
    keep = [True] * len(sorted_verts)
    
    for i in range(len(sorted_verts)):
        if not keep[i]:
            continue
            
        for j in range(i+1, len(sorted_verts)):
            if not keep[j]:
                continue
                
            dist = np.linalg.norm(sorted_verts[i] - sorted_verts[j])
            
            if dist < min_distance:
                keep[j] = False
    
    result = sorted_verts[keep]
    return result

def classify_vertices(vertices, junction_threshold=3, neighbor_radius=None):
    """
    Classifica vértices em três categorias baseado no número de vizinhos.
    Retorna: (junctions, edge_centers, cell_centers)
    """
    if len(vertices) == 0:
        return np.empty((0,2)), np.empty((0,2)), np.empty((0,2))
    
    if neighbor_radius is None:
        if len(vertices) > 1:
            D = distance_matrix(vertices, vertices)
            np.fill_diagonal(D, np.inf)
            min_dists = D.min(axis=1)
            neighbor_radius = np.median(min_dists) * 1.5
        else:
            neighbor_radius = 20.0
    
    D = distance_matrix(vertices, vertices)
    neighbor_counts = (D < neighbor_radius).sum(axis=1) - 1
    
    junctions = vertices[neighbor_counts >= junction_threshold]
    edge_centers = vertices[(neighbor_counts >= 2) & (neighbor_counts < junction_threshold)]
    cell_centers = vertices[neighbor_counts < 2]
    
    return junctions, edge_centers, cell_centers

def order_vertices_grid(vertices, row_thresh_frac=0.04):
    """Ordena vértices: cima→baixo (y), esquerda→direita (x)."""
    if len(vertices) == 0:
        return vertices

    verts = vertices.copy()
    ys = verts[:,1]
    xs = verts[:,0]
    order = np.argsort(ys)

    H = (ys.max() - ys.min() + 1)
    row_thresh = max(4.0, H * row_thresh_frac)

    rows = []
    cur = [order[0]]
    for idx in order[1:]:
        if abs(ys[idx]-ys[cur[-1]]) <= row_thresh:
            cur.append(idx)
        else:
            rows.append(cur)
            cur = [idx]
    rows.append(cur)

    new_order = []
    for r in rows:
        r_sorted = sorted(r, key=lambda i: xs[i])
        new_order.extend(r_sorted)
    return verts[new_order, :]

def draw_numbers_over(img_rgba, vertices, color=(0,0,255,255), fontsize=0.5, thickness=1):
    """Desenha números nos vértices. color em BGRA."""
    out = img_rgba.copy()
    for i,(x,y) in enumerate(vertices, start=1):
        cv2.putText(out, str(i), (int(x), int(y)),
                    cv2.FONT_HERSHEY_SIMPLEX, fontsize, color, thickness, cv2.LINE_AA)
    return out

# -------------------------
# Widget colapsável
# -------------------------

class CollapsibleBox(QtWidgets.QWidget):
    """Caixa que pode ser expandida/colapsada."""
    def __init__(self, title="", parent=None):
        super().__init__(parent)

        self.toggle_button = QtWidgets.QToolButton()
        self.toggle_button.setText(title)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; font-weight: bold; }")
        self.toggle_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
        self.toggle_button.clicked.connect(self.on_toggle)

        self.content_area = QtWidgets.QWidget()
        self.content_area.setMaximumHeight(0)
        self.content_area.setMinimumHeight(0)

        lay = QtWidgets.QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.toggle_button)
        lay.addWidget(self.content_area)

    def on_toggle(self):
        if self.toggle_button.isChecked():
            self.toggle_button.setArrowType(QtCore.Qt.DownArrow)
            self.content_area.setMaximumHeight(16777215)
        else:
            self.toggle_button.setArrowType(QtCore.Qt.RightArrow)
            self.content_area.setMaximumHeight(0)

    def setContentLayout(self, layout):
        self.content_area.setLayout(layout)

# -------------------------
# GUI
# -------------------------

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seeds Aura - Enumerador de Vértices")
        self.resize(1400, 800)

        self.img_path = None
        self.img_rgba = None
        self.all_vertices = None
        self.junctions = None
        self.edge_centers = None
        self.cell_centers = None
        self.output_img = None

        # ===== PAINEL LATERAL ESQUERDO =====
        
        left_panel = QtWidgets.QWidget()
        left_panel.setMaximumWidth(270)
        left_panel.setStyleSheet("background-color: #f5f5f5;")
        
        left_layout = QtWidgets.QVBoxLayout(left_panel)
        left_layout.setContentsMargins(10, 10, 10, 10)
        left_layout.setSpacing(10)
        
        # Botões principais
        self.btn_open = QtWidgets.QPushButton("📁 Abrir Imagem")
        self.btn_open.setMinimumHeight(40)
        self.btn_open.setStyleSheet("font-size: 11pt; font-weight: bold;")
        
        self.btn_process = QtWidgets.QPushButton("⚙️ Detectar Vértices")
        self.btn_process.setMinimumHeight(40)
        self.btn_process.setEnabled(False)
        self.btn_process.setStyleSheet("font-size: 11pt; font-weight: bold;")
        
        left_layout.addWidget(self.btn_open)
        left_layout.addWidget(self.btn_process)
        
        # ===== Parâmetros de Detecção (COLAPSÁVEL) =====
        
        params_box = CollapsibleBox("⚙️ Parâmetros de Detecção")
        params_layout = QtWidgets.QFormLayout()
        params_layout.setSpacing(8)
        
        self.spin_eps = QtWidgets.QDoubleSpinBox()
        self.spin_eps.setDecimals(1)
        self.spin_eps.setRange(3.0, 30.0)
        self.spin_eps.setValue(10.0)
        self.spin_eps.setSingleStep(0.5)
        
        self.spin_min_dist = QtWidgets.QDoubleSpinBox()
        self.spin_min_dist.setDecimals(1)
        self.spin_min_dist.setRange(2.0, 20.0)
        self.spin_min_dist.setValue(8.0)
        self.spin_min_dist.setSingleStep(0.5)

        self.spin_junction_thresh = QtWidgets.QSpinBox()
        self.spin_junction_thresh.setRange(2, 8)
        self.spin_junction_thresh.setValue(3)
        
        self.spin_row_tolerance = QtWidgets.QDoubleSpinBox()
        self.spin_row_tolerance.setDecimals(3)
        self.spin_row_tolerance.setRange(0.01, 0.15)
        self.spin_row_tolerance.setValue(0.040)
        self.spin_row_tolerance.setSingleStep(0.005)
        
        params_layout.addRow("Raio de fusão:", self.spin_eps)
        params_layout.addRow("Dist. mínima:", self.spin_min_dist)
        params_layout.addRow("Vizinhos p/ junção:", self.spin_junction_thresh)
        params_layout.addRow("Tolerância linha:", self.spin_row_tolerance)
        
        params_box.setContentLayout(params_layout)
        left_layout.addWidget(params_box)
        
        # ===== O que Enumerar =====
        
        enum_group = QtWidgets.QGroupBox("🔢 O que Enumerar")
        enum_layout = QtWidgets.QVBoxLayout()
        enum_layout.setSpacing(5)
        
        self.radio_all = QtWidgets.QRadioButton("Todos os pontos")
        self.radio_junctions = QtWidgets.QRadioButton("Apenas JUNÇÕES (vértices)")
        self.radio_edges = QtWidgets.QRadioButton("Apenas CENTROS DE ARESTA")
        self.radio_cells = QtWidgets.QRadioButton("Apenas CENTROS DE CÉLULA")
        self.radio_all.setChecked(True)
        
        enum_layout.addWidget(self.radio_all)
        enum_layout.addWidget(self.radio_junctions)
        enum_layout.addWidget(self.radio_edges)
        enum_layout.addWidget(self.radio_cells)
        
        enum_group.setLayout(enum_layout)
        left_layout.addWidget(enum_group)
        
        # ===== Aparência =====
        
        appearance_group = QtWidgets.QGroupBox("🎨 Aparência")
        appearance_layout = QtWidgets.QFormLayout()
        appearance_layout.setSpacing(8)
        
        self.cmb_color = QtWidgets.QComboBox()
        self.cmb_color.addItems(["Vermelho", "Azul", "Verde", "Preto", "Branco", "Laranja"])
        self.cmb_color.setCurrentIndex(0)
        
        self.spin_font = QtWidgets.QDoubleSpinBox()
        self.spin_font.setDecimals(2)
        self.spin_font.setRange(0.3, 2.5)
        self.spin_font.setSingleStep(0.05)
        self.spin_font.setValue(0.70)
        
        self.spin_thick = QtWidgets.QSpinBox()
        self.spin_thick.setRange(1, 5)
        self.spin_thick.setValue(2)
        
        appearance_layout.addRow("Cor:", self.cmb_color)
        appearance_layout.addRow("Tamanho:", self.spin_font)
        appearance_layout.addRow("Espessura:", self.spin_thick)
        
        appearance_group.setLayout(appearance_layout)
        left_layout.addWidget(appearance_group)
        
        # ===== Botão Limpar =====
        
        self.btn_clear = QtWidgets.QPushButton("🧹 Limpar Numeração")
        self.btn_clear.setMinimumHeight(35)
        self.btn_clear.setEnabled(False)
        self.btn_clear.setStyleSheet("background-color: #fff3cd; border: 1px solid #ffc107;")
        self.btn_clear.setToolTip("Remove a numeração mas mantém os vértices detectados")
        left_layout.addWidget(self.btn_clear)
        
        # ===== Status e Informações =====
        
        self.status_label = QtWidgets.QLabel("Aguardando imagem...")
        self.status_label.setStyleSheet("""
            background-color: white;
            color: #666;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-weight: bold;
        """)
        self.status_label.setWordWrap(True)
        left_layout.addWidget(self.status_label)
        
        self.info_label = QtWidgets.QLabel()
        self.info_label.setStyleSheet("""
            background-color: white;
            color: #333;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 9pt;
        """)
        self.info_label.setWordWrap(True)
        self.info_label.hide()
        left_layout.addWidget(self.info_label)
        
        # Botões de salvar
        self.btn_save_img = QtWidgets.QPushButton("💾 Salvar PNG")
        self.btn_save_img.setMinimumHeight(35)
        self.btn_save_img.setEnabled(False)
        
        self.btn_save_csv = QtWidgets.QPushButton("📊 Salvar CSV")
        self.btn_save_csv.setMinimumHeight(35)
        self.btn_save_csv.setEnabled(False)
        
        left_layout.addWidget(self.btn_save_img)
        left_layout.addWidget(self.btn_save_csv)
        
        left_layout.addStretch()
        
        # ===== ÁREA DE VISUALIZAÇÃO (DIREITA) =====
        
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("background-color: white; border: 2px solid #ddd;")
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(self.label)
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        
        # ===== LAYOUT PRINCIPAL =====
        
        main_widget = QtWidgets.QWidget()
        main_layout = QtWidgets.QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        main_layout.addWidget(left_panel)
        main_layout.addWidget(scroll, 1)
        
        self.setCentralWidget(main_widget)

        # ===== SIGNALS =====
        
        self.btn_open.clicked.connect(self.on_open)
        self.btn_process.clicked.connect(self.on_process)
        self.btn_clear.clicked.connect(self.on_clear)
        self.btn_save_img.clicked.connect(self.on_save_img)
        self.btn_save_csv.clicked.connect(self.on_save_csv)
        
        self.radio_all.toggled.connect(self.on_enumeration_changed)
        self.radio_junctions.toggled.connect(self.on_enumeration_changed)
        self.radio_edges.toggled.connect(self.on_enumeration_changed)
        self.radio_cells.toggled.connect(self.on_enumeration_changed)
        
        self.cmb_color.currentIndexChanged.connect(self.on_appearance_changed)
        self.spin_font.valueChanged.connect(self.on_appearance_changed)
        self.spin_thick.valueChanged.connect(self.on_appearance_changed)

    def update_status(self, text, color="#666"):
        """Atualiza o label de status com cor."""
        self.status_label.setText(text)
        self.status_label.setStyleSheet(f"""
            background-color: white;
            color: {color};
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-weight: bold;
        """)

    def on_open(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Escolha a imagem da malha", "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)")
        if not path:
            return
        try:
            self.img_rgba = load_image_any(path)
            self.img_path = path
            self.all_vertices = None
            self.junctions = None
            self.edge_centers = None
            self.cell_centers = None
            self.output_img = None
            
            self.btn_process.setEnabled(True)
            self.btn_clear.setEnabled(False)
            self.btn_save_img.setEnabled(False)
            self.btn_save_csv.setEnabled(False)
            self.info_label.hide()
            
            self.update_status(f"Imagem carregada: {os.path.basename(path)}", "green")
            
            pixmap = to_qpixmap(self.img_rgba)
            self.label.setPixmap(pixmap)
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", f"Não foi possível abrir:\n{str(e)}")
            self.update_status("Erro ao carregar imagem", "red")

    def on_process(self):
        if self.img_rgba is None:
            return
        
        try:
            eps = float(self.spin_eps.value())
            min_dist = float(self.spin_min_dist.value())
            junction_thresh = int(self.spin_junction_thresh.value())

            self.update_status("Processando: detectando bordas...", "blue")
            QtWidgets.QApplication.processEvents()

            mask = binarize_edges(self.img_rgba)
            
            self.update_status("Processando: detectando cantos...", "blue")
            QtWidgets.QApplication.processEvents()
            
            pts = good_corners(mask, max_corners=2000, min_dist=int(min_dist*0.7))
            if len(pts) == 0:
                raise RuntimeError("Nenhum canto detectado.")

            self.update_status(f"Processando: agrupando {len(pts)} pontos...", "blue")
            QtWidgets.QApplication.processEvents()

            verts = aggressive_clustering(pts, eps=eps)
            
            self.update_status(f"Processando: removendo duplicatas...", "blue")
            QtWidgets.QApplication.processEvents()
            
            verts = remove_close_points_strict(verts, min_distance=min_dist)
            verts = remove_close_points_strict(verts, min_distance=min_dist*0.8)
            
            self.update_status(f"Processando: classificando vértices...", "blue")
            QtWidgets.QApplication.processEvents()
            
            self.junctions, self.edge_centers, self.cell_centers = classify_vertices(
                verts, junction_threshold=junction_thresh)
            
            self.all_vertices = verts
            
            # Atualiza informações
            info_text = (
                f"<b>Resultados da Classificação:</b><br>"
                f"🔶 <b>Junções:</b> {len(self.junctions)} pontos<br>"
                f"🔷 <b>Centros de aresta:</b> {len(self.edge_centers)} pontos<br>"
                f"🔵 <b>Centros de célula:</b> {len(self.cell_centers)} pontos<br>"
                f"<b>TOTAL:</b> {len(verts)} vértices detectados"
            )
            self.info_label.setText(info_text)
            self.info_label.show()
            
            self.btn_clear.setEnabled(True)
            self.btn_save_img.setEnabled(True)
            self.btn_save_csv.setEnabled(True)
            
            self.update_visualization()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro", str(e))
            self.update_status(f"Erro: {str(e)}", "red")

    def on_clear(self):
        """Limpa a numeração mas mantém os vértices detectados."""
        if self.img_rgba is None:
            return
        
        # Mostra imagem original sem numeração
        pixmap = to_qpixmap(self.img_rgba)
        self.label.setPixmap(pixmap)
        
        self.output_img = None
        self.btn_save_img.setEnabled(False)
        
        self.update_status("Numeração removida. Clique em 'Detectar Vértices' para enumerar novamente.", "orange")

    def on_enumeration_changed(self):
        if self.all_vertices is not None:
            self.update_visualization()

    def on_appearance_changed(self):
        if self.all_vertices is not None:
            self.update_visualization()

    def update_visualization(self):
        if self.all_vertices is None:
            return
        
        # Seleciona vértices
        if self.radio_junctions.isChecked():
            vertices_to_draw = self.junctions
            type_name = "junções"
        elif self.radio_edges.isChecked():
            vertices_to_draw = self.edge_centers
            type_name = "centros de aresta"
        elif self.radio_cells.isChecked():
            vertices_to_draw = self.cell_centers
            type_name = "centros de célula"
        else:
            vertices_to_draw = self.all_vertices
            type_name = "todos os pontos"
        
        if len(vertices_to_draw) == 0:
            self.update_status(f"Nenhum vértice do tipo '{type_name}'", "orange")
            pixmap = to_qpixmap(self.img_rgba)
            self.label.setPixmap(pixmap)
            return
        
        # Ordena
        row_tolerance = float(self.spin_row_tolerance.value())
        vertices_ordered = order_vertices_grid(vertices_to_draw, row_thresh_frac=row_tolerance)
        
        # Desenha
        color = self.get_color_bgra()
        self.output_img = draw_numbers_over(
            self.img_rgba, vertices_ordered, color=color,
            fontsize=float(self.spin_font.value()),
            thickness=int(self.spin_thick.value()))
        
        pixmap = to_qpixmap(self.output_img)
        self.label.setPixmap(pixmap)
        
        self.btn_save_img.setEnabled(True)
        self.update_status(f"Exibindo: {len(vertices_ordered)} {type_name} numerados", "green")

    def get_color_bgra(self):
        name = self.cmb_color.currentText().lower()
        colors = {
            "vermelho": (0, 0, 255, 255),
            "azul": (255, 0, 0, 255),
            "verde": (0, 180, 0, 255),
            "preto": (0, 0, 0, 255),
            "branco": (255, 255, 255, 255),
            "laranja": (0, 165, 255, 255)
        }
        return colors.get(name, (0, 0, 255, 255))

    def on_save_img(self):
        if self.output_img is None:
            return
        
        if self.radio_junctions.isChecked():
            suffix = "_juncoes"
        elif self.radio_edges.isChecked():
            suffix = "_centros_aresta"
        elif self.radio_cells.isChecked():
            suffix = "_centros_celula"
        else:
            suffix = "_todos"
        
        base = os.path.splitext(os.path.basename(self.img_path))[0]
        default_name = f"{base}{suffix}.png"
        
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Salvar imagem numerada", default_name, "PNG (*.png)")
        
        if not path:
            return
        
        try:
            if not path.lower().endswith('.png'):
                path += '.png'
            
            cv2.imwrite(path, self.output_img)
            QtWidgets.QMessageBox.information(self, "Sucesso!", f"Imagem salva:\n{path}")
            self.update_status(f"PNG salvo: {os.path.basename(path)}", "green")
                
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro ao salvar", str(e))

    def on_save_csv(self):
        if self.all_vertices is None:
            return
        
        row_tolerance = float(self.spin_row_tolerance.value())
        
        if self.radio_junctions.isChecked():
            vertices = order_vertices_grid(self.junctions, row_thresh_frac=row_tolerance)
            suffix = "_juncoes"
            type_name = "junções"
        elif self.radio_edges.isChecked():
            vertices = order_vertices_grid(self.edge_centers, row_thresh_frac=row_tolerance)
            suffix = "_centros_aresta"
            type_name = "centros de aresta"
        elif self.radio_cells.isChecked():
            vertices = order_vertices_grid(self.cell_centers, row_thresh_frac=row_tolerance)
            suffix = "_centros_celula"
            type_name = "centros de célula"
        else:
            vertices = order_vertices_grid(self.all_vertices, row_thresh_frac=row_tolerance)
            suffix = "_todos"
            type_name = "todos os pontos"
        
        if len(vertices) == 0:
            QtWidgets.QMessageBox.warning(self, "Aviso", f"Nenhum vértice de '{type_name}'.")
            return
        
        base = os.path.splitext(os.path.basename(self.img_path))[0]
        default_name = f"{base}{suffix}.csv"
        
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Salvar coordenadas CSV", default_name, "CSV (*.csv)")
        
        if not path:
            return
        
        try:
            ids = np.arange(1, len(vertices)+1, dtype=int).reshape(-1,1)
            arr = np.hstack([ids, vertices])
            np.savetxt(path, arr, fmt=["%d","%.2f","%.2f"], delimiter=",",
                       header="id,x,y", comments="")
            
            QtWidgets.QMessageBox.information(
                self, "Sucesso!", f"CSV salvo com {len(vertices)} {type_name}:\n{path}")
            self.update_status(f"CSV salvo: {os.path.basename(path)}", "green")
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erro ao salvar CSV", str(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
