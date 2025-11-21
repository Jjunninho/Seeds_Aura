import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# ==================================================
# CLASSES DE PROCESSAMENTO (Lógica Original Mantida)
# ==================================================

class ProcessadorLineart:
    """Converte fotos em desenhos de colorir (line art)"""
    
    def __init__(self, img_rgb):
        self.img_original = img_rgb
        self.h, self.w = img_rgb.shape[:2]
        self.img_linhas = None
    
    def processar(self, canny_low=30, canny_high=100, 
                  blur_size=5, line_thickness=1, use_adaptive=True):
        
        # 1. PRÉ-PROCESSAMENTO
        # Converter para BGR (OpenCV trabalha em BGR)
        img_bgr = cv2.cvtColor(self.img_original, cv2.COLOR_RGB2BGR)
        
        # Equalizar histograma
        img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_equalizado = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        
        # Converter para grayscale
        gray = cv2.cvtColor(img_equalizado, cv2.COLOR_BGR2GRAY)
        
        # 2. SUAVIZAÇÃO
        if blur_size < 3: blur_size = 3
        if blur_size % 2 == 0: blur_size += 1
        blurred = cv2.bilateralFilter(gray, blur_size, 75, 75)
        
        # 3. DETECÇÃO DE BORDAS
        edges = cv2.Canny(blurred, canny_low, canny_high)
        
        # 4. MELHORAMENTO DAS LINHAS
        if line_thickness > 1:
            kernel = np.ones((line_thickness, line_thickness), np.uint8)
            edges = cv2.dilate(edges, kernel, iterations=1)
        
        # 5. THRESHOLD ADAPTATIVO
        if use_adaptive:
            adaptive = cv2.adaptiveThreshold(
                blurred, 255, 
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV, 11, 2
            )
            edges = cv2.bitwise_or(edges, adaptive)
        
        # 6. LIMPEZA E TRANSPARÊNCIA
        # Inverter (linhas pretas)
        edges_inv = cv2.bitwise_not(edges)
        
        # Criar canal Alpha
        img_rgba = np.zeros((self.h, self.w, 4), dtype=np.uint8)
        img_rgba[:, :, 0] = 0  # R (Preto)
        img_rgba[:, :, 1] = 0  # G (Preto)
        img_rgba[:, :, 2] = 0  # B (Preto)
        img_rgba[:, :, 3] = edges # Alpha baseado nas bordas
        
        self.img_linhas = img_rgba
        return img_rgba

# ==================================================
# INTERFACE STREAMLIT
# ==================================================

st.set_page_config(page_title="Seeds Aura - Colorir", page_icon="🎨", layout="wide")

# Título e Header
st.title("🎨 Seeds Aura: Foto → Desenho de Colorir")
st.markdown("""
Transforme suas fotos em **Line Art** com fundo transparente num piscar de olhos.
Ideal para livros de colorir, atividades educativas e arte digital.
""")

# --- SIDEBAR DE CONFIGURAÇÕES ---
st.sidebar.header("⚙️ Configurações")

# Seleção de Modo (Presets)
modo = st.sidebar.selectbox(
    "🎭 Escolha o Modo",
    ("Balanceado (Recomendado)", "Simples (Limpo)", "Detalhado (Complexo)", "Cartoon (Traços Fortes)"),
    index=0
)

# Definição dos valores baseados no modo
if "Simples" in modo:
    def_low, def_high, def_blur, def_thick, def_adapt = 50, 150, 7, 2, False
elif "Detalhado" in modo:
    def_low, def_high, def_blur, def_thick, def_adapt = 20, 80, 3, 1, True
elif "Cartoon" in modo:
    def_low, def_high, def_blur, def_thick, def_adapt = 40, 120, 9, 2, False
else: # Balanceado
    def_low, def_high, def_blur, def_thick, def_adapt = 30, 100, 5, 1, True

# Ajuste Fino (Expander)
with st.sidebar.expander("🎛️ Ajuste Fino (Avançado)", expanded=True):
    canny_low = st.slider("Sensibilidade Mínima", 10, 100, def_low, help="Valores menores detectam mais detalhes sutis")
    canny_high = st.slider("Sensibilidade Máxima", 50, 200, def_high, help="Controla a intensidade das bordas principais")
    thickness = st.slider("Espessura da Linha", 1, 3, def_thick)
    blur_size = st.slider("Suavização (Blur)", 3, 15, def_blur, step=2)
    use_adaptive = st.checkbox("Threshold Adaptativo", value=def_adapt, help="Melhora detecção em fotos escuras ou com sombras")

# --- ÁREA PRINCIPAL ---
arquivo = st.file_uploader("📂 Carregue sua foto aqui", type=["jpg", "jpeg", "png", "bmp", "webp"])

if arquivo:
    # Carregar imagem
    image = Image.open(arquivo)
    img_array = np.array(image.convert('RGB'))
    
    # Layout de colunas para Antes/Depois
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📸 Original")
        st.image(image, use_column_width=True)
    
    # Processamento
    with st.spinner('Desenhando...'):
        processador = ProcessadorLineart(img_array)
        img_resultado = processador.processar(
            canny_low=canny_low,
            canny_high=canny_high,
            blur_size=blur_size,
            line_thickness=thickness,
            use_adaptive=use_adaptive
        )
        
        # Converter resultado para mostrar no Streamlit
        # O Streamlit exibe numpy arrays diretamente, mas para download precisamos converter
        img_pil = Image.fromarray(img_resultado)
        
        with col2:
            st.subheader("✏️ Desenho")
            # Mostramos com um fundo branco por trás para visualizar melhor na tela
            # (Mas o download será transparente)
            bg = Image.new("RGB", img_pil.size, (255, 255, 255))
            bg.paste(img_pil, mask=img_pil.split()[3])
            st.image(bg, use_column_width=True)
            
    # --- ÁREA DE DOWNLOAD ---
    st.markdown("---")
    st.subheader("💾 Baixar Resultado")
    
    # Preparar buffer para download
    buf = io.BytesIO()
    img_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    col_dl1, col_dl2 = st.columns([1, 2])
    with col_dl1:
        btn = st.download_button(
            label="📥 Download PNG Transparente",
            data=byte_im,
            file_name=f"seeds_aura_desenho.png",
            mime="image/png",
            use_container_width=True
        )
    
    st.success(f"Imagem processada com sucesso! Dimensões: {img_array.shape[1]}x{img_array.shape[0]}px")

else:
    # Estado vazio (Instructions)
    st.info("👆 Comece enviando uma imagem no botão acima!")
    st.markdown("---")
    st.markdown("### Exemplos de uso:")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown("✅ **Retratos:** Use o modo *Balanceado*")
    with c2: st.markdown("✅ **Paisagens:** Use o modo *Detalhado*")
    with c3: st.markdown("✅ **Objetos:** Use o modo *Simples*")
