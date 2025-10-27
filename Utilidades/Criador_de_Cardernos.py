#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Cadernos Personalizados
-----------------------------------
Crie cadernos com diferentes padrões de grade personalizáveis
com preview em tempo real!

Autor: Claude
Data: 20/10/2025
"""

import sys
import math
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, QSpinBox, QDoubleSpinBox,
    QGroupBox, QFormLayout, QFileDialog, QColorDialog, QCheckBox,
    QScrollArea
)
from PyQt5.QtGui import (QPainter, QPen, QColor, QPageSize, QPdfWriter, 
                         QPixmap, QPainterPath, QImage)
from PyQt5.QtCore import Qt, QRectF, QPointF, QSize

# Conversão: 1mm = 3.779528 pixels em 96 DPI
MM_TO_PX = 3.779528

class PreviewCanvas(QLabel):
    """Canvas para mostrar o preview do caderno"""
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("QLabel { background-color: white; border: 1px solid #ccc; }")
        self.setMinimumSize(600, 800)
        self.current_pixmap = None
    
    def set_pattern(self, pixmap):
        """Define o padrão a ser exibido"""
        self.current_pixmap = pixmap
        # Escala para caber na tela mantendo proporção
        scaled = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled)
    
    def resizeEvent(self, event):
        """Reescala quando redimensionar a janela"""
        super().resizeEvent(event)
        if self.current_pixmap:
            scaled = self.current_pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled)


class NotebookGenerator:
    """Classe para gerar diferentes tipos de padrões de caderno"""
    
    @staticmethod
    def draw_grid(painter, width, height, square_size, line_width, color, 
                  margin, highlight_every=0, highlight_width=0):
        """Desenha grade quadriculada"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        # Linhas verticais
        x = margin
        count = 0
        while x <= width - margin:
            if highlight_every > 0 and count % highlight_every == 0 and count > 0:
                pen.setWidthF(highlight_width)
                painter.setPen(pen)
                painter.drawLine(QPointF(x, margin), QPointF(x, height - margin))
                pen.setWidthF(line_width)
                painter.setPen(pen)
            else:
                painter.drawLine(QPointF(x, margin), QPointF(x, height - margin))
            x += square_size
            count += 1
        
        # Linhas horizontais
        y = margin
        count = 0
        while y <= height - margin:
            if highlight_every > 0 and count % highlight_every == 0 and count > 0:
                pen.setWidthF(highlight_width)
                painter.setPen(pen)
                painter.drawLine(QPointF(margin, y), QPointF(width - margin, y))
                pen.setWidthF(line_width)
                painter.setPen(pen)
            else:
                painter.drawLine(QPointF(margin, y), QPointF(width - margin, y))
            y += square_size
            count += 1
    
    @staticmethod
    def draw_dots(painter, width, height, dot_spacing, dot_size, color, margin):
        """Desenha grade de pontos (dot grid)"""
        pen = QPen(color)
        pen.setWidthF(dot_size)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        
        y = margin
        while y <= height - margin:
            x = margin
            while x <= width - margin:
                painter.drawPoint(QPointF(x, y))
                x += dot_spacing
            y += dot_spacing
    
    @staticmethod
    def draw_hexagons(painter, width, height, hex_size, line_width, color, margin):
        """Desenha grade hexagonal"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        # Geometria do hexágono
        h = hex_size * math.sqrt(3) / 2
        w = hex_size * 1.5
        
        row = 0
        y = margin
        while y < height - margin + h:
            col = 0
            x = margin
            offset = (w / 3) if row % 2 == 1 else 0
            
            while x < width - margin + hex_size:
                cx = x + offset
                cy = y
                
                # Desenha hexágono
                points = []
                for i in range(6):
                    angle = math.pi / 3 * i
                    px = cx + hex_size * math.cos(angle)
                    py = cy + hex_size * math.sin(angle)
                    points.append(QPointF(px, py))
                
                for i in range(6):
                    painter.drawLine(points[i], points[(i + 1) % 6])
                
                x += w
                col += 1
            y += h
            row += 1
    
    @staticmethod
    def draw_isometric(painter, width, height, grid_size, line_width, color, margin):
        """Desenha grade isométrica (triângulos)"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        h = grid_size * math.sqrt(3) / 2
        
        # Linhas inclinadas à direita (30°)
        x = margin - (height - 2*margin) / math.sqrt(3)
        while x <= width - margin + grid_size:
            painter.drawLine(QPointF(x, margin), 
                           QPointF(x + (height - 2*margin) / math.sqrt(3), height - margin))
            x += grid_size
        
        # Linhas inclinadas à esquerda (-30°)
        x = margin
        while x <= width - margin + (height - 2*margin) / math.sqrt(3) + grid_size:
            painter.drawLine(QPointF(x, margin), 
                           QPointF(x - (height - 2*margin) / math.sqrt(3), height - margin))
            x += grid_size
        
        # Linhas horizontais
        y = margin
        while y <= height - margin:
            painter.drawLine(QPointF(margin, y), QPointF(width - margin, y))
            y += h
    
    @staticmethod
    def draw_ruled(painter, width, height, line_spacing, line_width, color, margin):
        """Desenha linhas pautadas (ruled)"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        y = margin + line_spacing
        while y <= height - margin:
            painter.drawLine(QPointF(margin, y), QPointF(width - margin, y))
            y += line_spacing
        
        # Linha vertical da margem esquerda
        margin_line = margin + line_spacing * 2
        pen.setColor(QColor(255, 200, 200, 100))
        painter.setPen(pen)
        painter.drawLine(QPointF(margin_line, margin), 
                        QPointF(margin_line, height - margin))
    
    @staticmethod
    def draw_music(painter, width, height, staff_height, line_width, color, margin):
        """Desenha pautas musicais"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        y = margin + staff_height
        while y <= height - margin - staff_height * 4:
            # Desenha 5 linhas da pauta
            for i in range(5):
                line_y = y + i * (staff_height / 4)
                painter.drawLine(QPointF(margin, line_y), 
                               QPointF(width - margin, line_y))
            
            y += staff_height * 2
    
    @staticmethod
    def draw_polar(painter, width, height, num_circles, num_rays, line_width, color, margin):
        """Desenha grade polar/circular"""
        pen = QPen(color)
        pen.setWidthF(line_width)
        painter.setPen(pen)
        
        cx = width / 2
        cy = height / 2
        max_radius = min(width, height) / 2 - margin
        
        # Círculos concêntricos
        for i in range(1, num_circles + 1):
            radius = (max_radius / num_circles) * i
            painter.drawEllipse(QPointF(cx, cy), radius, radius)
        
        # Raios
        for i in range(num_rays):
            angle = (2 * math.pi / num_rays) * i
            x1 = cx
            y1 = cy
            x2 = cx + max_radius * math.cos(angle)
            y2 = cy + max_radius * math.sin(angle)
            painter.drawLine(QPointF(x1, y1), QPointF(x2, y2))
    
    @staticmethod
    def draw_calligraphy(painter, width, height, line_height, line_width, color, margin):
        """Desenha guias para caligrafia"""
        pen_main = QPen(color)
        pen_main.setWidthF(line_width * 1.5)
        
        pen_guide = QPen(QColor(color.red(), color.green(), color.blue(), 80))
        pen_guide.setWidthF(line_width * 0.5)
        pen_guide.setStyle(Qt.DashLine)
        
        y = margin + line_height
        while y <= height - margin:
            # Linha base (forte)
            painter.setPen(pen_main)
            painter.drawLine(QPointF(margin, y), QPointF(width - margin, y))
            
            # Linha superior (forte)
            painter.drawLine(QPointF(margin, y - line_height), 
                           QPointF(width - margin, y - line_height))
            
            # Linhas guia (tracejadas)
            painter.setPen(pen_guide)
            painter.drawLine(QPointF(margin, y - line_height * 0.33), 
                           QPointF(width - margin, y - line_height * 0.33))
            painter.drawLine(QPointF(margin, y - line_height * 0.66), 
                           QPointF(width - margin, y - line_height * 0.66))
            
            y += line_height * 1.5


class NotebookGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Cadernos Personalizados")
        self.setGeometry(50, 50, 1400, 900)
        
        # Cor padrão
        self.current_color = QColor(180, 180, 180)
        
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)
        
        # PAINEL ESQUERDO - Controles
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_panel.setMaximumWidth(400)
        
        # Título
        title = QLabel("📓 Gerador de Cadernos")
        title.setStyleSheet("font-size: 18px; font-weight: bold; padding: 10px;")
        left_layout.addWidget(title)
        
        # Seleção de tipo
        type_group = QGroupBox("Tipo de Caderno")
        type_layout = QVBoxLayout()
        self.pattern_combo = QComboBox()
        self.pattern_combo.addItems([
            "Grade Quadriculada",
            "Grade de Pontos (Dot Grid)",
            "Grade Hexagonal",
            "Grade Isométrica",
            "Linhas Pautadas",
            "Pautas Musicais",
            "Grade Polar/Circular",
            "Guias para Caligrafia"
        ])
        self.pattern_combo.currentIndexChanged.connect(self.update_params_visibility)
        type_layout.addWidget(self.pattern_combo)
        type_group.setLayout(type_layout)
        left_layout.addWidget(type_group)
        
        # Configurações de página
        page_group = QGroupBox("Configurações da Página")
        page_layout = QFormLayout()
        
        self.page_size = QComboBox()
        self.page_size.addItems(["A4", "A5", "Carta (Letter)", "A3"])
        page_layout.addRow("Tamanho:", self.page_size)
        
        self.margin_spin = QDoubleSpinBox()
        self.margin_spin.setRange(0, 50)
        self.margin_spin.setValue(15)
        self.margin_spin.setSuffix(" mm")
        page_layout.addRow("Margem:", self.margin_spin)
        
        page_group.setLayout(page_layout)
        left_layout.addWidget(page_group)
        
        # Parâmetros do padrão
        self.params_group = QGroupBox("Parâmetros do Padrão")
        self.params_layout = QFormLayout()
        
        # Tamanho do quadrado/espaçamento
        self.size_spin = QDoubleSpinBox()
        self.size_spin.setRange(1, 50)
        self.size_spin.setValue(5)
        self.size_spin.setSuffix(" mm")
        self.size_label = QLabel("Tamanho do quadrado:")
        self.params_layout.addRow(self.size_label, self.size_spin)
        
        # Espessura da linha
        self.thickness_spin = QDoubleSpinBox()
        self.thickness_spin.setRange(0.1, 5)
        self.thickness_spin.setValue(0.3)
        self.thickness_spin.setSingleStep(0.1)
        self.thickness_spin.setSuffix(" mm")
        self.params_layout.addRow("Espessura da linha:", self.thickness_spin)
        
        # Destaque a cada N linhas (para grade)
        self.highlight_check = QCheckBox("Destacar a cada")
        self.highlight_every = QSpinBox()
        self.highlight_every.setRange(2, 20)
        self.highlight_every.setValue(5)
        self.highlight_every.setSuffix(" linhas")
        self.highlight_width = QDoubleSpinBox()
        self.highlight_width.setRange(0.1, 5)
        self.highlight_width.setValue(0.8)
        self.highlight_width.setSuffix(" mm")
        highlight_layout = QHBoxLayout()
        highlight_layout.addWidget(self.highlight_check)
        highlight_layout.addWidget(self.highlight_every)
        highlight_layout.addWidget(QLabel("Esp:"))
        highlight_layout.addWidget(self.highlight_width)
        self.params_layout.addRow(highlight_layout)
        
        # Parâmetros específicos para polar
        self.circles_spin = QSpinBox()
        self.circles_spin.setRange(3, 30)
        self.circles_spin.setValue(10)
        self.circles_label = QLabel("Número de círculos:")
        self.params_layout.addRow(self.circles_label, self.circles_spin)
        
        self.rays_spin = QSpinBox()
        self.rays_spin.setRange(4, 72)
        self.rays_spin.setValue(12)
        self.rays_label = QLabel("Número de raios:")
        self.params_layout.addRow(self.rays_label, self.rays_spin)
        
        self.params_group.setLayout(self.params_layout)
        left_layout.addWidget(self.params_group)
        
        # Cor
        color_group = QGroupBox("Aparência")
        color_layout = QHBoxLayout()
        color_layout.addWidget(QLabel("Cor:"))
        self.color_btn = QPushButton("Escolher Cor")
        self.color_btn.clicked.connect(self.choose_color)
        self.update_color_button()
        color_layout.addWidget(self.color_btn)
        color_layout.addStretch()
        color_group.setLayout(color_layout)
        left_layout.addWidget(color_group)
        
        # Botões de ação
        self.generate_btn = QPushButton("🎨 Gerar Preview")
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_preview)
        left_layout.addWidget(self.generate_btn)
        
        self.export_btn = QPushButton("💾 Salvar como PDF")
        self.export_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
        """)
        self.export_btn.clicked.connect(self.export_pdf)
        self.export_btn.setEnabled(False)
        left_layout.addWidget(self.export_btn)
        
        # Info
        info_label = QLabel(
            "💡 Primeiro clique em 'Gerar Preview' para ver o resultado!\n"
            "Depois você pode salvar em PDF se gostar."
        )
        info_label.setWordWrap(True)
        info_label.setStyleSheet("QLabel { color: #666; font-size: 11px; padding: 10px; background-color: #f0f0f0; border-radius: 5px; }")
        left_layout.addWidget(info_label)
        
        left_layout.addStretch()
        
        # PAINEL DIREITO - Preview
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        
        preview_label = QLabel("Preview do Caderno")
        preview_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px;")
        right_layout.addWidget(preview_label)
        
        # Área de scroll para o preview
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        self.preview_canvas = PreviewCanvas()
        scroll.setWidget(self.preview_canvas)
        right_layout.addWidget(scroll)
        
        # Adiciona os painéis ao layout principal
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)
        
        self.update_params_visibility()
        
        # Gera preview inicial
        self.generate_preview()
    
    def update_params_visibility(self):
        """Atualiza visibilidade dos parâmetros baseado no tipo selecionado"""
        pattern_type = self.pattern_combo.currentText()
        
        # Esconde todos primeiro
        self.size_label.hide()
        self.size_spin.hide()
        self.highlight_check.hide()
        self.highlight_every.hide()
        self.highlight_width.hide()
        self.circles_label.hide()
        self.circles_spin.hide()
        self.rays_label.hide()
        self.rays_spin.hide()
        
        # Mostra os relevantes
        if "Quadriculada" in pattern_type:
            self.size_label.setText("Tamanho do quadrado:")
            self.size_label.show()
            self.size_spin.show()
            self.highlight_check.show()
            self.highlight_every.show()
            self.highlight_width.show()
        elif "Pontos" in pattern_type:
            self.size_label.setText("Espaçamento dos pontos:")
            self.size_label.show()
            self.size_spin.show()
        elif "Hexagonal" in pattern_type:
            self.size_label.setText("Tamanho do hexágono:")
            self.size_label.show()
            self.size_spin.show()
        elif "Isométrica" in pattern_type:
            self.size_label.setText("Tamanho da grade:")
            self.size_label.show()
            self.size_spin.show()
        elif "Pautadas" in pattern_type:
            self.size_label.setText("Espaçamento das linhas:")
            self.size_label.show()
            self.size_spin.setValue(8)
            self.size_spin.show()
        elif "Musicais" in pattern_type:
            self.size_label.setText("Altura da pauta:")
            self.size_label.show()
            self.size_spin.setValue(20)
            self.size_spin.show()
        elif "Polar" in pattern_type:
            self.circles_label.show()
            self.circles_spin.show()
            self.rays_label.show()
            self.rays_spin.show()
        elif "Caligrafia" in pattern_type:
            self.size_label.setText("Altura da linha:")
            self.size_label.show()
            self.size_spin.setValue(15)
            self.size_spin.show()
    
    def choose_color(self):
        """Abre diálogo para escolher cor"""
        color = QColorDialog.getColor(self.current_color, self)
        if color.isValid():
            self.current_color = color
            self.update_color_button()
    
    def update_color_button(self):
        """Atualiza a aparência do botão de cor"""
        self.color_btn.setStyleSheet(
            f"QPushButton {{ background-color: rgb({self.current_color.red()}, "
            f"{self.current_color.green()}, {self.current_color.blue()}); "
            f"color: {'white' if self.current_color.lightness() < 128 else 'black'}; "
            f"padding: 5px; border-radius: 3px; }}"
        )
    
    def get_page_dimensions(self):
        """Retorna dimensões da página em mm"""
        page_type = self.page_size.currentText()
        if page_type == "A4":
            return 210, 297
        elif page_type == "A5":
            return 148, 210
        elif page_type == "Carta (Letter)":
            return 215.9, 279.4
        elif page_type == "A3":
            return 297, 420
        return 210, 297
    
    def draw_pattern(self, painter, width_mm, height_mm):
        """Desenha o padrão selecionado"""
        pattern_type = self.pattern_combo.currentText()
        
        # Converte dimensões para pixels
        width = width_mm * MM_TO_PX
        height = height_mm * MM_TO_PX
        margin = self.margin_spin.value() * MM_TO_PX
        size = self.size_spin.value() * MM_TO_PX
        thickness = self.thickness_spin.value() * MM_TO_PX
        
        gen = NotebookGenerator()
        
        if "Quadriculada" in pattern_type:
            highlight_every = self.highlight_every.value() if self.highlight_check.isChecked() else 0
            highlight_width = self.highlight_width.value() * MM_TO_PX
            gen.draw_grid(painter, width, height, size, thickness, 
                         self.current_color, margin, highlight_every, highlight_width)
        
        elif "Pontos" in pattern_type:
            dot_size = thickness * 2
            gen.draw_dots(painter, width, height, size, dot_size, 
                         self.current_color, margin)
        
        elif "Hexagonal" in pattern_type:
            gen.draw_hexagons(painter, width, height, size, thickness, 
                            self.current_color, margin)
        
        elif "Isométrica" in pattern_type:
            gen.draw_isometric(painter, width, height, size, thickness, 
                             self.current_color, margin)
        
        elif "Pautadas" in pattern_type:
            gen.draw_ruled(painter, width, height, size, thickness, 
                          self.current_color, margin)
        
        elif "Musicais" in pattern_type:
            gen.draw_music(painter, width, height, size, thickness, 
                          self.current_color, margin)
        
        elif "Polar" in pattern_type:
            gen.draw_polar(painter, width, height, 
                          self.circles_spin.value(), 
                          self.rays_spin.value(), 
                          thickness, self.current_color, margin)
        
        elif "Caligrafia" in pattern_type:
            gen.draw_calligraphy(painter, width, height, size, thickness, 
                               self.current_color, margin)
    
    def generate_preview(self):
        """Gera o preview do caderno"""
        width_mm, height_mm = self.get_page_dimensions()
        
        # Cria imagem em alta resolução para preview
        width_px = int(width_mm * MM_TO_PX * 2)  # 2x para melhor qualidade
        height_px = int(height_mm * MM_TO_PX * 2)
        
        pixmap = QPixmap(width_px, height_px)
        pixmap.fill(Qt.white)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(2, 2)  # Escala para melhor qualidade
        
        self.draw_pattern(painter, width_mm, height_mm)
        
        painter.end()
        
        self.preview_canvas.set_pattern(pixmap)
        self.export_btn.setEnabled(True)
        
        self.statusBar().showMessage("✅ Preview gerado com sucesso! Agora você pode salvar em PDF se quiser.", 5000)
    
    def export_pdf(self):
        """Exporta o caderno para PDF"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Salvar Caderno", "", "PDF Files (*.pdf)"
        )
        
        if not filename:
            return
        
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        
        width_mm, height_mm = self.get_page_dimensions()
        
        # Cria PDF writer
        writer = QPdfWriter(filename)
        
        # Define tamanho da página
        page_type = self.page_size.currentText()
        if "A4" in page_type:
            writer.setPageSize(QPageSize(QPageSize.A4))
        elif "A5" in page_type:
            writer.setPageSize(QPageSize(QPageSize.A5))
        elif "A3" in page_type:
            writer.setPageSize(QPageSize(QPageSize.A3))
        else:
            writer.setPageSize(QPageSize(QPageSize.Letter))
        
        writer.setResolution(300)  # 300 DPI para alta qualidade
        
        # Cria painter
        painter = QPainter(writer)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Desenha o padrão
        self.draw_pattern(painter, width_mm, height_mm)
        
        painter.end()
        
        self.statusBar().showMessage(f"✅ Caderno salvo com sucesso em: {filename}", 5000)


def main():
    app = QApplication(sys.argv)
    window = NotebookGeneratorGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()