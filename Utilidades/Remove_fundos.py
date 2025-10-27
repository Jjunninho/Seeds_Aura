#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extrator de Linhas v1.0
Remove o fundo colorido e mantém apenas as linhas pretas
"""

import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from pathlib import Path


class ExtratorLinhas:
    """Remove fundo e mantém apenas as linhas"""
    
    def __init__(self, img):
        self.img_original = img
        self.h, self.w = img.shape[:2]
        self.img_linhas = None
        
    def extrair_linhas(self, threshold=127):
        """
        Remove o fundo colorido e mantém apenas as linhas pretas
        
        Retorna:
        - Imagem com fundo transparente (PNG) ou branco
        """
        print("\n" + "="*60)
        print("✂️ REMOVENDO FUNDO")
        print("="*60)
        
        # 1. Converter para escala de cinza
        gray = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2GRAY)
        print("✓ Convertido para escala de cinza")
        
        # 2. Binarização - tudo que for escuro vira preto, resto vira branco
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        print(f"✓ Binarização com threshold: {threshold}")
        
        # 3. Inverter: linhas pretas em fundo branco
        # (já está correto assim)
        
        # 4. Criar imagem com canal alpha (transparente)
        # Criar imagem RGBA (com transparência)
        img_rgba = np.zeros((self.h, self.w, 4), dtype=np.uint8)
        
        # Onde for branco (fundo) = transparente
        # Onde for preto (linha) = preto opaco
        img_rgba[:, :, 0] = 0      # R = 0
        img_rgba[:, :, 1] = 0      # G = 0
        img_rgba[:, :, 2] = 0      # B = 0
        img_rgba[:, :, 3] = 255 - binary  # Alpha: branco vira 0 (transparente), preto vira 255 (opaco)
        
        self.img_linhas = img_rgba
        
        print("✅ Fundo removido! Linhas extraídas.")
        print(f"   Dimensões: {self.w}x{self.h}px")
        
        return img_rgba
    
    def salvar_png(self, caminho):
        """Salva como PNG com transparência"""
        if self.img_linhas is None:
            return False
        
        # Converter de BGRA para RGBA para o OpenCV
        img_rgba = cv2.cvtColor(self.img_linhas, cv2.COLOR_BGRA2RGBA)
        cv2.imwrite(str(caminho), img_rgba)
        print(f"✓ Salvo em: {caminho}")
        return True
    
    def gerar_preview(self):
        """Gera preview com fundo xadrez (mostra transparência)"""
        if self.img_linhas is None:
            return None
        
        # Criar fundo xadrez
        tamanho_quadrado = 20
        xadrez = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        
        for i in range(0, self.h, tamanho_quadrado):
            for j in range(0, self.w, tamanho_quadrado):
                if ((i // tamanho_quadrado) + (j // tamanho_quadrado)) % 2 == 0:
                    xadrez[i:i+tamanho_quadrado, j:j+tamanho_quadrado] = [200, 200, 200]
                else:
                    xadrez[i:i+tamanho_quadrado, j:j+tamanho_quadrado] = [255, 255, 255]
        
        # Compor imagem com alpha
        alpha = self.img_linhas[:, :, 3] / 255.0
        alpha = alpha[:, :, np.newaxis]
        
        # Pegar RGB das linhas
        linhas_rgb = self.img_linhas[:, :, :3]
        
        # Blend
        preview = (linhas_rgb * alpha + xadrez * (1 - alpha)).astype(np.uint8)
        
        return preview


class Aplicacao:
    """Interface gráfica"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("✂️ Extrator de Linhas - Remove Fundo")
        self.root.geometry("1400x800")
        
        self.img_original = None
        self.extrator = None
        
        self._criar_interface()
    
    def _criar_interface(self):
        # Frame principal
        main = ttk.Frame(self.root, padding="10")
        main.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(2, weight=1)
        
        # CONTROLES
        ctrl = ttk.LabelFrame(main, text="⚙️ Controles", padding="10")
        ctrl.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Botão carregar
        ttk.Button(
            ctrl,
            text="📁 Carregar Imagem",
            command=self.carregar
        ).grid(row=0, column=0, padx=5, pady=5)
        
        self.lbl_arquivo = ttk.Label(ctrl, text="Nenhuma imagem carregada")
        self.lbl_arquivo.grid(row=0, column=1, padx=5)
        
        # Slider de threshold
        ttk.Label(ctrl, text="Sensibilidade (threshold):").grid(row=1, column=0, sticky=tk.E, padx=5)
        self.slider_threshold = tk.Scale(
            ctrl, 
            from_=0, 
            to=255, 
            orient=tk.HORIZONTAL, 
            length=300,
            command=self.atualizar_preview
        )
        self.slider_threshold.set(127)
        self.slider_threshold.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(
            ctrl, 
            text="← Mais linhas | Menos linhas →",
            foreground="gray"
        ).grid(row=2, column=1, sticky=tk.W, padx=5)
        
        # Botões de ação
        btns = ttk.Frame(ctrl)
        btns.grid(row=1, column=2, rowspan=2, padx=20)
        
        self.btn_extrair = ttk.Button(
            btns,
            text="✂️ REMOVER FUNDO",
            command=self.extrair,
            state="disabled"
        )
        self.btn_extrair.pack(pady=5)
        
        self.btn_salvar = ttk.Button(
            btns,
            text="💾 Salvar PNG",
            command=self.salvar,
            state="disabled"
        )
        self.btn_salvar.pack(pady=5)
        
        # Status
        self.lbl_status = ttk.Label(
            ctrl,
            text="👆 Carregue uma imagem para começar",
            foreground="blue",
            font=('Arial', 10, 'bold')
        )
        self.lbl_status.grid(row=3, column=0, columnspan=3, pady=10)
        
        # CANVAS
        # Original
        frame_orig = ttk.LabelFrame(main, text="📷 Imagem Original", padding="5")
        frame_orig.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.canvas_orig = tk.Canvas(frame_orig, bg="gray80", width=680, height=600)
        self.canvas_orig.pack(fill=tk.BOTH, expand=True)
        
        # Resultado
        frame_result = ttk.LabelFrame(main, text="✂️ Linhas Extraídas (fundo transparente)", padding="5")
        frame_result.grid(row=2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)
        
        self.canvas_result = tk.Canvas(frame_result, bg="gray80", width=680, height=600)
        self.canvas_result.pack(fill=tk.BOTH, expand=True)
    
    def carregar(self):
        """Carregar imagem"""
        arquivo = filedialog.askopenfilename(
            title="Selecione a imagem da malha",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp"), ("Todos", "*.*")]
        )
        
        if not arquivo:
            return
        
        self.img_original = cv2.imread(arquivo)
        
        if self.img_original is None:
            messagebox.showerror("Erro", "Não foi possível carregar a imagem")
            return
        
        # Mostrar
        self._mostrar(self.canvas_orig, self.img_original)
        
        h, w = self.img_original.shape[:2]
        self.lbl_arquivo.config(text=f"✅ {Path(arquivo).name} ({w}x{h}px)")
        self.btn_extrair.config(state="normal")
        self.lbl_status.config(text="✨ Ajuste o threshold e clique em 'REMOVER FUNDO'")
        
        # Criar extrator
        self.extrator = ExtratorLinhas(self.img_original)
    
    def atualizar_preview(self, valor=None):
        """Atualiza preview ao mover o slider"""
        if self.extrator is None:
            return
        
        # Não atualizar automaticamente, apenas ao clicar no botão
        pass
    
    def extrair(self):
        """Extrair linhas"""
        if self.img_original is None:
            return
        
        threshold = self.slider_threshold.get()
        
        self.lbl_status.config(text="⏳ Removendo fundo...", foreground="orange")
        self.root.update()
        
        try:
            # Extrair
            if self.extrator is None:
                self.extrator = ExtratorLinhas(self.img_original)
            
            img_linhas = self.extrator.extrair_linhas(threshold=threshold)
            
            # Gerar preview com fundo xadrez
            preview = self.extrator.gerar_preview()
            self._mostrar(self.canvas_result, preview)
            
            self.lbl_status.config(
                text="✅ Fundo removido! Linhas extraídas com transparência",
                foreground="green"
            )
            
            self.btn_salvar.config(state="normal")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao extrair:\n{str(e)}")
            self.lbl_status.config(text="❌ Erro", foreground="red")
    
    def _mostrar(self, canvas, img):
        """Mostrar imagem no canvas"""
        h, w = img.shape[:2]
        
        canvas_w = 670
        canvas_h = 590
        
        scale = min(canvas_w / w, canvas_h / h)
        novo_w = int(w * scale)
        novo_h = int(h * scale)
        
        img_resize = cv2.resize(img, (novo_w, novo_h))
        
        # Se for BGR, converter para RGB
        if len(img_resize.shape) == 3 and img_resize.shape[2] == 3:
            img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
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
    
    def salvar(self):
        """Salvar PNG com transparência"""
        if self.extrator is None or self.extrator.img_linhas is None:
            return
        
        arquivo = filedialog.asksaveasfilename(
            title="Salvar imagem",
            defaultextension=".png",
            filetypes=[("PNG com transparência", "*.png")]
        )
        
        if not arquivo:
            return
        
        try:
            self.extrator.salvar_png(arquivo)
            
            messagebox.showinfo(
                "Sucesso!",
                f"Imagem salva com sucesso!\n\n"
                f"📁 {arquivo}\n\n"
                f"✓ Fundo transparente\n"
                f"✓ Linhas pretas preservadas\n"
                f"✓ Mesmas dimensões da original"
            )
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar:\n{str(e)}")


def main():
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()


if __name__ == "__main__":
    main()