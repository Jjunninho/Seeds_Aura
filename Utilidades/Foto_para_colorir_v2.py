#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Foto para Desenho de Colorir v2.0
Transforma fotos em line art (caderno de pintar) com fundo transparente
Inclui 8 métodos de reparo de arquivos problemáticos
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Scale
from PIL import Image, ImageTk
from pathlib import Path
import os


class ReparadorArquivos:
    """8 métodos para abrir arquivos problemáticos"""
    
    @staticmethod
    def tentar_abrir(path):
        """Tenta todos os 8 métodos até conseguir abrir"""
        methods = [
            ("OpenCV padrão", ReparadorArquivos.method_cv2_default),
            ("OpenCV UNCHANGED", ReparadorArquivos.method_cv2_unchanged),
            ("PIL padrão", ReparadorArquivos.method_pil_default),
            ("PIL → RGB", ReparadorArquivos.method_pil_rgb),
            ("PIL → RGBA → RGB", ReparadorArquivos.method_pil_rgba),
            ("Bytes brutos", ReparadorArquivos.method_raw_bytes),
            ("Sem perfil de cor", ReparadorArquivos.method_no_icc),
            ("Forçar grayscale", ReparadorArquivos.method_force_gray)
        ]
        
        for idx, (name, method) in enumerate(methods, 1):
            print(f"🔧 Método {idx}/8: {name}...")
            try:
                result = method(path)
                
                if result is not None and result.size > 0:
                    # Verifica se não é tudo preto
                    if np.mean(result) > 5:
                        print(f"✅ Sucesso com método: {name}")
                        return result, name
                        
            except Exception as e:
                print(f"   ❌ {name} falhou: {e}")
                continue
        
        return None, None
    
    @staticmethod
    def method_cv2_default(path):
        """Método 1: OpenCV padrão"""
        img = cv2.imread(path)
        if img is not None:
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return None
    
    @staticmethod
    def method_cv2_unchanged(path):
        """Método 2: OpenCV UNCHANGED"""
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            return None
        
        if len(img.shape) == 2:
            return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        elif img.shape[2] == 4:
            return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        else:
            return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    @staticmethod
    def method_pil_default(path):
        """Método 3: PIL padrão"""
        img = Image.open(path)
        return np.array(img.convert('RGB'))
    
    @staticmethod
    def method_pil_rgb(path):
        """Método 4: PIL → RGB forçado"""
        img = Image.open(path)
        img_rgb = img.convert('RGB')
        return np.array(img_rgb)
    
    @staticmethod
    def method_pil_rgba(path):
        """Método 5: PIL → RGBA → RGB"""
        img = Image.open(path)
        
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3] if len(img.split()) == 4 else None)
        
        return np.array(background)
    
    @staticmethod
    def method_raw_bytes(path):
        """Método 6: Lê bytes brutos"""
        with open(path, 'rb') as f:
            data = f.read()
        
        from io import BytesIO
        img = Image.open(BytesIO(data))
        return np.array(img.convert('RGB'))
    
    @staticmethod
    def method_no_icc(path):
        """Método 7: Ignora perfil ICC"""
        img = Image.open(path)
        
        if 'icc_profile' in img.info:
            img.info.pop('icc_profile')
        
        return np.array(img.convert('RGB'))
    
    @staticmethod
    def method_force_gray(path):
        """Método 8: Força escala de cinza"""
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        return None


class ProcessadorLineart:
    """Converte fotos em desenhos de colorir (line art)"""
    
    def __init__(self, img_rgb):
        self.img_original = img_rgb
        self.h, self.w = img_rgb.shape[:2]
        self.img_linhas = None
        self.img_resultado = None
    
    def processar(self, modo="balanced", canny_low=30, canny_high=100, 
                  blur_size=5, line_thickness=1, use_adaptive=True):
        """
        Converte foto em line art
        
        Parâmetros:
        - modo: "simple", "balanced", "detailed", "cartoon"
        - canny_low/high: thresholds do Canny
        - blur_size: tamanho do blur (ímpar)
        - line_thickness: espessura das linhas
        - use_adaptive: usar threshold adaptativo
        """
        print("\n" + "="*60)
        print("🎨 CONVERTENDO PARA DESENHO DE COLORIR")
        print("="*60)
        
        # 1. PRÉ-PROCESSAMENTO
        print("📋 Etapa 1: Pré-processamento...")
        
        # Converter para BGR (OpenCV trabalha em BGR)
        img_bgr = cv2.cvtColor(self.img_original, cv2.COLOR_RGB2BGR)
        
        # Equalizar histograma para melhorar contraste
        img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_equalizado = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        
        # Converter para grayscale
        gray = cv2.cvtColor(img_equalizado, cv2.COLOR_BGR2GRAY)
        
        # 2. SUAVIZAÇÃO (preserva bordas)
        print("🔄 Etapa 2: Suavização bilateral...")
        
        if blur_size < 3:
            blur_size = 3
        if blur_size % 2 == 0:
            blur_size += 1
        
        # Bilateral filter preserva bordas enquanto suaviza
        blurred = cv2.bilateralFilter(gray, blur_size, 75, 75)
        
        # 3. DETECÇÃO DE BORDAS CANNY
        print(f"✏️ Etapa 3: Detecção de bordas (modo: {modo})...")
        
        edges = cv2.Canny(blurred, canny_low, canny_high)
        
        # 4. MELHORAMENTO DAS LINHAS
        print("🎯 Etapa 4: Melhorando linhas...")
        
        # Dilatar para conectar linhas quebradas
        if line_thickness > 1:
            kernel = np.ones((line_thickness, line_thickness), np.uint8)
            edges = cv2.dilate(edges, kernel, iterations=1)
        
        # 5. THRESHOLD ADAPTATIVO (para áreas escuras)
        if use_adaptive:
            print("🔍 Etapa 5: Threshold adaptativo...")
            
            # Threshold adaptativo pega detalhes que o Canny perdeu
            adaptive = cv2.adaptiveThreshold(
                blurred, 255, 
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV, 11, 2
            )
            
            # Combinar com bordas Canny
            edges = cv2.bitwise_or(edges, adaptive)
        
        # 6. LIMPEZA MORFOLÓGICA
        print("🧹 Etapa 6: Limpeza de ruídos...")
        
        # Remover ruídos pequenos
        kernel_clean = np.ones((2, 2), np.uint8)
        edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel_clean)
        
        # Inverter: queremos linhas pretas em fundo branco
        edges_inv = cv2.bitwise_not(edges)
        
        # 7. CRIAR IMAGEM COM TRANSPARÊNCIA
        print("🖼️ Etapa 7: Criando transparência...")
        
        img_rgba = np.zeros((self.h, self.w, 4), dtype=np.uint8)
        img_rgba[:, :, 0] = 0  # R
        img_rgba[:, :, 1] = 0  # G
        img_rgba[:, :, 2] = 0  # B
        img_rgba[:, :, 3] = edges  # Alpha: onde tem borda fica opaco
        
        self.img_linhas = img_rgba
        self.img_resultado = edges_inv  # Para preview
        
        print("✅ Conversão completa!")
        print(f"   Dimensões: {self.w}x{self.h}px")
        
        return img_rgba, edges_inv
    
    def aplicar_modo(self, modo):
        """Aplica configurações pré-definidas por modo"""
        modos = {
            "simple": {
                "canny_low": 50,
                "canny_high": 150,
                "blur_size": 7,
                "line_thickness": 2,
                "use_adaptive": False
            },
            "balanced": {
                "canny_low": 30,
                "canny_high": 100,
                "blur_size": 5,
                "line_thickness": 1,
                "use_adaptive": True
            },
            "detailed": {
                "canny_low": 20,
                "canny_high": 80,
                "blur_size": 3,
                "line_thickness": 1,
                "use_adaptive": True
            },
            "cartoon": {
                "canny_low": 40,
                "canny_high": 120,
                "blur_size": 9,
                "line_thickness": 2,
                "use_adaptive": False
            }
        }
        
        return modos.get(modo, modos["balanced"])
    
    def salvar_png(self, caminho):
        """Salva como PNG com transparência"""
        if self.img_linhas is None:
            return False
        
        # Converter de BGRA para RGBA
        img_rgba = cv2.cvtColor(self.img_linhas, cv2.COLOR_BGRA2RGBA)
        cv2.imwrite(str(caminho), img_rgba)
        print(f"💾 Salvo em: {caminho}")
        return True


class Aplicacao:
    """Interface gráfica"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 Foto → Desenho de Colorir + Reparador")
        self.root.geometry("1600x900")
        self.root.configure(bg='white')
        
        self.img_original = None
        self.processador = None
        self.metodo_usado = None
        
        # Tamanho para redimensionamento
        self.resize_width = tk.IntVar(value=0)
        self.resize_height = tk.IntVar(value=0)
        self.maintain_aspect = tk.BooleanVar(value=True)
        
        self._criar_interface()
    
    def _criar_interface(self):
        # ========== HEADER SIMPLIFICADO ==========
        header = tk.Frame(self.root, bg='white', height=60)
        header.pack(fill=tk.X, side=tk.TOP)
        header.pack_propagate(False)
        
        tk.Label(
            header, 
            text="🎨 FOTO → DESENHO DE COLORIR", 
            font=('Arial', 20, 'bold'), 
            bg='white', 
            fg='#2c3e50'
        ).pack(side=tk.LEFT, padx=20, pady=10)
        
        tk.Button(
            header, 
            text="📂 CARREGAR FOTO", 
            command=self.carregar,
            font=('Arial', 12, 'bold'), 
            bg='#00ff88', 
            fg='black', 
            relief=tk.FLAT, 
            padx=30, 
            pady=10, 
            cursor='hand2'
        ).pack(side=tk.RIGHT, padx=20, pady=10)
        
        # ========== STATUS BAR (RODAPÉ) ==========
        self.status = tk.Label(
            self.root, 
            text="🟢 Pronto! Carregue uma foto para começar", 
            bg='#27ae60', 
            fg='white', 
            anchor=tk.W,
            font=('Arial', 10, 'bold'), 
            padx=15, 
            pady=6
        )
        self.status.pack(fill=tk.X, side=tk.BOTTOM)
        
        # ========== CONTAINER PRINCIPAL ==========
        container = tk.Frame(self.root, bg='white')
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ========== PAINEL ESQUERDO (CONTROLES) COM SCROLL ==========
        # Frame externo que vai conter o canvas + scrollbar
        painel_esquerdo_wrapper = tk.Frame(container, bg='#ecf0f1', width=400)
        painel_esquerdo_wrapper.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        painel_esquerdo_wrapper.pack_propagate(False)
        
        # Canvas para permitir scroll
        canvas_scroll = tk.Canvas(painel_esquerdo_wrapper, bg='#ecf0f1', highlightthickness=0)
        scrollbar = tk.Scrollbar(painel_esquerdo_wrapper, orient="vertical", command=canvas_scroll.yview)
        
        # Frame interno que vai dentro do canvas (este é scrollável)
        painel_esquerdo = tk.Frame(canvas_scroll, bg='#ecf0f1')
        
        # Criar uma "janela" no canvas contendo o frame
        canvas_scroll.create_window((0, 0), window=painel_esquerdo, anchor="nw")
        canvas_scroll.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar canvas e scrollbar
        canvas_scroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Atualizar a região de scroll quando o conteúdo mudar
        def on_frame_configure(event):
            canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
        
        painel_esquerdo.bind("<Configure>", on_frame_configure)
        
        # Permitir scroll com mousewheel
        def on_mousewheel(event):
            canvas_scroll.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas_scroll.bind_all("<MouseWheel>", on_mousewheel)
        
        # --- CONFIGURAÇÕES ---
        config_frame = tk.LabelFrame(
            painel_esquerdo, 
            text="⚙️ CONFIGURAÇÕES", 
            bg='#ecf0f1', 
            fg='#2c3e50',
            font=('Arial', 12, 'bold'),
            padx=10,
            pady=10
        )
        config_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Modo de conversão
        tk.Label(
            config_frame, 
            text="🎭 Modo:", 
            bg='#ecf0f1', 
            fg='#2c3e50',
            font=('Arial', 10, 'bold')
        ).grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.modo_var = tk.StringVar(value="balanced")
        modos = [
            ("Simples (menos linhas)", "simple"),
            ("Balanceado ⭐", "balanced"),
            ("Detalhado (mais linhas)", "detailed"),
            ("Cartoon (traços fortes)", "cartoon")
        ]
        
        for idx, (texto, valor) in enumerate(modos):
            tk.Radiobutton(
                config_frame,
                text=texto,
                variable=self.modo_var,
                value=valor,
                bg='#ecf0f1',
                fg='#34495e',
                selectcolor='white',
                font=('Arial', 9)
            ).grid(row=idx+1, column=0, sticky=tk.W, padx=20)
        
        # --- AJUSTE FINO ---
        ajuste_frame = tk.LabelFrame(
            config_frame,
            text="🎛️ Ajuste Fino",
            bg='#ecf0f1',
            fg='#34495e',
            font=('Arial', 9, 'bold')
        )
        ajuste_frame.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=10)
        
        # Threshold Canny Low
        tk.Label(
            ajuste_frame, 
            text="Sensibilidade Mínima:", 
            bg='#ecf0f1', 
            fg='#34495e',
            font=('Arial', 8)
        ).pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.slider_canny_low = Scale(
            ajuste_frame,
            from_=10,
            to=100,
            orient=tk.HORIZONTAL,
            bg='#ecf0f1',
            fg='#2c3e50',
            highlightthickness=0,
            troughcolor='#bdc3c7'
        )
        self.slider_canny_low.set(30)
        self.slider_canny_low.pack(fill=tk.X, padx=5)
        
        # Threshold Canny High
        tk.Label(
            ajuste_frame, 
            text="Sensibilidade Máxima:", 
            bg='#ecf0f1', 
            fg='#34495e',
            font=('Arial', 8)
        ).pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.slider_canny_high = Scale(
            ajuste_frame,
            from_=50,
            to=200,
            orient=tk.HORIZONTAL,
            bg='#ecf0f1',
            fg='#2c3e50',
            highlightthickness=0,
            troughcolor='#bdc3c7'
        )
        self.slider_canny_high.set(100)
        self.slider_canny_high.pack(fill=tk.X, padx=5)
        
        # Espessura da linha
        tk.Label(
            ajuste_frame, 
            text="Espessura das Linhas:", 
            bg='#ecf0f1', 
            fg='#34495e',
            font=('Arial', 8)
        ).pack(anchor=tk.W, padx=5, pady=(5,0))
        
        self.slider_thickness = Scale(
            ajuste_frame,
            from_=1,
            to=3,
            orient=tk.HORIZONTAL,
            bg='#ecf0f1',
            fg='#2c3e50',
            highlightthickness=0,
            troughcolor='#bdc3c7'
        )
        self.slider_thickness.set(1)
        self.slider_thickness.pack(fill=tk.X, padx=5)
        
        # Checkbox threshold adaptativo
        self.use_adaptive = tk.BooleanVar(value=True)
        tk.Checkbutton(
            ajuste_frame,
            text="Usar Threshold Adaptativo (recomendado)",
            variable=self.use_adaptive,
            bg='#ecf0f1',
            fg='#34495e',
            selectcolor='white',
            font=('Arial', 8)
        ).pack(anchor=tk.W, padx=5, pady=5)
        
        # --- REDIMENSIONAMENTO ---
        resize_frame = tk.LabelFrame(
            painel_esquerdo,
            text="📐 REDIMENSIONAR ANTES DE SALVAR",
            bg='#ecf0f1',
            fg='#2c3e50',
            font=('Arial', 12, 'bold'),
            padx=10,
            pady=10
        )
        resize_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Largura
        tk.Label(
            resize_frame,
            text="Largura (px):",
            bg='#ecf0f1',
            fg='#34495e',
            font=('Arial', 9)
        ).grid(row=0, column=0, sticky=tk.W, pady=3)
        
        self.entry_width = tk.Entry(
            resize_frame,
            textvariable=self.resize_width,
            width=10,
            font=('Arial', 10)
        )
        self.entry_width.grid(row=0, column=1, padx=5)
        self.entry_width.bind('<KeyRelease>', self.on_width_change)
        
        # Altura
        tk.Label(
            resize_frame,
            text="Altura (px):",
            bg='#ecf0f1',
            fg='#34495e',
            font=('Arial', 9)
        ).grid(row=1, column=0, sticky=tk.W, pady=3)
        
        self.entry_height = tk.Entry(
            resize_frame,
            textvariable=self.resize_height,
            width=10,
            font=('Arial', 10)
        )
        self.entry_height.grid(row=1, column=1, padx=5)
        self.entry_height.bind('<KeyRelease>', self.on_height_change)
        
        # Manter proporção
        tk.Checkbutton(
            resize_frame,
            text="🔗 Manter proporção",
            variable=self.maintain_aspect,
            bg='#ecf0f1',
            fg='#34495e',
            selectcolor='white',
            font=('Arial', 9, 'bold')
        ).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        tk.Label(
            resize_frame,
            text="💡 Deixe 0 para manter tamanho original",
            bg='#ecf0f1',
            fg='#7f8c8d',
            font=('Arial', 8, 'italic')
        ).grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=3)
        
        self.lbl_original_size = tk.Label(
            resize_frame,
            text="Original: -",
            bg='#ecf0f1',
            fg='#2980b9',
            font=('Arial', 8)
        )
        self.lbl_original_size.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=3)
        
        # --- BOTÕES DE AÇÃO ---
        btn_frame = tk.Frame(painel_esquerdo, bg='#ecf0f1')
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.btn_processar = tk.Button(
            btn_frame,
            text="✂️ CONVERTER AGORA",
            command=self.processar,
            font=('Arial', 12, 'bold'),
            bg='#9b59b6',
            fg='white',
            relief=tk.FLAT,
            padx=20,
            pady=15,
            cursor='hand2',
            state='disabled'
        )
        self.btn_processar.pack(fill=tk.X, pady=5)
        
        self.btn_salvar = tk.Button(
            btn_frame,
            text="💾 SALVAR PNG TRANSPARENTE",
            command=self.salvar,
            font=('Arial', 11, 'bold'),
            bg='#3498db',
            fg='white',
            relief=tk.FLAT,
            padx=20,
            pady=12,
            cursor='hand2',
            state='disabled'
        )
        self.btn_salvar.pack(fill=tk.X, pady=5)
        
        # --- INFO ---
        info_text = """
📋 COMO USAR:

1️⃣ Clique em "CARREGAR FOTO"
2️⃣ Escolha o modo de conversão
3️⃣ Ajuste configurações se desejar
4️⃣ Clique em "CONVERTER AGORA"
5️⃣ Defina tamanho (opcional)
6️⃣ Salve como PNG transparente

💡 DICAS:
• Modo "Balanceado" funciona bem
  para a maioria das fotos
• Fotos com muito detalhe: use
  "Detalhado"
• Para cartoon: use "Cartoon"
• O programa tenta 8 métodos
  diferentes para abrir arquivos
  problemáticos!
        """
        
        tk.Label(
            painel_esquerdo,
            text=info_text,
            bg='#ecf0f1',
            fg='#34495e',
            font=('Consolas', 8),
            justify=tk.LEFT
        ).pack(padx=15, pady=10)
        
        # ========== PAINEL DIREITO (PREVIEW) ==========
        painel_direito = tk.Frame(container, bg='white')
        painel_direito.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Canvas Original
        frame_orig = tk.LabelFrame(
            painel_direito,
            text="📷 FOTO ORIGINAL",
            bg='white',
            fg='#2980b9',
            font=('Arial', 11, 'bold'),
            padx=5,
            pady=5
        )
        frame_orig.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.canvas_orig = tk.Canvas(frame_orig, bg='#f8f9fa', highlightthickness=1, highlightbackground='#bdc3c7')
        self.canvas_orig.pack(fill=tk.BOTH, expand=True)
        
        # Canvas Resultado
        frame_result = tk.LabelFrame(
            painel_direito,
            text="✏️ DESENHO PARA COLORIR",
            bg='white',
            fg='#27ae60',
            font=('Arial', 11, 'bold'),
            padx=5,
            pady=5
        )
        frame_result.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.canvas_result = tk.Canvas(frame_result, bg='#f8f9fa', highlightthickness=1, highlightbackground='#bdc3c7')
        self.canvas_result.pack(fill=tk.BOTH, expand=True)
    
    def set_status(self, msg, color='#27ae60'):
        """Atualiza barra de status"""
        self.status.config(text=msg, bg=color)
        self.root.update()
    
    def carregar(self):
        """Carregar foto"""
        arquivo = filedialog.askopenfilename(
            title="Selecione a foto",
            filetypes=[
                ("Imagens", "*.png *.jpg *.jpeg *.bmp *.tif *.webp"),
                ("Todos", "*.*")
            ]
        )
        
        if not arquivo:
            return
        
        self.set_status("🔧 Tentando abrir arquivo...", '#f39c12')
        
        # Tentar abrir com os 8 métodos
        img_rgb, metodo = ReparadorArquivos.tentar_abrir(arquivo)
        
        if img_rgb is None:
            messagebox.showerror(
                "❌ Erro",
                "Não foi possível abrir o arquivo.\n\n"
                "Nenhum dos 8 métodos de reparo funcionou.\n\n"
                "Tente:\n"
                "1. Converter para outro formato\n"
                "2. Abrir no Photoshop e salvar novamente\n"
                "3. Tirar um screenshot"
            )
            self.set_status("❌ Falha ao abrir arquivo", '#da3633')
            return
        
        self.img_original = img_rgb
        self.metodo_usado = metodo
        
        # Mostrar no canvas
        self._mostrar_canvas(self.canvas_orig, img_rgb)
        
        # Atualizar info
        h, w = img_rgb.shape[:2]
        self.lbl_original_size.config(text=f"Original: {w}x{h}px")
        self.resize_width.set(w)
        self.resize_height.set(h)
        
        # Ativar botão
        self.btn_processar.config(state='normal')
        
        nome = Path(arquivo).name
        self.set_status(
            f"✅ Carregado: {nome} ({w}x{h}px) | Método: {metodo}",
            '#27ae60'
        )
    
    def processar(self):
        """Converter para desenho de colorir"""
        if self.img_original is None:
            return
        
        self.set_status("⏳ Convertendo para desenho de colorir...", '#f39c12')
        
        try:
            # Pegar configurações
            modo = self.modo_var.get()
            canny_low = self.slider_canny_low.get()
            canny_high = self.slider_canny_high.get()
            thickness = self.slider_thickness.get()
            use_adaptive = self.use_adaptive.get()
            
            # Processar
            self.processador = ProcessadorLineart(self.img_original)
            img_rgba, img_preview = self.processador.processar(
                modo=modo,
                canny_low=canny_low,
                canny_high=canny_high,
                line_thickness=thickness,
                use_adaptive=use_adaptive
            )
            
            # Gerar preview com fundo xadrez
            preview_com_xadrez = self._gerar_preview_transparente(img_rgba)
            
            # Mostrar resultado
            self._mostrar_canvas(self.canvas_result, preview_com_xadrez)
            
            self.btn_salvar.config(state='normal')
            
            self.set_status(
                "✅ Conversão completa! Pronto para salvar",
                '#27ae60'
            )
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar:\n{str(e)}")
            self.set_status("❌ Erro no processamento", '#da3633')
    
    def _gerar_preview_transparente(self, img_rgba):
        """Gera preview com fundo xadrez mostrando transparência"""
        h, w = img_rgba.shape[:2]
        
        # Criar fundo xadrez
        tamanho_quadrado = 20
        xadrez = np.zeros((h, w, 3), dtype=np.uint8)
        
        for i in range(0, h, tamanho_quadrado):
            for j in range(0, w, tamanho_quadrado):
                if ((i // tamanho_quadrado) + (j // tamanho_quadrado)) % 2 == 0:
                    xadrez[i:i+tamanho_quadrado, j:j+tamanho_quadrado] = [40, 40, 40]
                else:
                    xadrez[i:i+tamanho_quadrado, j:j+tamanho_quadrado] = [60, 60, 60]
        
        # Compor com alpha
        alpha = img_rgba[:, :, 3] / 255.0
        alpha = alpha[:, :, np.newaxis]
        
        linhas_rgb = img_rgba[:, :, :3]
        
        preview = (linhas_rgb * alpha + xadrez * (1 - alpha)).astype(np.uint8)
        
        return preview
    
    def _mostrar_canvas(self, canvas, img):
        """Mostrar imagem no canvas"""
        canvas.update_idletasks()
        
        canvas_w = max(canvas.winfo_width(), 100)
        canvas_h = max(canvas.winfo_height(), 100)
        
        h, w = img.shape[:2]
        
        scale = min(canvas_w / w, canvas_h / h, 1.0)
        novo_w = int(w * scale)
        novo_h = int(h * scale)
        
        img_resize = cv2.resize(img, (novo_w, novo_h), interpolation=cv2.INTER_AREA)
        
        # Converter para RGB se necessário
        if len(img_resize.shape) == 2:
            img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_GRAY2RGB)
        elif img_resize.shape[2] == 4:
            img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGRA2RGB)
        else:
            img_rgb = img_resize
        
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        
        canvas.delete("all")
        canvas.create_image(
            canvas_w // 2,
            canvas_h // 2,
            image=img_tk,
            anchor=tk.CENTER
        )
        canvas.image = img_tk
    
    def on_width_change(self, event=None):
        """Atualiza altura ao mudar largura (se manter proporção)"""
        if not self.maintain_aspect.get() or self.img_original is None:
            return
        
        try:
            new_width = self.resize_width.get()
            if new_width <= 0:
                return
            
            h, w = self.img_original.shape[:2]
            aspect = h / w
            new_height = int(new_width * aspect)
            self.resize_height.set(new_height)
        except:
            pass
    
    def on_height_change(self, event=None):
        """Atualiza largura ao mudar altura (se manter proporção)"""
        if not self.maintain_aspect.get() or self.img_original is None:
            return
        
        try:
            new_height = self.resize_height.get()
            if new_height <= 0:
                return
            
            h, w = self.img_original.shape[:2]
            aspect = w / h
            new_width = int(new_height * aspect)
            self.resize_width.set(new_width)
        except:
            pass
    
    def salvar(self):
        """Salvar PNG com transparência"""
        if self.processador is None or self.processador.img_linhas is None:
            return
        
        arquivo = filedialog.asksaveasfilename(
            title="Salvar desenho para colorir",
            defaultextension=".png",
            filetypes=[("PNG com transparência", "*.png")]
        )
        
        if not arquivo:
            return
        
        try:
            # Verificar se precisa redimensionar
            new_w = self.resize_width.get()
            new_h = self.resize_height.get()
            
            img_final = self.processador.img_linhas.copy()
            
            if new_w > 0 and new_h > 0:
                h_orig, w_orig = img_final.shape[:2]
                
                if new_w != w_orig or new_h != h_orig:
                    self.set_status(f"📐 Redimensionando para {new_w}x{new_h}px...", '#f39c12')
                    img_final = cv2.resize(
                        img_final, 
                        (new_w, new_h),
                        interpolation=cv2.INTER_AREA
                    )
            
            # Salvar
            self.set_status("💾 Salvando...", '#f39c12')
            
            # Converter BGRA para RGBA
            img_rgba = cv2.cvtColor(img_final, cv2.COLOR_BGRA2RGBA)
            cv2.imwrite(arquivo, img_rgba)
            
            h, w = img_final.shape[:2]
            
            messagebox.showinfo(
                "✅ Sucesso!",
                f"Desenho para colorir salvo!\n\n"
                f"📁 {arquivo}\n\n"
                f"📐 Dimensões: {w}x{h}px\n"
                f"✅ Fundo transparente\n"
                f"✅ Linhas pretas preservadas\n\n"
                f"💡 Use em programas de pintura digital\n"
                f"   ou imprima para colorir!"
            )
            
            self.set_status("✅ Arquivo salvo com sucesso!", '#27ae60')
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar:\n{str(e)}")
            self.set_status("❌ Erro ao salvar", '#da3633')


def main():
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()


if __name__ == "__main__":
    main()
