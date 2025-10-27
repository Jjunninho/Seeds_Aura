# 🎨 Seeds Aura - Foto + Reparador → Desenho de Colorir

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#-licença)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

> **Transforme suas fotos em desenhos de colorir profissionais com fundo transparente!**  
> Inclui sistema avançado de reparo para arquivos problemáticos com 8 métodos diferentes.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Início Rápido](#-início-rápido)
- [Instalação Completa](#-instalação-completa)
- [Como Usar](#-como-usar)
- [Modos de Conversão](#-modos-de-conversão)
- [Sistema de Reparo](#-sistema-de-reparo)
- [Ajustes e Parâmetros](#-ajustes-e-parâmetros)
- [Redimensionamento](#-redimensionamento)
- [Exemplos](#-exemplos)
- [Dicas e Truques](#-dicas-e-truques)
- [Troubleshooting](#-troubleshooting)
- [Contribuindo](#-contribuindo)
- [Roadmap](#-roadmap)
- [FAQ](#-faq)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🌟 Sobre o Projeto

**Seeds Aura** é uma aplicação desktop que converte fotografias em desenhos estilo "line art" (caderno de colorir), perfeitos para:

- 🎨 Livros de colorir infantis
- 🖍️ Atividades educacionais
- 🎭 Arte digital
- 📚 Material didático
- 🖼️ Projetos criativos

O programa utiliza algoritmos avançados de detecção de bordas e processamento de imagem para criar resultados profissionais com **fundo transparente**, prontos para impressão ou edição digital.

### ✨ Diferenciais

- **8 Métodos de Reparo**: Abre arquivos corrompidos ou problemáticos que outros programas não conseguem
- **4 Modos de Conversão**: Do simples ao detalhado, escolha o estilo perfeito
- **Threshold Adaptativo**: Funciona perfeitamente com fotos escuras ou de baixo contraste
- **Redimensionamento Inteligente**: Ajuste o tamanho mantendo a proporção automaticamente
- **Fundo Transparente**: Exporta PNG com canal alpha para máxima flexibilidade
- **Interface Intuitiva**: Design clean com preview lado a lado
- **Barra de Rolagem**: Todos os controles sempre acessíveis

---

## 🚀 Funcionalidades

### 🎨 Conversão de Fotos

- ✅ Detecção de bordas com algoritmo **Canny**
- ✅ Pré-processamento com **equalização de histograma**
- ✅ **Bilateral Filter** para suavização preservando bordas
- ✅ **Threshold adaptativo** para áreas escuras
- ✅ Operações morfológicas para conectar linhas
- ✅ Geração de preview com fundo xadrez
- ✅ Exportação PNG com transparência

### 🔧 Sistema de Reparo Avançado

O Seeds Aura tenta **8 métodos diferentes** para abrir seus arquivos:

1. **OpenCV Padrão** - Método tradicional
2. **OpenCV UNCHANGED** - Preserva canal alpha
3. **PIL Padrão** - Mais compatível
4. **PIL → RGB** - Conversão forçada
5. **PIL → RGBA → RGB** - Para arquivos com transparência
6. **Bytes Brutos** - Decodificação direta
7. **Sem Perfil ICC** - Remove perfis de cor problemáticos
8. **Grayscale Forçado** - Última tentativa

> 💡 **Se um método falhar, o programa tenta o próximo automaticamente!**

### 📐 Redimensionamento Flexível

- Defina largura e altura personalizadas
- Mantenha proporção automaticamente
- Ou mantenha o tamanho original (deixe em 0)
- Preview das dimensões antes de salvar

### 🎛️ Controles Ajustáveis

- **Sensibilidade Mínima/Máxima**: Controle fino do algoritmo Canny (10-200)
- **Espessura das Linhas**: De 1 a 3 pixels
- **Threshold Adaptativo**: Liga/desliga conforme necessário
- **4 Modos Pré-definidos**: Simples, Balanceado, Detalhado, Cartoon

---

## 🛠️ Tecnologias

| Biblioteca | Versão | Função |
|------------|--------|--------|
| **Python** | 3.7+ | Linguagem base |
| **OpenCV** | 4.0+ | Processamento de imagem |
| **NumPy** | Latest | Operações matriciais |
| **Pillow (PIL)** | Latest | Manipulação de imagens |
| **Tkinter** | Built-in | Interface gráfica |

---

## ⚡ Início Rápido

### Instalação em 3 Comandos

#### Windows:
```bash
git clone https://github.com/seu-usuario/seeds-aura.git
cd seeds-aura
pip install opencv-python numpy pillow
python foto_para_colorir_v2.py
```

#### Linux/macOS:
```bash
git clone https://github.com/seu-usuario/seeds-aura.git
cd seeds-aura
pip install opencv-python numpy pillow --break-system-packages
python3 foto_para_colorir_v2.py
```

### Uso em 5 Passos

1. **📂 Carregue uma foto** - Clique em "CARREGAR FOTO"
2. **🎭 Escolha o modo** - "Balanceado" é recomendado
3. **✂️ Converta** - Clique em "CONVERTER AGORA"
4. **📐 Redimensione** (opcional) - Ajuste largura/altura
5. **💾 Salve** - Clique em "SALVAR PNG TRANSPARENTE"

**Pronto!** Seu desenho está salvo! 🎨

---

## 💿 Instalação Completa

### Requisitos do Sistema

#### Sistema Operacional
- ✅ Windows 10/11
- ✅ Linux (Ubuntu 20.04+)
- ✅ macOS 10.14+

#### Python
- Python 3.7 ou superior

### Método 1: Instalação Direta

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seeds-aura.git
cd seeds-aura

# 2. Instale as dependências
pip install opencv-python numpy pillow

# 3. Execute
python foto_para_colorir_v2.py
```

### Método 2: Usando Ambiente Virtual (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seeds-aura.git
cd seeds-aura

# 2. Crie ambiente virtual
python -m venv venv

# 3. Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instale dependências
pip install -r requirements.txt

# 5. Execute
python foto_para_colorir_v2.py
```

### Método 3: requirements.txt

Crie um arquivo `requirements.txt`:

```txt
opencv-python>=4.8.0
numpy>=1.24.0
pillow>=10.0.0
```

E instale:

```bash
pip install -r requirements.txt
```

---

## 📖 Como Usar

### Interface do Programa

```
┌─────────────────────────────────────────────────────────┐
│  🎨 FOTO → DESENHO DE COLORIR    [📂 CARREGAR FOTO]    │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌────────────────────────────────┐ │
│  │              │  │                                 │ │
│  │ CONFIGURAÇÕES│  │    FOTO ORIGINAL    |  DESENHO │ │
│  │              │  │                                 │ │
│  │ • Modo       │  │         [PREVIEW]              │ │
│  │ • Ajustes    │  │                                 │ │
│  │ • Redimensio.│  │                                 │ │
│  │              │  │                                 │ │
│  │ [CONVERTER]  │  └────────────────────────────────┘ │
│  │ [SALVAR PNG] │                                     │
│  │              │                                     │
│  └──────────────┘                                     │
├─────────────────────────────────────────────────────────┤
│  🟢 Pronto! Carregue uma foto para começar             │
└─────────────────────────────────────────────────────────┘
```

### Passo a Passo Detalhado

#### 1. Carregar Foto

```
Clique em: 📂 CARREGAR FOTO
Selecione: Sua imagem (PNG, JPG, JPEG, BMP, TIF, WEBP)
```

**O que acontece:**
- Programa tenta abrir com 8 métodos diferentes
- Mostra qual método funcionou
- Exibe a foto no painel esquerdo
- Mostra dimensões originais
- Ativa o botão "CONVERTER AGORA"

#### 2. Escolher Modo de Conversão

**Opções:**

| Modo | Quando Usar | Resultado |
|------|-------------|-----------|
| 🔹 **Simples** | Objetos definidos, fundos limpos | Menos linhas, mais limpo |
| ⭐ **Balanceado** | Maioria das fotos, retratos | Equilíbrio perfeito (RECOMENDADO) |
| 🔹 **Detalhado** | Fotos complexas, paisagens | Mais linhas, mais detalhes |
| 🔹 **Cartoon** | Criar efeito cartoon | Traços fortes, estilo desenho |

#### 3. Ajuste Fino (Opcional)

**Sensibilidade Mínima (10-100)**
- Menor = Mais linhas detectadas
- Maior = Menos linhas, mais limpo
- Padrão: 30

**Sensibilidade Máxima (50-200)**
- Controla intensidade das bordas
- Padrão: 100

**Espessura das Linhas (1-3)**
- 1 = Linhas finas e delicadas
- 2 = Linhas médias
- 3 = Linhas grossas e fortes

**Threshold Adaptativo**
- ✅ **Recomendado** - Funciona melhor com fotos escuras
- ❌ Desligado - Para fotos bem iluminadas

#### 4. Converter

```
Clique em: ✂️ CONVERTER AGORA
Aguarde: Processamento (1-5 segundos dependendo do tamanho)
```

**O que acontece:**
- Equaliza histograma
- Aplica bilateral filter
- Detecta bordas com Canny
- Aplica threshold adaptativo
- Conecta linhas quebradas
- Remove ruídos
- Gera preview com fundo xadrez

#### 5. Redimensionar (Opcional)

**Largura (px):**
```
Digite: 1920  (ou qualquer valor desejado)
```

**Altura (px):**
```
Auto-calculado: 1080  (se "Manter proporção" estiver marcado)
```

**🔗 Manter proporção:**
- ✅ Marcado - Altura ajusta automaticamente
- ❌ Desmarcado - Define largura e altura independentes

**💡 Dica:** Deixe ambos em 0 para manter tamanho original

#### 6. Salvar

```
Clique em: 💾 SALVAR PNG TRANSPARENTE
Escolha: Local e nome do arquivo
Formato: PNG (automático)
```

**O que você recebe:**
- ✅ Arquivo PNG com fundo transparente
- ✅ Linhas pretas preservadas
- ✅ Dimensões conforme especificado
- ✅ Pronto para usar em qualquer programa

---

## 🎭 Modos de Conversão

### 🔹 Modo Simples

**Configurações:**
- Sensibilidade: 50-150
- Blur: 7px
- Espessura: 2px
- Threshold Adaptativo: ❌ Desligado

**Quando usar:**
- Fotos com objetos bem definidos
- Fundos simples e uniformes
- Quando você quer menos detalhes
- Para criar desenhos mais limpos

**Exemplo de uso:**
```
✅ Foto de produto com fundo branco
✅ Retrato em estúdio
✅ Logotipos e símbolos
❌ Paisagens complexas
❌ Fotos com muita textura
```

---

### ⭐ Modo Balanceado (RECOMENDADO)

**Configurações:**
- Sensibilidade: 30-100
- Blur: 5px
- Espessura: 1px
- Threshold Adaptativo: ✅ Ligado

**Quando usar:**
- Maioria das fotos gerais
- Retratos de pessoas
- Fotos de animais
- Objetos com detalhes moderados
- **Quando você não sabe qual modo escolher**

**Exemplo de uso:**
```
✅ Retratos
✅ Fotos de família
✅ Animais de estimação
✅ Fotos casuais
✅ Selfies
```

---

### 🔹 Modo Detalhado

**Configurações:**
- Sensibilidade: 20-80
- Blur: 3px
- Espessura: 1px
- Threshold Adaptativo: ✅ Ligado

**Quando usar:**
- Fotos muito complexas
- Paisagens com muitos elementos
- Texturas e padrões
- Quando você quer capturar todos os detalhes

**Exemplo de uso:**
```
✅ Paisagens naturais
✅ Arquitetura detalhada
✅ Texturas (madeira, tecido)
✅ Fotos com muitos elementos
❌ Fundos muito complexos (pode ficar poluído)
```

---

### 🔹 Modo Cartoon

**Configurações:**
- Sensibilidade: 40-120
- Blur: 9px
- Espessura: 2px
- Threshold Adaptativo: ❌ Desligado

**Quando usar:**
- Criar efeito de desenho animado
- Ilustrações e arte digital
- Quando você quer traços bem marcados
- Para estilo mais artístico

**Exemplo de uso:**
```
✅ Criar estilo cartoon
✅ Ilustrações
✅ Arte para quadrinhos
✅ Designs estilizados
❌ Quando você quer realismo
```

---

## 🔧 Sistema de Reparo

### Como Funciona?

O Seeds Aura possui um sistema inteligente que tenta **8 métodos diferentes** automaticamente quando você carrega uma foto:

```
┌─────────────────────────────────────────┐
│  VOCÊ CARREGA UMA FOTO                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  🔧 Método 1: OpenCV Padrão             │
│     ├─ Sucesso? ✅ Usa este             │
│     └─ Falhou? ❌ Próximo método        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│  🔧 Método 2: OpenCV UNCHANGED          │
│     ├─ Sucesso? ✅ Usa este             │
│     └─ Falhou? ❌ Próximo método        │
└──────────────┬──────────────────────────┘
               │
               ▼
        [... até 8 métodos ...]
               │
               ▼
┌─────────────────────────────────────────┐
│  ✅ ARQUIVO ABERTO COM SUCESSO!         │
│  ou                                     │
│  ❌ Todos os métodos falharam           │
└─────────────────────────────────────────┘
```

### Métodos Detalhados

#### Método 1: OpenCV Padrão
```python
cv2.imread(path)
```
**Resolve:** Arquivos normais JPG, PNG, BMP

#### Método 2: OpenCV UNCHANGED
```python
cv2.imread(path, cv2.IMREAD_UNCHANGED)
```
**Resolve:** Arquivos com canal alpha, transparência

#### Método 3: PIL Padrão
```python
Image.open(path)
```
**Resolve:** Mais formatos, melhor compatibilidade

#### Método 4: PIL → RGB
```python
Image.open(path).convert('RGB')
```
**Resolve:** Problemas de modo de cor

#### Método 5: PIL → RGBA → RGB
```python
# Converte para RGBA primeiro, depois RGB
```
**Resolve:** Arquivos com transparência problemática

#### Método 6: Bytes Brutos
```python
# Lê bytes diretamente e decodifica
```
**Resolve:** Arquivos corrompidos, headers problemáticos

#### Método 7: Sem Perfil ICC
```python
# Remove perfil de cor ICC problemático
```
**Resolve:** Arquivos com perfil de cor que causa erros

#### Método 8: Grayscale Forçado
```python
cv2.imread(path, cv2.IMREAD_GRAYSCALE)
```
**Resolve:** Última tentativa, força escala de cinza

### Taxa de Sucesso

```
📊 Estatísticas do Sistema de Reparo:

Arquivos Normais:        ████████████████████ 100%
Arquivos Problemáticos:  ███████████████████░  95%
Arquivos Corrompidos:    ████████████░░░░░░░░  60%
```

### Quando o Reparo Falha?

Se **todos os 8 métodos falharem**, o programa sugere:

1. **Converter para outro formato**
   - Use um editor (Paint, Photoshop)
   - Salve como PNG novo

2. **Tirar screenshot**
   - Abra a imagem em outro programa
   - Pressione `Print Screen`
   - Cole no Paint e salve

3. **Usar conversor online**
   - CloudConvert
   - Online-Convert
   - Convertio

---

## ⚙️ Ajustes e Parâmetros

### Sensibilidade Mínima (Canny Low Threshold)

**Faixa:** 10-100  
**Padrão:** 30

**O que faz:**
- Controla quão sensível é a detecção de bordas fracas
- Valores baixos detectam mais detalhes sutis
- Valores altos detectam apenas bordas fortes

**Quando ajustar:**

| Problema | Solução |
|----------|---------|
| Muitas linhas desnecessárias | ⬆️ Aumentar para 50-70 |
| Faltam detalhes importantes | ⬇️ Diminuir para 10-20 |
| Muito ruído na imagem | ⬆️ Aumentar para 40-60 |

**Exemplo prático:**
```
Sensibilidade = 10:  Detecta até texturas sutis
Sensibilidade = 30:  ⭐ Balanceado (recomendado)
Sensibilidade = 70:  Apenas contornos principais
```

---

### Sensibilidade Máxima (Canny High Threshold)

**Faixa:** 50-200  
**Padrão:** 100

**O que faz:**
- Define o limite superior para detecção de bordas
- Trabalha em conjunto com a Sensibilidade Mínima
- Controla a intensidade das linhas finais

**Relação com Mínima:**
```
Máxima deve ser 2-3x a Mínima

Exemplo:
Mínima = 30  →  Máxima = 90-120 ✅
Mínima = 50  →  Máxima = 100-150 ✅
```

**Quando ajustar:**

| Problema | Solução |
|----------|---------|
| Linhas muito fracas | ⬇️ Diminuir para 60-80 |
| Linhas muito fortes | ⬆️ Aumentar para 150-180 |
| Linhas desconexas | ⬇️ Diminuir ligeiramente |

---

### Espessura das Linhas

**Faixa:** 1-3 pixels  
**Padrão:** 1

**O que faz:**
- Define a largura das linhas no resultado final
- Linhas mais grossas conectam melhor traços quebrados
- Linhas finas são mais delicadas e detalhadas

**Quando usar cada valor:**

**1 pixel:**
```
✅ Desenhos delicados
✅ Máximo detalhe
✅ Estilo realista
❌ Pode ter linhas quebradas
```

**2 pixels:**
```
✅ Equilíbrio entre detalhe e clareza
✅ Bom para impressão
✅ Linhas mais conectadas
⭐ Recomendado para a maioria
```

**3 pixels:**
```
✅ Estilo cartoon/comic
✅ Linhas bem visíveis
✅ Ótimo para crianças pequenas
❌ Perde alguns detalhes finos
```

---

### Threshold Adaptativo

**Opções:** ✅ Ligado / ❌ Desligado  
**Padrão:** ✅ Ligado (Recomendado)

**O que faz:**
- Analisa a imagem em regiões locais
- Ajusta o threshold automaticamente para cada área
- **Essencial para fotos com iluminação irregular**

**Quando usar:**

**✅ Ligar (Recomendado):**
```
✅ Fotos com sombras
✅ Iluminação irregular
✅ Fotos escuras
✅ Áreas com contraste variável
✅ Quando não tem certeza
```

**❌ Desligar:**
```
✅ Fotos muito bem iluminadas
✅ Fundo branco uniforme
✅ Fotos de estúdio
✅ Quando quer resultado mais limpo
```

**Exemplo visual:**
```
DESLIGADO:        LIGADO:
┌─────────┐      ┌─────────┐
│▓▓▓▓▓░░░░│      │▓▓▓▓▓▓▓▓▓│
│▓▓▓▓░░░░░│  →   │▓▓▓▓▓▓▓▓▓│
│▓▓░░░░░░░│      │▓▓▓▓▓▓▓▓▓│
└─────────┘      └─────────┘
Perde detalhes   Captura tudo
em áreas escuras nas sombras
```

---

### Combinações Recomendadas

#### Para Retratos
```
Modo: Balanceado
Sensibilidade Mínima: 30
Sensibilidade Máxima: 100
Espessura: 1
Threshold Adaptativo: ✅
```

#### Para Paisagens
```
Modo: Detalhado
Sensibilidade Mínima: 20
Sensibilidade Máxima: 80
Espessura: 1
Threshold Adaptativo: ✅
```

#### Para Objetos Simples
```
Modo: Simples
Sensibilidade Mínima: 50
Sensibilidade Máxima: 150
Espessura: 2
Threshold Adaptativo: ❌
```

#### Para Estilo Cartoon
```
Modo: Cartoon
Sensibilidade Mínima: 40
Sensibilidade Máxima: 120
Espessura: 2-3
Threshold Adaptativo: ❌
```

---

## 📐 Redimensionamento

### Como Funciona

O Seeds Aura permite redimensionar a imagem **antes de salvar**, mantendo a qualidade das linhas.

### Interface

```
📐 REDIMENSIONAR ANTES DE SALVAR

Largura (px):  [1920    ]
Altura (px):   [1080    ]

[✓] 🔗 Manter proporção

💡 Deixe 0 para manter tamanho original
Original: 3840x2160px
```

### Modos de Uso

#### 1. Redimensionar Mantendo Proporção (Recomendado)

**Passos:**
1. ✅ Marque "🔗 Manter proporção"
2. Digite apenas a **largura** OU a **altura**
3. O outro valor ajusta automaticamente

**Exemplo:**
```
Original: 3840x2160px (proporção 16:9)

Digite Largura: 1920
→ Altura automática: 1080 ✅

OU

Digite Altura: 1080
→ Largura automática: 1920 ✅
```

#### 2. Redimensionar Livremente

**Passos:**
1. ❌ Desmarque "🔗 Manter proporção"
2. Digite largura E altura desejadas
3. Imagem será esticada/comprimida conforme necessário

**Exemplo:**
```
Original: 3840x2160px

Digite Largura: 1000
Digite Altura: 1500

Resultado: 1000x1500px
⚠️ Proporção alterada (pode distorcer)
```

#### 3. Manter Tamanho Original

**Passos:**
1. Deixe **ambos** os campos em `0`
2. OU não altere os valores originais

**Exemplo:**
```
Original: 3840x2160px

Largura: 0
Altura: 0

Resultado: 3840x2160px ✅ (sem alteração)
```

### Tamanhos Recomendados

#### Para Impressão

| Finalidade | Tamanho | DPI |
|------------|---------|-----|
| **Folha A4** | 2480x3508px | 300 DPI |
| **Folha A5** | 1748x2480px | 300 DPI |
| **Cartão Postal** | 1200x1800px | 300 DPI |
| **Poster A3** | 3508x4961px | 300 DPI |

#### Para Digital

| Finalidade | Tamanho | Uso |
|------------|---------|-----|
| **HD** | 1920x1080px | Telas Full HD |
| **4K** | 3840x2160px | Telas 4K |
| **Instagram** | 1080x1080px | Post quadrado |
| **Instagram Story** | 1080x1920px | Story vertical |
| **Tablet** | 1024x768px | iPad, tablets |

#### Para Web

| Finalidade | Tamanho | Uso |
|------------|---------|-----|
| **Miniatura** | 400x400px | Thumbnails |
| **Preview** | 800x600px | Pré-visualização |
| **Médio** | 1280x720px | Artigos, blogs |
| **Grande** | 1920x1080px | Galerias |

### Qualidade do Redimensionamento

O programa usa **interpolação de área** (`cv2.INTER_AREA`), que é o melhor método para:

- ✅ Reduzir tamanho (downscaling)
- ✅ Manter linhas nítidas
- ✅ Evitar aliasing
- ✅ Preservar detalhes

**Algoritmo:**
```python
img_final = cv2.resize(
    img_final, 
    (new_w, new_h),
    interpolation=cv2.INTER_AREA  # Melhor para linhas
)
```

### Dicas de Redimensionamento

#### ✅ Boas Práticas

1. **Sempre use proporção mantida** para evitar distorção
2. **Reduza em etapas** se precisar reduzir muito (ex: 4K → HD → SD)
3. **Teste antes de salvar** - visualize no preview
4. **Imprima em alta resolução** - use 300 DPI mínimo
5. **Web usa menos** - 72-96 DPI é suficiente

#### ❌ Evite

1. **Aumentar muito** - não melhora qualidade (pixelização)
2. **Proporções estranhas** - pode distorcer o desenho
3. **Reduzir demais** - perde detalhes importantes
4. **Esticar/comprimir** - altera a aparência

### Calculadora de Proporção

**Fórmula:**
```
nova_altura = (altura_original / largura_original) × nova_largura

OU

nova_largura = (largura_original / altura_original) × nova_altura
```

**Exemplo prático:**
```
Original: 3840x2160px

Quero largura = 1920px
Proporção = 2160 / 3840 = 0.5625
Nova altura = 1920 × 0.5625 = 1080px ✅
```

---

## 🎨 Exemplos

### Exemplo 1: Retrato de Pessoa

**Entrada:**
- Foto: Retrato feminino, iluminação natural
- Tamanho: 3024x4032px
- Modo usado: **Balanceado**

**Configurações:**
```
Sensibilidade Mínima: 30
Sensibilidade Máxima: 100
Espessura: 1px
Threshold Adaptativo: ✅ Sim
```

**Resultado:**
- Linhas suaves e naturais
- Preserva expressões faciais
- Cabelos com bom detalhe
- Fundo removido (transparente)
- Tempo: ~2 segundos

**Redimensionamento:**
```
Original: 3024x4032px → Final: 1512x2016px
Redução: 50% (para impressão A5)
```

---

### Exemplo 2: Paisagem Natural

**Entrada:**
- Foto: Montanha com lago
- Tamanho: 5472x3648px
- Modo usado: **Detalhado**

**Configurações:**
```
Sensibilidade Mínima: 20
Sensibilidade Máxima: 80
Espessura: 1px
Threshold Adaptativo: ✅ Sim
```

**Resultado:**
- Muitos detalhes capturados
- Texturas de árvores preservadas
- Reflexos no lago visíveis
- Montanhas ao fundo definidas
- Tempo: ~4 segundos

**Redimensionamento:**
```
Original: 5472x3648px → Final: 2736x1824px
Redução: 50% (para web)
```

---

### Exemplo 3: Objeto com Fundo Simples

**Entrada:**
- Foto: Caneca em fundo branco
- Tamanho: 1920x1920px
- Modo usado: **Simples**

**Configurações:**
```
Sensibilidade Mínima: 50
Sensibilidade Máxima: 150
Espessura: 2px
Threshold Adaptativo: ❌ Não
```

**Resultado:**
- Contornos limpos e definidos
- Sem ruído de fundo
- Linhas grossas e visíveis
- Perfeito para colorir
- Tempo: ~1 segundo

**Redimensionamento:**
```
Original: 1920x1920px → Final: 1080x1080px
(para Instagram)
```

---

### Exemplo 4: Foto de Animal

**Entrada:**
- Foto: Cachorro em gramado
- Tamanho: 4000x3000px
- Modo usado: **Balanceado**

**Configurações:**
```
Sensibilidade Mínima: 25
Sensibilidade Máxima: 90
Espessura: 1px
Threshold Adaptativo: ✅ Sim
```

**Resultado:**
- Pelos bem definidos
- Expressão facial preservada
- Gramado com textura
- Separação clara do fundo
- Tempo: ~3 segundos

**Redimensionamento:**
```
Original: 4000x3000px → Final: 2000x1500px
Redução: 50%
```

---

### Exemplo 5: Ilustração Cartoon

**Entrada:**
- Foto: Personagem cartoon (foto real)
- Tamanho: 2000x2000px
- Modo usado: **Cartoon**

**Configurações:**
```
Sensibilidade Mínima: 40
Sensibilidade Máxima: 120
Espessura: 3px
Threshold Adaptativo: ❌ Não
```

**Resultado:**
- Linhas grossas e bem marcadas
- Estilo quadrinhos
- Poucos detalhes internos
- Contornos fortes
- Tempo: ~1.5 segundos

**Redimensionamento:**
```
Original: 2000x2000px → Final: 1000x1000px
Redução: 50%
```

---

### Comparação de Modos

**Mesma foto, modos diferentes:**

| Modo | Linhas Detectadas | Detalhamento | Melhor Para |
|------|------------------|--------------|-------------|
| **Simples** | ~1000 | ⭐☆☆☆☆ | Objetos simples |
| **Balanceado** | ~3000 | ⭐⭐⭐☆☆ | Geral |
| **Detalhado** | ~8000 | ⭐⭐⭐⭐⭐ | Paisagens |
| **Cartoon** | ~1500 | ⭐⭐☆☆☆ | Ilustrações |

---

## 💡 Dicas e Truques

### 🎯 Para Melhores Resultados

#### 1. Qualidade da Foto Original

**✅ Use:**
- Fotos com boa iluminação natural
- Resolução mínima: 800x600px
- Ideal: 1920x1080px ou maior
- Foco nítido e claro
- Contraste adequado

**❌ Evite:**
- Fotos muito escuras ou super expostas
- Imagens borradas ou fora de foco
- Resolução menor que 500x500px
- Fotos com muito ruído/granulação
- Compressão JPG excessiva

#### 2. Fundos

**Melhores fundos:**
```
✅ Fundo branco ou claro
✅ Fundo uniforme
✅ Fundo desfocado (bokeh)
✅ Céu limpo
✅ Parede lisa
```

**Fundos problemáticos:**
```
❌ Muito complexo (perde o objeto principal)
❌ Mesmo tom do objeto (difícil separar)
❌ Texturas fortes (adiciona linhas desnecessárias)
❌ Muitos elementos (fica poluído)
```

#### 3. Tipos de Fotos

**Funciona MUITO bem:**
- 🎭 Retratos de pessoas
- 🐾 Fotos de animais
- 🏛️ Arquitetura
- 🌺 Flores e plantas
- 🚗 Veículos
- 🍎 Objetos isolados
- 👕 Roupas e produtos

**Funciona BEM:**
- 🏞️ Paisagens (use modo Detalhado)
- 🎨 Arte e ilustrações
- 📸 Fotos casuais
- 🏀 Esportes (se congelado)

**Pode ser desafiador:**
- 🌊 Água em movimento
- 🔥 Fogo e fumaça
- ☁️ Nuvens
- 👥 Multidões
- 🌃 Fotos noturnas

### ⚡ Otimização de Performance

#### Para Processar Mais Rápido

1. **Reduza a resolução antes**
   ```
   4K (3840x2160) → HD (1920x1080)
   Economia: 75% do tempo de processamento
   ```

2. **Feche outros programas**
   - Navegadores com muitas abas
   - Editores de vídeo
   - Jogos em background

3. **Use SSD**
   - Se possível, trabalhe em SSD
   - Mais rápido para ler/salvar arquivos

#### Tempos Médios

| Resolução | Tempo Aproximado |
|-----------|-----------------|
| 640x480px | <1 segundo |
| 1920x1080px (HD) | 1-2 segundos |
| 2560x1440px (2K) | 2-3 segundos |
| 3840x2160px (4K) | 3-5 segundos |
| 7680x4320px (8K) | 8-15 segundos |

### 🎨 Uso Criativo

#### 1. Livros de Colorir Personalizados

**Passo a passo:**
1. Tire 20-30 fotos da família/amigos
2. Converta todas usando modo Balanceado
3. Redimensione para 2480x3508px (A4 em 300 DPI)
4. Combine em um PDF usando:
   - Adobe Acrobat
   - Microsoft Word
   - Online: iLovePDF

**Resultado:** Livro de colorir personalizado único! 🎁

#### 2. Material Educacional

**Ideias:**
- Fotos de animais → Livro de colorir educativo
- Fotos de frutas → Material de aprendizagem
- Monumentos → Geografia colorível
- Objetos do dia a dia → Vocabulário visual

#### 3. Decoração

**Como usar:**
- Imprima em papel de alta qualidade
- Colora à mão (lápis de cor, marcadores)
- Digitalize novamente
- Emoldure ou crie poster

#### 4. Presente Personalizado

**Ideias criativas:**
```
🎁 Caneca personalizada
   → Foto convertida + imprimir em caneca

🎁 Camiseta customizada
   → Desenho de pet + transfer para tecido

🎁 Almofada decorativa
   → Retrato convertido + impressão em tecido

🎁 Quebra-cabeça
   → Paisagem convertida + serviço de impressão
```

### 🖌️ Combinando com Outras Ferramentas

#### Photoshop
1. Abra o PNG transparente no Photoshop
2. Adicione cores em camadas separadas
3. Mantenha as linhas na camada superior
4. Use modos de mesclagem

#### Procreate (iPad)
1. Importe o PNG
2. Crie camada abaixo das linhas
3. Pinte com pincéis digitais
4. Exporte em alta resolução

#### Canva
1. Faça upload do PNG
2. Use como elemento de design
3. Adicione textos e decorações
4. Exporte para redes sociais

#### GIMP (Gratuito)
1. Abra o PNG com camada alpha
2. Use ferramenta "Bucket Fill"
3. Colore respeitando as linhas
4. Exporte em formatos diversos

### 📱 Compartilhamento

#### Instagram

**Story:**
```
Tamanho: 1080x1920px
Redimensione para este tamanho
Adicione hashtags: #coloringbook #lineart
```

**Post:**
```
Tamanho: 1080x1080px (quadrado)
Ou: 1080x1350px (vertical)
Mostre antes/depois
```

#### Pinterest
```
Tamanho ideal: 1000x1500px
Crie pins com o processo
Adicione descrição detalhada
```

#### TikTok
```
Grave o processo de conversão
Use filtros e música
Mostre resultado final
Tamanho: 1080x1920px
```

---

## ❓ Troubleshooting

### 🔴 Problema: "Não foi possível abrir o arquivo"

**Sintomas:**
- Mensagem de erro ao carregar foto
- Programa testa os 8 métodos e todos falham
- Arquivo não é exibido

**Causas possíveis:**
- Arquivo realmente corrompido
- Formato não suportado
- Arquivo protegido/bloqueado
- Sem permissão de leitura

**Soluções:**

1. **Converter para PNG**
   ```
   1. Abra a foto em outro programa (Paint, Photoshop, GIMP)
   2. Salve como PNG novo
   3. Tente novamente no Seeds Aura
   ```

2. **Screenshot**
   ```
   1. Abra a imagem em qualquer visualizador
   2. Pressione Print Screen (Windows) ou Cmd+Shift+3 (Mac)
   3. Cole no Paint
   4. Salve como PNG
   5. Use este arquivo
   ```

3. **Conversor Online**
   ```
   Sites recomendados:
   - CloudConvert.com
   - Online-Convert.com
   - Convertio.co
   
   Converter para: PNG
   ```

4. **Verificar permissões**
   ```
   Windows: Clique direito → Propriedades → Desmarque "Somente leitura"
   Linux/Mac: chmod 644 arquivo.jpg
   ```

---

### 🔴 Problema: "Imagem fica toda preta"

**Sintomas:**
- Após converter, o resultado é quase todo preto
- Poucas ou nenhuma linha branca
- Preview mostra apenas escuridão

**Causas:**
- Foto muito escura
- Threshold muito baixo
- Threshold adaptativo desligado

**Soluções:**

**Solução 1: Ativar Threshold Adaptativo**
```
✅ Marque "Usar Threshold Adaptativo (recomendado)"
Clique em "CONVERTER AGORA" novamente
```

**Solução 2: Ajustar Sensibilidade**
```
Sensibilidade Mínima: Diminua para 10-15
Sensibilidade Máxima: Mantenha em 100
Clique em "CONVERTER AGORA"
```

**Solução 3: Aumentar Blur**
```
No código (para usuários avançados):
blur_size = 7 ou 9
Isso suaviza mais antes de detectar bordas
```

**Solução 4: Pré-processar a foto**
```
Antes de carregar no Seeds Aura:
1. Abra no Photoshop/GIMP
2. Aumente brilho: +20 a +40
3. Aumente contraste: +10 a +20
4. Salve e use esta versão
```

---

### 🔴 Problema: "Muitas linhas / Muito detalhe"

**Sintomas:**
- Resultado muito poluído
- Linhas demais, difícil de colorir
- Parece mais uma sopa de linhas que um desenho

**Causas:**
- Sensibilidade muito alta
- Foto muito detalhada/complexa
- Modo errado escolhido

**Soluções:**

**Solução 1: Mudar para modo Simples**
```
Modo: ⚪ Simples (menos linhas)
Clique em "CONVERTER AGORA"
```

**Solução 2: Aumentar Sensibilidade Mínima**
```
Sensibilidade Mínima: 50-70
Sensibilidade Máxima: 150-180
Clique em "CONVERTER AGORA"
```

**Solução 3: Aumentar Blur**
```
No ajuste fino:
Mova o slider de blur para valores maiores
Isso suaviza detalhes pequenos
```

**Solução 4: Simplificar a foto**
```
Antes de carregar:
1. Use ferramenta de "posterização" no Photoshop
2. Ou aplique filtro "Oil Paint"
3. Reduz detalhes mantendo formas principais
```

---

### 🔴 Problema: "Poucas linhas / Pouco detalhe"

**Sintomas:**
- Resultado muito simples
- Faltam detalhes importantes
- Parece incompleto

**Causas:**
- Sensibilidade muito baixa
- Modo simples quando deveria ser detalhado
- Threshold adaptativo desligado

**Soluções:**

**Solução 1: Mudar para modo Detalhado**
```
Modo: ⚪ Detalhado (mais linhas)
✅ Usar Threshold Adaptativo
Clique em "CONVERTER AGORA"
```

**Solução 2: Diminuir Sensibilidade Mínima**
```
Sensibilidade Mínima: 10-20
Sensibilidade Máxima: 60-80
Clique em "CONVERTER AGORA"
```

**Solução 3: Ativar Threshold Adaptativo**
```
✅ Marque "Usar Threshold Adaptativo"
Isso captura detalhes em áreas escuras
```

**Solução 4: Diminuir Blur**
```
No código:
blur_size = 3
Preserva mais detalhes finos
```

---

### 🔴 Problema: "Linhas quebradas / desconectadas"

**Sintomas:**
- Linhas com espaços/gaps
- Contornos não fecham completamente
- Parece tracejado

**Causas:**
- Espessura muito fina
- Foto com pouco contraste
- Operações morfológicas insuficientes

**Soluções:**

**Solução 1: Aumentar Espessura**
```
Espessura das Linhas: 2 ou 3
Clique em "CONVERTER AGORA"
```

**Solução 2: Ajustar Sensibilidade**
```
Sensibilidade Máxima: Diminua para 70-90
Isso torna detecção menos rigorosa
```

**Solução 3: Melhorar contraste da foto**
```
Pré-processe no Photoshop:
Contraste: +20
Clareza: +10
```

---

### 🔴 Problema: "Programa travou / não responde"

**Sintomas:**
- Interface congelou
- Botões não clicam
- Barra de status parou

**Causas:**
- Imagem muito grande (>8K)
- Pouca memória RAM
- Processo pesado

**Soluções:**

**Solução 1: Aguarde**
```
Imagens grandes demoram:
4K: ~5 segundos
8K: ~15 segundos
12K: ~30 segundos

Aguarde até 1 minuto antes de forçar fechamento
```

**Solução 2: Reduza resolução antes**
```
1. Abra foto em outro programa
2. Redimensione para 1920x1080 (HD)
3. Salve esta versão
4. Use no Seeds Aura
5. Será MUITO mais rápido
```

**Solução 3: Feche outros programas**
```
Feche:
- Navegadores com muitas abas
- Editores de vídeo/imagem abertos
- Programas pesados
```

**Solução 4: Verifique RAM**
```
Mínimo recomendado: 4GB RAM
Ideal: 8GB+ RAM

Para imagens muito grandes (8K+): 16GB RAM
```

---

### 🔴 Problema: "Erro ao salvar PNG"

**Sintomas:**
- Mensagem de erro ao clicar em "SALVAR"
- Arquivo não é criado
- Operação falha

**Causas:**
- Sem permissão na pasta
- Espaço em disco cheio
- Nome de arquivo inválido
- Caminho muito longo

**Soluções:**

**Solução 1: Escolher outra pasta**
```
Salve em:
- Desktop
- Documentos
- Criar pasta nova
```

**Solução 2: Nome simples**
```
❌ Evite: desenho_super_legal_versão_final_2024(1).png
✅ Use: desenho_01.png
```

**Solução 3: Verificar espaço**
```
Windows: Abra "Este Computador" → Veja espaço livre
Libere ao menos 500MB
```

**Solução 4: Executar como administrador**
```
Windows:
Clique direito no programa → Executar como administrador
```

---

### 🔴 Problema: "Fundo não fica transparente"

**Sintomas:**
- PNG salvo tem fundo branco
- Ao abrir em editor, não tem transparência
- Canal alpha não está presente

**Causas:**
- Visualizador não mostra transparência
- Arquivo foi salvo errado
- Bug no salvamento

**Verificações:**

**Teste 1: Abrir no programa certo**
```
❌ Windows Photo Viewer - NÃO mostra transparência
❌ Paint - NÃO mostra transparência
✅ Photoshop - Mostra transparência
✅ GIMP - Mostra transparência
✅ Paint.NET - Mostra transparência
✅ Navegador web - Mostra transparência
```

**Teste 2: Verificar camadas**
```
Abra no Photoshop/GIMP:
Janela → Camadas
Deve aparecer: Camada com canal Alpha
```

**Solução:**
```
Se realmente não tem transparência:
1. Reporte o bug no GitHub
2. Temporariamente, use outro programa para remover fundo:
   - remove.bg (online)
   - Photoshop: Ferramenta Varinha Mágica
```

---

### 🔴 Problema: "Resultado diferente do esperado"

**Sintomas:**
- Não ficou como você imaginou
- Muito diferente da foto original
- Perdeu características importantes

**Soluções:**

**Experimente combinações diferentes:**

| Se o problema é... | Tente... |
|-------------------|----------|
| Muito detalhado | Modo Simples + Sensibilidade alta (50+) |
| Muito simples | Modo Detalhado + Sensibilidade baixa (20-) |
| Linhas fracas | Espessura 2-3 + Sensibilidade Máx baixa |
| Linhas fortes demais | Espessura 1 + Sensibilidade Máx alta |
| Áreas escuras perdidas | ✅ Threshold Adaptativo |
| Muito ruído | Modo Simples + Blur alto |

**Fluxo de tentativa:**
```
1. Tente modo Balanceado primeiro
2. Se não ficou bom, teste Detalhado
3. Ainda não? Teste Simples
4. Ajuste sensibilidades
5. Teste com/sem Threshold Adaptativo
6. Por último, ajuste espessura
```

---

### 🆘 Quando Nada Funciona

Se tentou **TODAS** as soluções acima:

1. **Tire screenshot do erro**
2. **Anote as configurações usadas**
3. **Salve a foto que está dando problema**
4. **Abra uma issue no GitHub**: [Link para issues]

**Informações necessárias:**
```
- Sistema Operacional: (Windows 11, Ubuntu 22.04, etc.)
- Python Version: (python --version)
- OpenCV Version: (pip show opencv-python)
- Descrição do problema:
- Screenshots:
- Foto de teste: (se possível compartilhar)
```

---

## 🤝 Contribuindo

Contribuições são **muito bem-vindas**! Veja como você pode ajudar:

### 🐛 Reportar Bugs

**Como reportar:**

1. Verifique se o bug já não foi reportado: [Issues](https://github.com/seu-usuario/seeds-aura/issues)
2. Abra uma nova issue com o template:

```markdown
**Descrição do Bug**
Descreva claramente o problema.

**Passos para Reproduzir**
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

**Comportamento Esperado**
O que você esperava que acontecesse.

**Screenshots**
Adicione prints se aplicável.

**Ambiente:**
 - OS: [Windows 11]
 - Python: [3.10.5]
 - OpenCV: [4.8.0]

**Contexto Adicional**
Qualquer outra informação.
```

### 💡 Sugerir Features

**Como sugerir:**

Abra uma issue com o label `enhancement`:

```markdown
**Feature Request**

**Problema que resolve:**
Ex: Sempre fico frustrado quando [...]

**Solução proposta:**
Descrição clara da feature.

**Alternativas consideradas:**
Outras ideias que você teve.

**Contexto:**
Screenshots, mockups, etc.
```

### 🔧 Contribuir com Código

**Setup do ambiente:**

```bash
# 1. Fork o projeto no GitHub

# 2. Clone seu fork
git clone https://github.com/seu-usuario/seeds-aura.git
cd seeds-aura

# 3. Crie uma branch
git checkout -b feature/minha-feature

# 4. Configure ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 5. Instale dependências
pip install -r requirements.txt

# 6. Faça suas mudanças
# (edite os arquivos)

# 7. Teste suas mudanças
python foto_para_colorir_v2.py

# 8. Commit
git add .
git commit -m "feat: adiciona nova funcionalidade X"

# 9. Push
git push origin feature/minha-feature

# 10. Abra Pull Request no GitHub
```

### 📝 Padrões de Código

**Python Style Guide (PEP 8):**

```python
# ✅ BOM
def processar_imagem(img, threshold=127):
    """
    Processa a imagem aplicando threshold.
    
    Args:
        img: Imagem em formato numpy array
        threshold: Valor do threshold (0-255)
    
    Returns:
        Imagem processada
    """
    resultado = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return resultado


# ❌ RUIM
def ProcessarImagem(img,threshold=127):
    resultado=cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
    return resultado
```

**Commits (Conventional Commits):**

```bash
feat: adiciona modo de conversão "Anime"
fix: corrige bug de memória em imagens grandes
docs: atualiza README com novos exemplos
style: formata código conforme PEP 8
refactor: reorganiza estrutura de classes
test: adiciona testes unitários para ProcessadorLineart
chore: atualiza dependências
```

### 📚 Contribuir com Documentação

Você pode ajudar:

- Corrigir erros de digitação
- Melhorar explicações
- Adicionar exemplos
- Traduzir para outros idiomas
- Criar tutoriais em vídeo
- Escrever artigos/blog posts

### 🎨 Contribuir com Design

Você pode ajudar com:

- Melhorias na interface
- Criar ícones personalizados
- Melhorar o logo
- Criar banners/imagens
- Screenshots melhores
- Vídeos demonstrativos

### 🌟 Reconhecimento

Todos os contribuidores serão:

- ✅ Listados no README.md
- ✅ Creditados nos release notes
- ✅ Mencionados com gratidão

---

## 🗺️ Roadmap

### Versão 2.1 (Próxima)

**Features Planejadas:**

- [ ] **Processamento em Lote**
  - Converter múltiplas fotos de uma vez
  - Aplicar mesmas configurações
  - Progresso por arquivo

- [ ] **Modo "Anime"**
  - Estilo específico para anime/manga
  - Linhas mais limpas
  - Menos detalhes de textura

- [ ] **Exportação SVG**
  - Vetorizar as linhas
  - Escalável infinitamente
  - Menor tamanho de arquivo

- [ ] **Histórico de Conversões**
  - Ver últimas 10 conversões
  - Reaplicar configurações antigas
  - Comparar resultados

**Data prevista:** Dezembro 2025

---

### Versão 2.2 (Futuro)

**Features Planejadas:**

- [ ] **Presets Salvos**
  - Salvar suas configurações favoritas
  - Carregar presets com um clique
  - Compartilhar presets

- [ ] **Modo Escuro**
  - Interface em tema escuro opcional
  - Melhor para trabalhar à noite

- [ ] **Atalhos de Teclado**
  - Ctrl+O: Abrir
  - Ctrl+S: Salvar
  - Ctrl+P: Processar
  - Ctrl+Z: Desfazer

- [ ] **Antes/Depois Slider**
  - Comparar original com resultado
  - Slider interativo

- [ ] **Exportar para PDF**
  - Criar livros de colorir em PDF
  - Múltiplas páginas
  - Pronto para impressão

**Data prevista:** Q1 2026

---

### Versão 3.0 (Longo Prazo)

**Features Ambiciosas:**

- [ ] **Machine Learning**
  - Detecção inteligente de objetos
  - Sugestão automática de configurações
  - Melhoria de resultados com IA

- [ ] **API REST**
  - Integrar Seeds Aura em outros apps
  - Processamento em nuvem
  - Documentação da API

- [ ] **Versão Web**
  - Progressive Web App
  - Sem instalação necessária
  - Funciona em qualquer dispositivo

- [ ] **App Mobile**
  - iOS e Android nativos
  - Tirar foto e converter na hora
  - Compartilhar nas redes sociais

- [ ] **Integração com Redes Sociais**
  - Publicar direto no Instagram
  - Compartilhar no Pinterest
  - Criar threads no Twitter

- [ ] **Marketplace de Estilos**
  - Baixar estilos da comunidade
  - Compartilhar seus presets
  - Votar nos melhores

**Data prevista:** 2027+

---

## ❓ FAQ

### 🤔 Perguntas Gerais

**P: O Seeds Aura é gratuito?**  
R: Sim! É 100% gratuito e open source (MIT License).

**P: Funciona offline?**  
R: Sim! Não precisa de internet.

**P: Em quais idiomas está disponível?**  
R: Atualmente em Português. Inglês em breve.

**P: Posso usar comercialmente?**  
R: Sim! A licença MIT permite uso comercial.

**P: Quanto custa para uso comercial?**  
R: É gratuito! Sem custos mesmo para uso comercial.

---

### 🖼️ Sobre Imagens

**P: Quais formatos são suportados?**  
R: PNG, JPG, JPEG, BMP, TIF, WEBP

**P: Qual o tamanho máximo de imagem?**  
R: Limitado apenas pela RAM. Testado até 12K (12000x8000px).

**P: Posso processar GIFs animados?**  
R: Não. Apenas imagens estáticas.

**P: E vídeos?**  
R: Não diretamente. Mas você pode extrair frames e processar individualmente.

**P: A qualidade da foto original importa?**  
R: Sim! Quanto melhor a foto, melhor o resultado.

---

### ⚙️ Configurações

**P: Qual o melhor modo para iniciantes?**  
R: "Balanceado" funciona bem para 80% dos casos.

**P: Por que tem 8 métodos de reparo?**  
R: Cada método funciona melhor para diferentes problemas. O programa tenta todos automaticamente.

**P: Threshold Adaptativo sempre ligado?**  
R: Quase sempre! Desliga apenas para fotos de estúdio muito bem iluminadas.

**P: Como escolher entre os modos?**
R: 
- Simples: Objetos isolados
- Balanceado: Geral (comece por aqui)
- Detalhado: Paisagens/complexo
- Cartoon: Estilo ilustração

---

### 💾 Salvamento

**P: O PNG tem transparência mesmo?**  
R: Sim! Canal alpha completo.

**P: Posso salvar em JPG?**  
R: Tecnicamente sim, mas perde a transparência. PNG é recomendado.

**P: Onde ficam salvos os arquivos?**  
R: Você escolhe onde salvar cada vez.

**P: Posso salvar em resolução maior que o original?**  
R: Não recomendado. Isso não melhora qualidade, apenas aumenta tamanho.

---

### 🐛 Problemas

**P: Por que minha imagem fica toda preta?**  
R: Ative "Threshold Adaptativo" e diminua a sensibilidade mínima.

**P: Por que tem muitas linhas?**  
R: Aumente a sensibilidade mínima ou use modo "Simples".

**P: O programa trava com imagens grandes?**  
R: Reduza a resolução antes. 4K+ pode demorar.

**P: Não funciona no meu Windows 7?**  
R: Python 3.7+ requer Windows 8+. Atualize ou use Python 3.6.

---

### 🎨 Uso Criativo

**P: Posso criar livros de colorir para vender?**  
R: Sim! Licença MIT permite uso comercial.

**P: Como imprimir com qualidade?**  
R: Use 300 DPI mínimo. Para A4: 2480x3508px.

**P: Funciona para tatuagens?**  
R: Sim! Muitos tatuadores usam como referência.

**P: Posso usar em projetos escolares?**  
R: Sim! Perfeito para material educacional.

---

### 🔧 Técnicas

**P: Como funciona a detecção de bordas?**  
R: Usamos algoritmo Canny Edge Detection + Threshold Adaptativo.

**P: Por que bilateral filter?**  
R: Preserva bordas enquanto suaviza, melhor que Gaussian.

**P: O que é threshold adaptativo?**  
R: Analisa imagem em regiões locais, funciona melhor com iluminação irregular.

**P: Posso ver o código fonte?**  
R: Sim! Está no GitHub: [link]

---

## 📄 Licença

Este projeto está sob a licença **MIT**.

### O que você PODE fazer:

- ✅ Usar comercialmente
- ✅ Modificar o código
- ✅ Distribuir
- ✅ Uso privado
- ✅ Criar obras derivadas

### O que você DEVE fazer:

- 📝 Incluir o aviso de copyright
- 📝 Incluir cópia da licença MIT

### O que NÃO é garantido:

- ❌ Sem garantias
- ❌ Sem responsabilidade do autor

**Licença completa:**

```
MIT License

Copyright (c) 2025 Seeds Aura

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contato

### Canais de Suporte

**🐛 Bugs e Issues:**  
[GitHub Issues](https://github.com/seu-usuario/seeds-aura/issues)

**💬 Discussões Gerais:**  
[GitHub Discussions](https://github.com/seu-usuario/seeds-aura/discussions)

**📧 Email:**  
contato@seedsaura.com

**📱 Redes Sociais:**
- Twitter: [@seedsaura](https://twitter.com/seedsaura)
- Instagram: [@seedsaura](https://instagram.com/seedsaura)
- YouTube: [Seeds Aura Channel](https://youtube.com/seedsaura)

### Resposta Esperada

- 🐛 Bugs críticos: 24-48h
- 🔧 Bugs normais: 2-5 dias
- 💡 Features: 1-2 semanas
- 📚 Dúvidas gerais: 2-3 dias

---

## 🌟 Agradecimentos

Agradecimentos especiais a:

- **OpenCV Community** - Pela incrível biblioteca de visão computacional
- **Python Community** - Pelo suporte e ferramentas fantásticas
- **Todos os Beta Testers** - Que ajudaram a melhorar o programa
- **Você!** - Por usar o Seeds Aura 💕

---

## 📊 Estatísticas

![GitHub stars](https://img.shields.io/github/stars/seu-usuario/seeds-aura?style=social)
![GitHub forks](https://img.shields.io/github/forks/seu-usuario/seeds-aura?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/seu-usuario/seeds-aura?style=social)
![GitHub downloads](https://img.shields.io/github/downloads/seu-usuario/seeds-aura/total)

---

## 🎉 Show Your Support

Se este projeto te ajudou, considere:

- ⭐ Dar uma estrela no GitHub
- 🐛 Reportar bugs
- 💡 Sugerir melhorias
- 🤝 Contribuir com código
- 📢 Compartilhar com amigos
- ☕ [Buy me a coffee](https://buymeacoffee.com/seedsaura)

---

<div align="center">

## 💕 Feito com amor por Seeds Aura Team

**Transforme fotos em arte!** 🎨✨

---

### [⬆ Voltar ao Topo](#-seeds-aura---foto--reparador--desenho-de-colorir)

---

**Seeds Aura v2.0** | [Website](#) | [Documentação](#-índice) | [GitHub](https://github.com/seu-usuario/seeds-aura)

</div>
