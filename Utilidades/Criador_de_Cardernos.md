# 📓 Gerador de Cadernos Personalizados - Documentação Completa

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Status](https://img.shields.io/badge/status-Ativo-success.svg)

**Crie cadernos com diferentes padrões de grade personalizáveis com preview em tempo real!**

</div>

---

## 📋 Índice Geral

1. [Sobre o Projeto](#1-sobre-o-projeto)
2. [Funcionalidades](#2-funcionalidades)
3. [Tipos de Grade](#3-tipos-de-grade)
4. [Instalação](#4-instalação)
5. [Como Usar](#5-como-usar)
6. [Parâmetros Personalizáveis](#6-parâmetros-personalizáveis)
7. [Exemplos Práticos](#7-exemplos-práticos)
8. [Estrutura do Código](#8-estrutura-do-código)
9. [Guia de Contribuição](#9-guia-de-contribuição)
10. [Changelog](#10-changelog)
11. [Licença](#11-licença)
12. [Recursos Adicionais](#12-recursos-adicionais)

---

# 1. Sobre o Projeto

## 🎯 Visão Geral

O **Gerador de Cadernos Personalizados** é uma aplicação desktop desenvolvida em Python com PyQt5 que permite criar páginas de caderno com diversos padrões de grade profissionais. Ideal para estudantes, artistas, músicos, engenheiros e qualquer pessoa que precise de páginas customizadas para impressão.

### ✨ Diferenciais

- 🎨 **8 tipos diferentes de grades** (quadriculada, pontos, hexagonal, isométrica, pautada, musical, polar e caligrafia)
- 👁️ **Preview em tempo real** das alterações
- 🎨 **Personalização completa** de cores, tamanhos e margens
- 📄 **Exportação em PDF de alta qualidade** (300 DPI)
- 💻 **Interface intuitiva e moderna**
- ⚡ **Processamento rápido e eficiente**

### 🎓 Para Quem é Este Projeto?

- **Estudantes**: Cadernos de matemática, física, química
- **Artistas**: Bullet journal, desenho, design
- **Músicos**: Pautas para composição e teoria musical
- **Engenheiros**: Desenhos técnicos e isométricos
- **Arquitetos**: Plantas e projetos
- **Jogadores de RPG**: Mapas hexagonais e quadriculados
- **Calígrafos**: Linhas guias para prática
- **Designers**: Grids para mockups e protótipos

---

# 2. Funcionalidades

## 🚀 Funcionalidades Principais

### Padrões Disponíveis

| Padrão | Descrição | Ideal Para |
|--------|-----------|------------|
| **Quadriculada** | Grade com quadrados regulares e destaque opcional | Matemática, desenho técnico, pixel art |
| **Pontos (Dot Grid)** | Pontos espaçados uniformemente | Bullet journal, design, esquemas |
| **Hexagonal** | Grade com hexágonos perfeitos | Jogos RPG, mapas, design orgânico |
| **Isométrica** | Grade triangular para projeção isométrica | Desenho 3D, arquitetura, engenharia |
| **Pautadas (Ruled)** | Linhas horizontais com margem | Escrita, anotações, cartas |
| **Musicais** | Pautas musicais de 5 linhas | Composição musical, partituras |
| **Polar (Circular)** | Círculos concêntricos com raios | Gráficos polares, mandalas, arte |
| **Caligrafia** | Linhas com guias de altura | Prática de caligrafia, lettering |

### Personalizações

- ✅ **Tamanho da página**: A4, A5, A3, Carta (Letter)
- ✅ **Cores personalizáveis**: Escolha qualquer cor para as linhas
- ✅ **Espessura das linhas**: Ajuste fino de 0.1mm a 2.0mm
- ✅ **Margens configuráveis**: De 0mm a 30mm
- ✅ **Parâmetros específicos**: Cada tipo de grade tem opções únicas
- ✅ **Linhas de destaque**: Para grades quadriculadas (estilo papel milimetrado)

---

# 3. Tipos de Grade

## 📐 Detalhamento Completo

### 1. Grade Quadriculada
```
Parâmetros:
- Tamanho do quadrado: 5-30mm
- Destacar a cada N linhas (opcional)
- Espessura das linhas de destaque
- Ideal para: papel milimetrado, gráficos, pixel art
```
**Características:**
- Quadrados perfeitos
- Opção de linhas de destaque mais grossas
- Ótimo contraste visual
- Perfeito para desenho técnico

### 2. Pontos (Dot Grid)
```
Parâmetros:
- Espaçamento dos pontos: 5-30mm
- Tamanho do ponto automático
- Ideal para: bullet journal, diagramas
```
**Características:**
- Discreto e minimalista
- Não interfere na escrita
- Permite linhas retas e curvas
- Favorito para planejamento criativo

### 3. Grade Hexagonal
```
Parâmetros:
- Tamanho do hexágono: 5-30mm
- Hexágonos regulares perfeitos
- Ideal para: mapas de jogos, estruturas
```
**Características:**
- Geometria perfeita
- Padrão de colmeia
- Excelente para mapas táticos
- Usado em board games

### 4. Grade Isométrica
```
Parâmetros:
- Tamanho da grade: 5-30mm
- Ângulos precisos de 30°
- Ideal para: desenhos 3D, projetos
```
**Características:**
- Projeção isométrica verdadeira
- Três eixos de 30°
- Perspectiva sem ponto de fuga
- Essencial para engenharia

### 5. Linhas Pautadas
```
Parâmetros:
- Espaçamento das linhas: 6-15mm
- Margem esquerda automática
- Ideal para: escrita, anotações
```
**Características:**
- Clássica e funcional
- Margem vermelha opcional
- Padrão de caderno escolar
- Perfeito para redações

### 6. Pautas Musicais
```
Parâmetros:
- Altura da pauta: 15-30mm
- 5 linhas por pauta
- Espaçamento entre pautas
- Ideal para: composição musical
```
**Características:**
- Padrão profissional
- Espaçamento adequado
- Múltiplas pautas por página
- Pronto para notação musical

### 7. Grade Polar
```
Parâmetros:
- Número de círculos: 5-20
- Número de raios: 4-36
- Ideal para: gráficos polares, mandalas
```
**Características:**
- Círculos concêntricos
- Raios angulares uniformes
- Centro perfeitamente alinhado
- Arte circular e gráficos

### 8. Linhas de Caligrafia
```
Parâmetros:
- Altura da linha: 10-25mm
- Linha base, meio e superior
- Ideal para: prática de lettering
```
**Características:**
- Três linhas guias
- Proporções perfeitas
- Espaçamento consistente
- Prática de escrita bonita

---

# 4. Instalação

## 📥 Guia de Instalação Completo

### 🔧 Requisitos do Sistema

**Sistema Operacional:**
- Windows 7/8/10/11
- macOS 10.13+
- Linux (Ubuntu, Fedora, Debian, etc.)

**Dependências:**
```txt
Python 3.7 ou superior
PyQt5 >= 5.15.0
numpy >= 1.19.0
```

---

### 💻 Windows

#### Método 1: Instalação Simples

**Passo 1: Instale o Python**
1. Vá para https://www.python.org/downloads/
2. Baixe Python 3.7 ou superior
3. ⚠️ **IMPORTANTE**: Marque "Add Python to PATH" durante a instalação

**Passo 2: Baixe o Projeto**
1. Clique no botão verde "Code" no GitHub
2. Selecione "Download ZIP"
3. Extraia em uma pasta de sua escolha

**Passo 3: Instale as Dependências**
Abra o Prompt de Comando (CMD) e execute:
```bash
cd caminho\para\gerador-cadernos
pip install -r requirements.txt
```

**Passo 4: Execute o Programa**
```bash
python Criador_de_Cadernos.py
```

#### Método 2: Usando Ambiente Virtual (Recomendado)

```bash
# Navegue até a pasta do projeto
cd caminho\para\gerador-cadernos

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o programa
python Criador_de_Cadernos.py
```

---

### 🍎 macOS

**Passo 1: Instale o Python (se necessário)**
```bash
# Usando Homebrew
brew install python3
```

**Passo 2: Clone ou Baixe o Projeto**
```bash
git clone https://github.com/seu-usuario/gerador-cadernos.git
cd gerador-cadernos
```

**Passo 3: Crie Ambiente Virtual (Recomendado)**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Passo 4: Instale as Dependências**
```bash
pip3 install -r requirements.txt
```

**Passo 5: Execute o Programa**
```bash
python3 Criador_de_Cadernos.py
```

---

### 🐧 Linux (Ubuntu/Debian)

**Passo 1: Instale Python e Pip**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Passo 2: Clone o Repositório**
```bash
git clone https://github.com/seu-usuario/gerador-cadernos.git
cd gerador-cadernos
```

**Passo 3: Crie Ambiente Virtual**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Passo 4: Instale as Dependências**
```bash
pip install -r requirements.txt
```

**Passo 5: Execute o Programa**
```bash
python3 Criador_de_Cadernos.py
```

---

### 🐛 Solução de Problemas Comuns

#### Erro: "pip não é reconhecido"
**Solução Windows:**
```bash
python -m pip install -r requirements.txt
```

#### Erro: "ModuleNotFoundError: No module named 'PyQt5'"
**Solução:**
```bash
pip install PyQt5 numpy
```

#### Erro: "Permission denied"
**Solução Linux/Mac:**
```bash
# Opção 1: Use ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Opção 2: Instale com --user
pip install --user -r requirements.txt
```

#### Erro ao Abrir Interface Gráfica
- Certifique-se de estar em ambiente gráfico (não SSH sem X11)
- No Linux, pode ser necessário: `sudo apt install python3-pyqt5`

---

### 📦 Criando Executável (Opcional)

Para criar um arquivo executável standalone:

**Windows (.exe):**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="Gerador-Cadernos" Criador_de_Cadernos.py
```

**macOS (.app):**
```bash
pip install py2app
# Criar arquivo setup.py primeiro
python setup.py py2app
```

**Linux (AppImage):**
```bash
pip install pyinstaller
pyinstaller --onefile --windowed Criador_de_Cadernos.py
```

O executável estará na pasta `dist/`

---

# 5. Como Usar

## 🎨 Guia de Uso Completo

### Interface Principal

A interface é dividida em três seções principais:

1. **Painel de Controle (Esquerda)**
   - Seleção de tipo de padrão
   - Configurações gerais
   - Parâmetros específicos

2. **Canvas de Preview (Centro)**
   - Visualização em tempo real
   - Redimensionável
   - Mantém proporção

3. **Barra de Ações (Inferior)**
   - Botão "Gerar Preview"
   - Botão "Salvar PDF"
   - Barra de status

---

### Passo a Passo Básico

#### 1. Selecione o Tipo de Padrão
- Clique no dropdown "Tipo de Padrão"
- Escolha entre 8 opções disponíveis
- A interface se adapta automaticamente

#### 2. Configure os Parâmetros Globais

**Tamanho da Página:**
- A4 (210 x 297 mm) - Padrão
- A5 (148 x 210 mm) - Metade do A4
- A3 (297 x 420 mm) - Dobro do A4
- Carta (215.9 x 279.4 mm) - Padrão americano

**Margens:**
- Range: 0-30mm
- Padrão: 10mm
- Dica: Use 20-30mm para fichário

**Espessura da Linha:**
- Range: 0.1-2.0mm
- Padrão: 0.3mm
- Dica: 0.2mm para discreto, 0.5mm para visível

**Cor das Linhas:**
- Clique no botão colorido
- Escolha qualquer cor RGB
- Cores claras são mais discretas

#### 3. Configure Parâmetros Específicos

**Para Grade Quadriculada:**
- Tamanho do quadrado: 5-30mm
- ☑️ Destacar a cada N linhas (opcional)
- Espessura do destaque: 0.5-3.0mm

**Para Pontos:**
- Espaçamento: 5-30mm

**Para Hexagonal:**
- Tamanho do hexágono: 5-30mm

**Para Isométrica:**
- Tamanho da grade: 5-30mm

**Para Pautadas:**
- Espaçamento das linhas: 6-15mm

**Para Musicais:**
- Altura da pauta: 15-30mm

**Para Polar:**
- Círculos: 5-20
- Raios: 4-36

**Para Caligrafia:**
- Altura da linha: 10-25mm

#### 4. Visualize em Tempo Real

- As mudanças aparecem automaticamente no preview
- Redimensione a janela para ver melhor
- A proporção é mantida

#### 5. Gere o Preview Final

- Clique em "Gerar Preview"
- Aguarde o processamento (rápido)
- Verifique se está como desejado

#### 6. Exporte para PDF

- Clique em "Salvar PDF"
- Escolha o local e nome do arquivo
- Aguarde a geração (300 DPI)
- Pronto para imprimir!

---

### Atalhos e Dicas

#### 💡 Dicas de Uso

**Para Impressão:**
- Use cores claras (cinza) para economizar tinta
- Configure margens adequadas para encadernação
- Teste uma página antes de imprimir muitas

**Para Melhor Resultado:**
- Ajuste o preview antes de exportar
- Use A4 para compatibilidade universal
- Salve configurações diferentes em PDFs separados

**Para Diferentes Propósitos:**
- Matemática: Quadriculada 5mm, destacar a cada 5
- Bullet Journal: Pontos 5mm, cor cinza claro
- Música: Pautas 20mm, cor preta
- Desenho técnico: Isométrica 10mm, cor azul claro

---

### Fluxo de Trabalho Recomendado

```
1. Decida o uso (matemática, arte, música, etc.)
   ↓
2. Escolha o tipo de padrão apropriado
   ↓
3. Configure tamanho da página
   ↓
4. Ajuste margens (pense na encadernação)
   ↓
5. Defina cor e espessura
   ↓
6. Configure parâmetros específicos
   ↓
7. Visualize e ajuste se necessário
   ↓
8. Exporte para PDF
   ↓
9. Imprima ou salve para uso posterior
```

---

# 6. Parâmetros Personalizáveis

## ⚙️ Referência Completa de Parâmetros

### Parâmetros Globais

| Parâmetro | Tipo | Faixa | Padrão | Descrição |
|-----------|------|-------|--------|-----------|
| **Tipo de Padrão** | Dropdown | 8 opções | Quadriculada | Seleciona o tipo de grade |
| **Tamanho da Página** | Dropdown | A3/A4/A5/Carta | A4 | Formato da página |
| **Margens** | SpinBox | 0-30mm | 10mm | Espaço das bordas |
| **Espessura da Linha** | DoubleSpinBox | 0.1-2.0mm | 0.3mm | Grossura do traço |
| **Cor da Linha** | ColorPicker | RGB completo | #C0C0C0 | Cor personalizada |

---

### Parâmetros por Tipo de Grade

#### Grade Quadriculada

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Tamanho do quadrado | 5-30mm | 5mm | Lado do quadrado |
| Destacar a cada | 0-10 linhas | 0 | Linhas destacadas |
| Espessura destaque | 0.5-3.0mm | 1.0mm | Grossura das destacadas |

**Uso típico:**
- 5mm sem destaque: Grade fina
- 5mm com destaque a cada 5: Papel milimetrado
- 10mm sem destaque: Grade grossa

---

#### Grade de Pontos

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Espaçamento | 5-30mm | 5mm | Distância entre pontos |

**Uso típico:**
- 5mm: Bullet journal padrão
- 7-8mm: Grade mais espaçada
- 10mm: Para desenhos maiores

---

#### Grade Hexagonal

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Tamanho | 5-30mm | 10mm | Raio do hexágono |

**Uso típico:**
- 10mm: Mapas de RPG padrão
- 15-20mm: Hexágonos maiores para jogos
- 5-7mm: Miniatura ou detalhes

---

#### Grade Isométrica

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Tamanho da grade | 5-30mm | 10mm | Espaçamento entre linhas |

**Uso típico:**
- 5mm: Desenhos detalhados
- 10mm: Uso geral
- 15mm: Sketches rápidos

---

#### Linhas Pautadas

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Espaçamento | 6-15mm | 8mm | Distância entre linhas |

**Uso típico:**
- 6-7mm: Escrita pequena
- 8-9mm: Escrita padrão
- 10-12mm: Escrita grande
- 15mm: Iniciantes ou crianças

---

#### Pautas Musicais

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Altura da pauta | 15-30mm | 20mm | Altura total da pauta |

**Uso típico:**
- 15-18mm: Pautas compactas
- 20-22mm: Padrão profissional
- 25-30mm: Pautas grandes para iniciantes

---

#### Grade Polar

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Círculos | 5-20 | 10 | Número de círculos |
| Raios | 4-36 | 12 | Número de raios |

**Uso típico:**
- 10 círculos, 12 raios: Uso geral
- 15 círculos, 24 raios: Gráficos detalhados
- 8 círculos, 8 raios: Mandalas simples
- 12 círculos, 36 raios: Precisão angular

---

#### Linhas de Caligrafia

| Parâmetro | Faixa | Padrão | Descrição |
|-----------|-------|--------|-----------|
| Altura da linha | 10-25mm | 15mm | Altura total (3 linhas) |

**Uso típico:**
- 10-12mm: Lettering pequeno
- 15-18mm: Prática padrão
- 20-25mm: Lettering grande

---

### Tabelas de Referência Rápida

#### Cores Recomendadas por Uso

| Uso | Cor | Código Hex | RGB | Motivo |
|-----|-----|------------|-----|--------|
| **Discreto** | Cinza claro | #D3D3D3 | (211,211,211) | Não interfere |
| **Matemática** | Azul claro | #B0C4DE | (176,196,222) | Tradicional |
| **Arte** | Violeta claro | #E6D5FF | (230,213,255) | Inspirador |
| **Técnico** | Verde claro | #90EE90 | (144,238,144) | Contraste suave |
| **Musical** | Preto | #000000 | (0,0,0) | Padrão profissional |
| **Muito discreto** | Cinza muito claro | #E8E8E8 | (232,232,232) | Quase invisível |

---

#### Espessuras Recomendadas

| Finalidade | Espessura | Observação |
|-----------|-----------|------------|
| **Muito discreto** | 0.1-0.2mm | Linhas finas, quase invisíveis |
| **Discreto** | 0.2-0.3mm | Visível mas não dominante |
| **Padrão** | 0.3-0.5mm | Equilíbrio ideal |
| **Visível** | 0.5-0.8mm | Linhas bem marcadas |
| **Destaque** | 0.8-1.5mm | Para linhas principais |
| **Muito grosso** | 1.5-2.0mm | Uso específico |

---

#### Margens por Tipo de Encadernação

| Encadernação | Margem Esquerda | Margem Outras | Observação |
|--------------|----------------|---------------|------------|
| **Espiral** | 20-25mm | 10-15mm | Espaço para espiral |
| **Fichário 3 furos** | 30mm | 10-15mm | Espaço para furos |
| **Grampeado** | 10-15mm | 10mm | Mínimo necessário |
| **Colado** | 15-20mm | 10-15mm | Espaço para cola |
| **Sem encadernação** | 10mm | 10mm | Margem estética |

---

# 7. Exemplos Práticos

## 📚 Casos de Uso Reais

### 🎯 Categoria: Estudantes

#### Exemplo 1: Caderno de Matemática

**Configuração:**
```
Tipo: Quadriculada
Página: A4
Tamanho do quadrado: 5mm
Destacar a cada: 5 linhas
Espessura normal: 0.3mm
Espessura destaque: 1.0mm
Cor: Azul claro (#B0C4DE)
Margens: 15mm (para espiral)
```

**Para que serve:**
- Gráficos e funções
- Geometria com régua
- Cálculos organizados
- Contagem fácil com destaques

**Dica profissional:** O destaque a cada 5 linhas cria uma grade secundária que facilita muito a leitura e construção de gráficos!

---

#### Exemplo 2: Caderno de Redação

**Configuração:**
```
Tipo: Pautadas
Página: A4
Espaçamento: 8mm
Espessura: 0.3mm
Cor: Cinza (#808080)
Margens: 20mm
```

**Para que serve:**
- Redações e textos
- Anotações de aula
- Resumos organizados
- Cartas formais

**Dica profissional:** 8mm é o espaçamento ideal para escrita à mão - não muito apertado, não muito espaçado.

---

#### Exemplo 3: Caderno de Química/Física

**Configuração:**
```
Tipo: Quadriculada (superior) + Pautadas (inferior)
Opção: Criar dois PDFs e intercalar ao imprimir
Grade: 5mm sem destaque
Pautas: 8mm
Cor: Verde claro (#90EE90)
Margens: 15mm
```

**Para que serve:**
- Parte superior: Fórmulas, gráficos, diagramas
- Parte inferior: Explicações escritas
- Ideal para ciências exatas

---

### 🎨 Categoria: Artistas e Designers

#### Exemplo 4: Bullet Journal Profissional

**Configuração:**
```
Tipo: Pontos (Dot Grid)
Página: A5
Espaçamento: 5mm
Espessura: 0.5mm
Cor: Cinza claro (#D3D3D3)
Margens: 10mm
```

**Para que serve:**
- Planejamento mensal/semanal
- Habit trackers
- Desenhos e doodles
- Layouts criativos

**Dica profissional:** A5 é o tamanho perfeito para bullet journal - portátil mas com espaço suficiente!

---

#### Exemplo 5: Sketchbook Isométrico

**Configuração:**
```
Tipo: Isométrica
Página: A4 ou A3
Tamanho da grade: 10mm
Espessura: 0.2mm
Cor: Azul muito claro (#E6F3FF)
Margens: 10mm
```

**Para que serve:**
- Desenhos 3D sem perspectiva
- Design de produtos
- Arquitetura conceitual
- Game design

**Dica profissional:** Use cor bem clara para que suas linhas de desenho se destaquem sobre a grade!

---

#### Exemplo 6: Mandala e Arte Circular

**Configuração:**
```
Tipo: Polar
Página: A4
Círculos: 12
Raios: 24
Espessura: 0.2mm
Cor: Violeta claro (#E6D5FF)
Margens: 20mm
```

**Para que serve:**
- Mandalas simétricas
- Arte geométrica
- Designs radiais
- Meditação artística

**Dica profissional:** 24 raios divide o círculo em ângulos de 15°, perfeito para simetria!

---

### 🎼 Categoria: Músicos

#### Exemplo 7: Caderno de Composição Musical

**Configuração:**
```
Tipo: Musicais
Página: A4 (orientação paisagem recomendada)
Altura da pauta: 20mm
Espessura: 0.4mm
Cor: Preto (#000000)
Margens: 15mm
```

**Para que serve:**
- Composições originais
- Transcrições de músicas
- Arranjos e harmonizações
- Exercícios de teoria musical

**Dica profissional:** Imprima em orientação paisagem (landscape) para ter mais compassos por linha!

---

#### Exemplo 8: Caderno de Teoria Musical

**Configuração:**
```
Opção 1: Musicais (20mm)
Opção 2: Pautadas (8mm)
Alternativa: Imprima ambos e intercale
```

**Para que serve:**
- Anotações teóricas com exemplos
- Exercícios de harmonia
- Análise de partituras
- Estudos de escalas e acordes

---

### 🏗️ Categoria: Engenheiros e Arquitetos

#### Exemplo 9: Papel Milimetrado Profissional

**Configuração:**
```
Tipo: Quadriculada
Página: A3
Tamanho do quadrado: 5mm
Destacar a cada: 10 linhas
Espessura normal: 0.2mm
Espessura destaque: 0.8mm
Cor: Verde (#90EE90)
Margens: 20mm
```

**Para que serve:**
- Desenhos técnicos
- Gráficos de engenharia
- Plantas baixas
- Estudos de escala

**Dica profissional:** A3 oferece espaço para desenhos mais complexos. Use escala 1:100 ou 1:50.

---

#### Exemplo 10: Grade Isométrica para CAD Manual

**Configuração:**
```
Tipo: Isométrica
Página: A3
Tamanho da grade: 5mm
Espessura: 0.15mm
Cor: Azul (#ADD8E6)
Margens: 15mm
```

**Para que serve:**
- Perspectiva isométrica manual
- Projetos mecânicos
- Design de peças
- Estudos volumétricos

---

### 🎮 Categoria: RPG e Jogos

#### Exemplo 11: Mapa Hexagonal para D&D

**Configuração:**
```
Tipo: Hexagonal
Página: A3
Tamanho do hexágono: 15mm
Espessura: 0.3mm
Cor: Marrom claro (#D2B48C)
Margens: 10mm
```

**Para que serve:**
- Mapas de mundo
- Batalhas táticas
- Dungeon crawling
- Estratégia hexagonal

**Dica profissional:** 15mm é aproximadamente 0.6 polegadas, compatível com miniaturas padrão de 25-28mm!

---

#### Exemplo 12: Grid de Combate Quadriculado

**Configuração:**
```
Tipo: Quadriculada
Página: A3
Tamanho do quadrado: 25mm (1 polegada)
Espessura: 0.5mm
Cor: Preto (#000000)
Margens: 10mm
```

**Para que serve:**
- D&D 5e
- Pathfinder
- Wargames
- Combate tático com miniaturas

**Dica profissional:** 25mm (1") é o padrão para miniaturas de RPG!

---

### ✍️ Categoria: Caligrafia e Lettering

#### Exemplo 13: Prática de Brush Lettering

**Configuração:**
```
Tipo: Caligrafia
Página: A4
Altura da linha: 15mm
Espessura: 0.3mm
Cor: Azul claro (#87CEEB)
Margens: 20mm
```

**Para que serve:**
- Prática de brush pen
- Lettering moderno
- Caligrafia decorativa
- Exercícios de proporção

**Dica profissional:** As três linhas guiam ascendentes, corpo e descendentes das letras!

---

#### Exemplo 14: Headers e Títulos Grandes

**Configuração:**
```
Tipo: Caligrafia
Página: A4
Altura da linha: 25mm
Espessura: 0.2mm
Cor: Cinza muito claro (#E8E8E8)
Margens: 15mm
```

**Para que serve:**
- Títulos decorativos
- Posters
- Banners
- Arte de parede

---

### 📊 Categoria: Gráficos e Ciência

#### Exemplo 15: Gráficos Polares Científicos

**Configuração:**
```
Tipo: Polar
Página: A4
Círculos: 10
Raios: 36 (a cada 10°)
Espessura: 0.3mm
Cor: Verde (#90EE90)
Margens: 30mm
```

**Para que serve:**
- Diagramas de radiação
- Gráficos estatísticos circulares
- Análise de frequência
- Patterns de áudio

**Dica profissional:** 36 raios = 10° cada, 72 raios = 5° cada para maior precisão!

---

### 🎨 Projetos Especiais

#### Exemplo 16: Caderno Misto Multi-Propósito

**Como criar:**
1. Crie PDF de pautadas (30 páginas)
2. Crie PDF de quadriculadas (30 páginas)
3. Crie PDF de pontos (20 páginas)
4. Imprima intercalando seções
5. Encaderne tudo junto

**Seções sugeridas:**
- Parte 1: Pautadas → Anotações gerais
- Parte 2: Quadriculadas → Cálculos e gráficos
- Parte 3: Pontos → Rascunhos e criatividade
- Parte 4: Específico para seu uso

---

## 💡 Dicas Avançadas

### Cores por Contexto

**Para Economia de Tinta:**
```
Cor: #E8E8E8 (cinza muito claro)
Espessura: 0.2mm
Resultado: Visível mas consome pouca tinta
```

**Para Máximo Contraste:**
```
Cor: #000000 (preto)
Espessura: 0.5mm
Resultado: Linhas bem visíveis e definidas
```

**Para Uso Profissional:**
```
Cor: #808080 (cinza médio)
Espessura: 0.3mm
Resultado: Aparência profissional e equilibrada
```

---

### Configurações por Idade

**Crianças (6-10 anos):**
- Espaçamento: Maior (10-15mm para pautadas)
- Cor: Mais escura para facilitar visualização
- Tipo: Pautadas simples ou quadriculada grande

**Adolescentes (11-17 anos):**
- Espaçamento: Padrão (8mm para pautadas)
- Cor: Personalizada conforme preferência
- Tipo: Variado conforme matéria

**Adultos:**
- Espaçamento: Personalizado conforme uso
- Cor: Tons profissionais ou criativos
- Tipo: Específico para necessidade

---

### Checklist Antes de Imprimir

- [ ] Tamanho da página correto para sua impressora
- [ ] Margens adequadas para encadernação
- [ ] Cor visível mas não dominante
- [ ] Preview verificado e aprovado
- [ ] Quantidade de páginas planejada
- [ ] Tipo de papel escolhido (75g, 90g, 120g)
- [ ] Configurações da impressora ajustadas
- [ ] Teste impresso (1 página primeiro!)
- [ ] Orçamento de tinta considerado

---

# 8. Estrutura do Código

## 🏗️ Arquitetura e Organização

### Visão Geral

```
Criador_de_Cadernos.py (674 linhas)
│
├── 📦 Imports e Constantes (linhas 1-27)
│   ├── PyQt5 (GUI framework)
│   ├── numpy (cálculos matemáticos)
│   └── MM_TO_PX = 3.779528 (conversão)
│
├── 🎨 PreviewCanvas (linhas 29-51)
│   └── Widget para preview
│
├── 🔧 NotebookGenerator (linhas 53-242)
│   └── Métodos de desenho
│
├── 🖥️ NotebookGeneratorGUI (linhas 244-663)
│   └── Interface principal
│
└── 🚀 main() (linhas 666-674)
    └── Inicialização
```

---

### Constantes e Conversões

```python
# Conversão: 1mm = 3.779528 pixels em 96 DPI
MM_TO_PX = 3.779528
```

**Por que este valor?**
- Monitores usam 96 DPI como padrão
- 1 polegada = 25.4mm
- 96 pixels / 25.4mm ≈ 3.779528 pixels/mm

**Uso:**
```python
width_px = width_mm * MM_TO_PX  # Converte mm para pixels
margin_px = margin_mm * MM_TO_PX
```

---

### Classe PreviewCanvas

```python
class PreviewCanvas(QLabel):
    """Canvas para mostrar o preview do caderno"""
```

**Responsabilidades:**
- Exibir pixmap escalado
- Manter proporção ao redimensionar
- Atualizar preview em tempo real

**Métodos principais:**

#### `__init__()`
```python
def __init__(self):
    super().__init__()
    self.setAlignment(Qt.AlignCenter)
    self.setStyleSheet("QLabel { background-color: white; border: 1px solid #ccc; }")
    self.setMinimumSize(600, 800)
    self.current_pixmap = None
```
- Inicializa o widget
- Define aparência (fundo branco, borda cinza)
- Tamanho mínimo 600x800px

#### `set_pattern(pixmap)`
```python
def set_pattern(self, pixmap):
    """Define o padrão a ser exibido"""
    self.current_pixmap = pixmap
    scaled = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
    self.setPixmap(scaled)
```
- Armazena pixmap original
- Escala mantendo proporção
- Usa transformação suave (antialiasing)

#### `resizeEvent(event)`
```python
def resizeEvent(self, event):
    """Reescala quando redimensionar a janela"""
    super().resizeEvent(event)
    if self.current_pixmap:
        scaled = self.current_pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setPixmap(scaled)
```
- Chamado automaticamente ao redimensionar
- Reescala o pixmap para nova janela

---

### Classe NotebookGenerator

```python
class NotebookGenerator:
    """Classe para gerar diferentes tipos de padrões de caderno"""
```

**Responsabilidades:**
- Desenhar todos os tipos de grade
- Cálculos geométricos precisos
- Usar QPainter para renderização

**Estrutura:**
- Todos métodos são `@staticmethod`
- Não precisa instanciar a classe
- Funciona como namespace de funções

---

#### Método: `draw_grid()`

```python
@staticmethod
def draw_grid(painter, width, height, square_size, line_width, color, 
              margin, highlight_every=0, highlight_width=0):
    """Desenha grade quadriculada"""
```

**Algoritmo:**
1. Desenha linhas verticais da esquerda para direita
2. Desenha linhas horizontais de cima para baixo
3. Destaca linhas a cada N posições (opcional)

**Pseudocódigo:**
```
PARA cada posição x de margem até largura-margem:
    SE é linha de destaque:
        usar linha grossa
    SENÃO:
        usar linha fina
    desenhar linha vertical

PARA cada posição y de margem até altura-margem:
    SE é linha de destaque:
        usar linha grossa
    SENÃO:
        usar linha fina
    desenhar linha horizontal
```

---

#### Método: `draw_dots()`

```python
@staticmethod
def draw_dots(painter, width, height, dot_spacing, dot_size, color, margin):
    """Desenha grade de pontos (dot grid)"""
```

**Algoritmo:**
1. Itera por linhas (y)
2. Para cada linha, itera por colunas (x)
3. Desenha ponto em cada posição

**Pseudocódigo:**
```
PARA cada y de margem até altura-margem:
    PARA cada x de margem até largura-margem:
        desenhar ponto em (x, y)
        x += espaçamento
    y += espaçamento
```

---

#### Método: `draw_hexagons()`

```python
@staticmethod
def draw_hexagons(painter, width, height, hex_size, line_width, color, margin):
    """Desenha grade hexagonal"""
```

**Geometria do Hexágono:**
```python
h = hex_size * math.sqrt(3) / 2  # Altura
w = hex_size * 1.5                # Largura entre centros
```

**Matemática:**
- Hexágono regular tem ângulos de 60°
- Altura = lado × √3/2
- Distância entre centros = 1.5 × lado
- Linhas ímpares têm offset de w/3

**Algoritmo:**
```
PARA cada linha (com offset alternado):
    PARA cada coluna:
        calcular centro do hexágono
        PARA cada vértice (0 a 5):
            calcular posição usando trigonometria
        desenhar 6 lados conectando vértices
```

---

#### Método: `draw_isometric()`

```python
@staticmethod
def draw_isometric(painter, width, height, grid_size, line_width, color, margin):
    """Desenha grade isométrica (triângulos)"""
```

**Geometria Isométrica:**
- Três conjuntos de linhas paralelas
- Ângulos de 30°, 90° (horizontal), -30°
- Altura triangular = lado × √3/2

**Três Conjuntos de Linhas:**
1. **Linhas inclinadas +30°** (direita)
2. **Linhas horizontais**
3. **Linhas inclinadas -30°** (esquerda)

**Cálculos:**
```python
h = grid_size * math.sqrt(3) / 2
# Inclinação: rise/run = tan(30°) = 1/√3
```

---

#### Método: `draw_ruled()`

```python
@staticmethod
def draw_ruled(painter, width, height, line_spacing, line_width, color, margin):
    """Desenha linhas pautadas (ruled)"""
```

**Algoritmo:**
1. Desenha linhas horizontais espaçadas
2. Adiciona margem vertical vermelha (opcional)

**Detalhes:**
```python
# Linhas horizontais
y = margin + line_spacing
while y <= height - margin:
    desenhar_linha_horizontal(y)
    y += line_spacing

# Margem esquerda (vermelha clara)
margin_line = margin + line_spacing * 2
desenhar_linha_vertical(margin_line, cor_vermelha_transparente)
```

---

#### Método: `draw_music()`

```python
@staticmethod
def draw_music(painter, width, height, staff_height, line_width, color, margin):
    """Desenha pautas musicais"""
```

**Estrutura de uma Pauta:**
- 5 linhas horizontais
- Espaçamento = altura_pauta / 4
- Múltiplas pautas separadas

**Algoritmo:**
```
y = margem + altura_pauta
ENQUANTO y < altura - margem:
    PARA cada linha (0 a 4):
        linha_y = y + i * (altura_pauta / 4)
        desenhar linha horizontal
    y += altura_pauta * 2  # Espaço entre pautas
```

---

#### Método: `draw_polar()`

```python
@staticmethod
def draw_polar(painter, width, height, num_circles, num_rays, line_width, color, margin):
    """Desenha grade polar/circular"""
```

**Componentes:**
1. **Círculos concêntricos** - raios incrementais
2. **Raios** - linhas do centro para fora

**Cálculos:**
```python
center_x = width / 2
center_y = height / 2
max_radius = min(width, height) / 2 - margin
radius_step = max_radius / num_circles
angle_step = 2 * math.pi / num_rays
```

**Algoritmo:**
```
# Círculos
PARA i de 1 até num_circles:
    raio = i * passo_raio
    desenhar_circulo(centro, raio)

# Raios
PARA i de 0 até num_rays:
    angulo = i * passo_angulo
    x_final = centro_x + max_raio * cos(angulo)
    y_final = centro_y + max_raio * sin(angulo)
    desenhar_linha(centro, ponto_final)
```

---

#### Método: `draw_calligraphy()`

```python
@staticmethod
def draw_calligraphy(painter, width, height, line_height, line_width, color, margin):
    """Desenha linhas de caligrafia com 3 guias"""
```

**Estrutura:**
- **Linha superior** (ascendentes - k, l, h)
- **Linha do meio** (corpo - a, e, o)
- **Linha de base** (base de todas letras)
- **Linha inferior** (descendentes - g, p, q)

**Proporções:**
```python
ascender_line = y
x_height_line = y + line_height * 0.4
baseline = y + line_height * 0.7
descender_line = y + line_height
```

**Algoritmo:**
```
y = margem
ENQUANTO y < altura - margem:
    desenhar linha superior (ascendente)
    desenhar linha do meio (x-height)
    desenhar linha de base (baseline) - MAIS GROSSA
    desenhar linha inferior (descendente)
    y += line_height + espaçamento
```

---

### Classe NotebookGeneratorGUI

```python
class NotebookGeneratorGUI(QMainWindow):
    """Janela principal da aplicação"""
```

**Responsabilidades:**
- Gerenciar interface gráfica
- Conectar eventos aos handlers
- Gerar preview em tempo real
- Exportar para PDF

---

#### Método: `__init__()`

```python
def __init__(self):
    super().__init__()
    self.setWindowTitle("📓 Gerador de Cadernos Personalizados")
    self.setGeometry(100, 100, 1400, 900)
    self.current_color = QColor(192, 192, 192)
    self.init_ui()
    self.generate_preview()
```

**Inicialização:**
1. Define título da janela
2. Define tamanho (1400x900)
3. Cor padrão: cinza claro
4. Cria interface
5. Gera preview inicial

---

#### Método: `init_ui()`

```python
def init_ui(self):
    """Inicializa a interface do usuário"""
```

**Estrutura da Interface:**

```
┌─────────────────────────────────────────┐
│           JANELA PRINCIPAL              │
├──────────┬──────────────────────────────┤
│          │                              │
│ PAINEL   │       CANVAS PREVIEW         │
│   DE     │                              │
│ CONTROLE │      (Visualização)          │
│          │                              │
│ (QScroll)│                              │
├──────────┴──────────────────────────────┤
│  [Gerar Preview] [Salvar PDF]   Status  │
└─────────────────────────────────────────┘
```

**Componentes do Painel de Controle:**

1. **Grupo: Configurações Gerais**
   - Tipo de Padrão (Dropdown)
   - Tamanho da Página (Dropdown)
   - Margens (SpinBox)
   - Espessura da Linha (DoubleSpinBox)
   - Cor das Linhas (ColorButton)

2. **Grupo: Parâmetros do Padrão**
   - Tamanho/Espaçamento (dinâmico)
   - Círculos e Raios (para polar)
   - Destaque (para quadriculada)

**Código simplificado:**
```python
# Layout principal
main_layout = QHBoxLayout()

# Painel esquerdo (controles)
control_panel = self.create_control_panel()
scroll = QScrollArea()
scroll.setWidget(control_panel)

# Canvas central (preview)
self.preview_canvas = PreviewCanvas()

# Adiciona ao layout
main_layout.addWidget(scroll, 1)      # 30% largura
main_layout.addWidget(self.preview_canvas, 2)  # 70% largura
```

---

#### Método: `update_params_visibility()`

```python
def update_params_visibility(self):
    """Atualiza visibilidade dos parâmetros baseado no tipo"""
```

**Lógica:**
```python
pattern_type = self.pattern_combo.currentText()

# Esconde todos
esconder_todos_parametros()

# Mostra apenas relevantes
if "Quadriculada" in pattern_type:
    mostrar(tamanho_quadrado)
    mostrar(opcoes_destaque)
elif "Pontos" in pattern_type:
    mostrar(espacamento_pontos)
elif "Polar" in pattern_type:
    mostrar(numero_circulos)
    mostrar(numero_raios)
# ... etc
```

**Benefício:**
- Interface limpa e focada
- Mostra apenas opções relevantes
- Evita confusão do usuário

---

#### Método: `choose_color()`

```python
def choose_color(self):
    """Abre diálogo para escolher cor"""
    color = QColorDialog.getColor(self.current_color, self)
    if color.isValid():
        self.current_color = color
        self.update_color_button()
```

**Fluxo:**
1. Abre diálogo nativo do sistema
2. Usuário escolhe cor
3. Se válida, atualiza cor atual
4. Atualiza aparência do botão

---

#### Método: `get_page_dimensions()`

```python
def get_page_dimensions(self):
    """Retorna dimensões da página em mm"""
    page_type = self.page_size.currentText()
    if page_type == "A4":
        return 210, 297
    elif page_type == "A5":
        return 148, 210
    # ... etc
```

**Dimensões Padrão:**
- A4: 210 × 297 mm
- A5: 148 × 210 mm (metade do A4)
- A3: 297 × 420 mm (dobro do A4)
- Carta: 215.9 × 279.4 mm (padrão EUA)

---

#### Método: `draw_pattern()`

```python
def draw_pattern(self, painter, width_mm, height_mm):
    """Desenha o padrão selecionado"""
```

**Fluxo:**
1. Obtém tipo de padrão
2. Converte dimensões para pixels
3. Obtém parâmetros configurados
4. Chama método apropriado do NotebookGenerator

**Exemplo:**
```python
pattern_type = self.pattern_combo.currentText()

# Converte mm → px
width = width_mm * MM_TO_PX
height = height_mm * MM_TO_PX
margin = self.margin_spin.value() * MM_TO_PX

gen = NotebookGenerator()

if "Quadriculada" in pattern_type:
    gen.draw_grid(painter, width, height, ...)
elif "Pontos" in pattern_type:
    gen.draw_dots(painter, width, height, ...)
# ... etc
```

---

#### Método: `generate_preview()`

```python
def generate_preview(self):
    """Gera o preview do caderno"""
```

**Processo:**
1. Obtém dimensões da página
2. Cria QPixmap em alta resolução (2x para qualidade)
3. Cria QPainter com antialiasing
4. Escala 2x para melhor renderização
5. Chama draw_pattern()
6. Exibe no canvas

**Por que 2x?**
```python
width_px = int(width_mm * MM_TO_PX * 2)  # 2x para melhor qualidade
```
- Renderiza em resolução maior
- Depois escala para tamanho do widget
- Resultado: preview mais suave e nítido

---

#### Método: `export_pdf()`

```python
def export_pdf(self):
    """Exporta o caderno para PDF"""
```

**Processo:**
1. Abre diálogo "Salvar Como"
2. Cria QPdfWriter
3. Define tamanho da página
4. Define resolução (300 DPI)
5. Cria QPainter
6. Desenha o padrão
7. Salva arquivo

**Código simplificado:**
```python
filename = QFileDialog.getSaveFileName(...)

writer = QPdfWriter(filename)
writer.setPageSize(QPageSize(QPageSize.A4))
writer.setResolution(300)  # 300 DPI = qualidade profissional

painter = QPainter(writer)
painter.setRenderHint(QPainter.Antialiasing)

self.draw_pattern(painter, width_mm, height_mm)

painter.end()  # Finaliza e salva
```

---

### Função `main()`

```python
def main():
    app = QApplication(sys.argv)
    window = NotebookGeneratorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```

**Explicação:**
- `QApplication(sys.argv)`: Cria aplicação Qt
- `NotebookGeneratorGUI()`: Instancia janela
- `window.show()`: Exibe janela
- `app.exec_()`: Loop de eventos (aguarda interações)
- `sys.exit()`: Encerra corretamente

---

## 🔬 Detalhes Técnicos Avançados

### Conversão de Unidades

**Preview (96 DPI):**
```python
MM_TO_PX = 3.779528
width_px = width_mm * MM_TO_PX
```

**PDF (300 DPI):**
```python
# O QPdfWriter usa internamente 1200 DPI
# mas aceita especificar 300 DPI para qualidade
writer.setResolution(300)
```

**Relação:**
- 96 DPI → Monitor (preview)
- 300 DPI → Impressão (PDF)
- 1200 DPI → Interno do Qt (vetorial)

---

### Qualidade de Renderização

**Antialiasing:**
```python
painter.setRenderHint(QPainter.Antialiasing)
```
- Suaviza bordas
- Melhor aparência
- Essencial para linhas diagonais

**Transformação Suave:**
```python
scaled = pixmap.scaled(
    size, 
    Qt.KeepAspectRatio, 
    Qt.SmoothTransformation  # ← Importante!
)
```
- Evita pixelização
- Melhor interpolação
- Preview mais bonito

---

### Otimizações

**1. Preview em 2x:**
```python
width_px = int(width_mm * MM_TO_PX * 2)
painter.scale(2, 2)
```
Renderiza maior, depois escala = melhor qualidade

**2. Métodos Estáticos:**
```python
@staticmethod
def draw_grid(...):
```
Não precisa instância = mais rápido

**3. Cálculos Fora do Loop:**
```python
h = hex_size * math.sqrt(3) / 2  # Calcula uma vez
while ...:
    usar h  # Não recalcula
```

---

## 📊 Fluxograma da Aplicação

```
┌─────────────┐
│   Início    │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Cria Aplicação  │
│    (QApp)       │
└──────┬──────────┘
       │
       ▼
┌──────────────────┐
│  Cria GUI        │
│  init_ui()       │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Gera Preview     │
│  Inicial         │
└──────┬───────────┘
       │
       ▼
┌──────────────────────────┐
│   Loop de Eventos        │
│ ┌──────────────────────┐ │
│ │ Usuário Interage     │ │
│ └──────┬───────────────┘ │
│        │                 │
│        ▼                 │
│ ┌──────────────────────┐ │
│ │ Atualiza Parâmetros  │ │
│ └──────┬───────────────┘ │
│        │                 │
│        ▼                 │
│ ┌──────────────────────┐ │
│ │ Gera Preview         │ │
│ │ generate_preview()   │ │
│ └──────┬───────────────┘ │
│        │                 │
│        ▼                 │
│ ┌──────────────────────┐ │
│ │ Exibe no Canvas      │ │
│ └──────────────────────┘ │
│        │                 │
│        └─────────────────┤
│                          │
│ Usuário clica "Salvar"? │
│        │                 │
│        ▼                 │
│ ┌──────────────────────┐ │
│ │ Export PDF           │ │
│ │ export_pdf()         │ │
│ └──────────────────────┘ │
│        │                 │
│        └─────────────────┤
└──────────────────────────┘
       │
       ▼
┌──────────────┐
│  Encerra     │
└──────────────┘
```

---

## 🧪 Como o Código Funciona Internamente

### Exemplo: Gerando Grade Quadriculada

**1. Usuário seleciona "Quadriculada"**
```python
# Signal emitido pelo QComboBox
pattern_combo.currentTextChanged.connect(
    self.update_params_visibility
)
```

**2. Interface atualiza**
```python
def update_params_visibility(self):
    if "Quadriculada" in pattern_type:
        self.size_label.show()
        self.size_spin.show()
        self.highlight_check.show()
```

**3. Usuário clica "Gerar Preview"**
```python
self.preview_btn.clicked.connect(self.generate_preview)
```

**4. Preview é gerado**
```python
def generate_preview(self):
    # 1. Cria imagem
    pixmap = QPixmap(width_px, height_px)
    pixmap.fill(Qt.white)
    
    # 2. Cria painter
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # 3. Desenha padrão
    self.draw_pattern(painter, width_mm, height_mm)
    
    # 4. Exibe
    self.preview_canvas.set_pattern(pixmap)
```

**5. Padrão é desenhado**
```python
def draw_pattern(self, painter, width_mm, height_mm):
    gen = NotebookGenerator()
    gen.draw_grid(
        painter, width, height,
        size, thickness, color, margin,
        highlight_every, highlight_width
    )
```

**6. Grade é renderizada**
```python
def draw_grid(painter, width, height, ...):
    # Linhas verticais
    x = margin
    while x <= width - margin:
        painter.drawLine(x, margin, x, height-margin)
        x += square_size
    
    # Linhas horizontais
    y = margin
    while y <= height - margin:
        painter.drawLine(margin, y, width-margin, y)
        y += square_size
```

**Resultado:** Grade quadriculada aparece no canvas!

---

# 9. Guia de Contribuição

## 🤝 Como Contribuir

### Código de Conduta

#### Nossos Padrões

**Comportamentos Esperados:**
- ✅ Usar linguagem acolhedora e inclusiva
- ✅ Respeitar diferentes pontos de vista
- ✅ Aceitar críticas construtivas
- ✅ Focar no melhor para a comunidade
- ✅ Mostrar empatia

**Comportamentos Inaceitáveis:**
- ❌ Linguagem ofensiva ou discriminatória
- ❌ Assédio de qualquer tipo
- ❌ Publicar informações privadas
- ❌ Conduta não profissional

---

### Tipos de Contribuição

#### 1. 🐛 Reportando Bugs

**Antes de reportar:**
- [ ] Verifique se já não foi reportado
- [ ] Teste na versão mais recente
- [ ] Colete informações do ambiente

**Template de Bug:**
```markdown
**Descrição:**
Descrição clara do problema

**Passos para Reproduzir:**
1. Vá para '...'
2. Clique em '...'
3. Veja o erro

**Esperado:**
O que deveria acontecer

**Atual:**
O que está acontecendo

**Ambiente:**
- OS: Windows 10
- Python: 3.9.7
- PyQt5: 5.15.6

**Screenshots:**
[Se aplicável]
```

---

#### 2. 💡 Sugerindo Funcionalidades

**Template de Feature Request:**
```markdown
**Problema que Resolve:**
Explicação da necessidade

**Solução Proposta:**
Como deveria funcionar

**Alternativas:**
Outras abordagens consideradas

**Contexto:**
Mockups, exemplos, referências
```

---

#### 3. 🔧 Contribuindo com Código

**Setup do Ambiente:**

```bash
# 1. Fork o repositório

# 2. Clone seu fork
git clone https://github.com/seu-usuario/gerador-cadernos.git
cd gerador-cadernos

# 3. Adicione upstream
git remote add upstream https://github.com/original/gerador-cadernos.git

# 4. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 5. Instale dependências
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Se existir
```

---

### Padrões de Código

#### Python Style Guide (PEP 8)

**✅ BOM:**
```python
def draw_pattern(self, painter, width, height):
    """Desenha o padrão selecionado"""
    margin = self.margin_spin.value() * MM_TO_PX
    return result
```

**❌ RUIM:**
```python
def drawPattern(self,painter,width,height):
    margin=self.margin_spin.value()*MM_TO_PX
    return result
```

---

#### Nomenclatura

| Tipo | Convenção | Exemplo |
|------|-----------|---------|
| Classes | PascalCase | `NotebookGenerator` |
| Funções | snake_case | `draw_pattern()` |
| Variáveis | snake_case | `line_width` |
| Constantes | UPPER_CASE | `MM_TO_PX` |
| Privados | _prefixo | `_internal()` |

---

#### Documentação

**Docstrings:**
```python
def draw_grid(painter, width, height, square_size):
    """
    Desenha grade quadriculada.
    
    Args:
        painter (QPainter): Objeto painter do Qt
        width (float): Largura em pixels
        height (float): Altura em pixels
        square_size (float): Tamanho do quadrado
    
    Returns:
        None
    """
    pass
```

**Comentários:**
```python
# ✅ BOM - Explica o PORQUÊ
# Convertemos para pixels porque o QPainter usa pixels
width_px = width_mm * MM_TO_PX

# ❌ RUIM - Explica o QUÊ (óbvio)
# Multiplica width_mm por MM_TO_PX
width_px = width_mm * MM_TO_PX
```

---

### Processo de Pull Request

#### Antes de Submeter

- [ ] Código segue PEP 8
- [ ] Testou localmente
- [ ] Documentação atualizada
- [ ] Commits bem descritos

#### Criando a Branch

```bash
# Atualize sua main
git checkout main
git pull upstream main

# Crie nova branch
git checkout -b feature/nome-da-funcionalidade
```

**Nomenclatura:**
- `feature/` - Novas funcionalidades
- `fix/` - Correções
- `docs/` - Documentação
- `refactor/` - Refatorações

**Exemplos:**
```
feature/grade-triangular
fix/exportacao-pdf-erro
docs/atualizar-readme
refactor/otimizar-desenho
```

---

#### Commits

**Convenção (Conventional Commits):**
```
<tipo>(<escopo>): <descrição>

[corpo opcional]

[rodapé opcional]
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Manutenção

**Exemplos:**
```bash
feat(grid): adiciona grade triangular
fix(pdf): corrige exportação A3
docs(readme): atualiza instalação
refactor(canvas): otimiza renderização
test(generator): adiciona testes hexágonos
chore(deps): atualiza PyQt5
```

---

#### Submetendo PR

```bash
# 1. Push para seu fork
git push origin feature/sua-branch

# 2. Abra PR no GitHub

# 3. Preencha template
```

**Template de PR:**
```markdown
## Descrição
Descrição clara das mudanças

## Tipo
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Breaking change
- [ ] Documentação

## Como Testar
1. Passos para testar
2. ...

## Checklist
- [ ] Segue style guide
- [ ] Testado localmente
- [ ] Docs atualizadas
- [ ] Commits bem descritos

## Screenshots
[Se aplicável]

## Issues
Fixes #123
```

---

### Ferramentas Recomendadas

**Editores:**
- VS Code
- PyCharm
- Sublime Text

**Linters:**
- pylint
- flake8
- black (formatter)

**Type Checkers:**
- mypy

**Instalação:**
```bash
pip install pylint flake8 black mypy
```

**Uso:**
```bash
# Linter
pylint Criador_de_Cadernos.py

# Formatter
black Criador_de_Cadernos.py

# Type check
mypy Criador_de_Cadernos.py
```

---

# 10. Changelog

## 📝 Histórico de Versões

### [1.0.0] - 2025-10-20

#### 🎉 Lançamento Inicial

**✨ Adicionado:**

**8 Tipos de Grade:**
- Grade Quadriculada com destaque opcional
- Grade de Pontos (Dot Grid)
- Grade Hexagonal
- Grade Isométrica
- Linhas Pautadas (Ruled)
- Pautas Musicais
- Grade Polar/Circular
- Linhas de Caligrafia

**Funcionalidades:**
- Preview em tempo real
- Exportação PDF 300 DPI
- Interface PyQt5
- Personalização de cores
- Ajuste de espessura (0.1-2.0mm)
- Margens configuráveis (0-30mm)
- Múltiplos tamanhos (A3, A4, A5, Carta)

**Parâmetros:**
- Tamanho de elementos (5-30mm)
- Círculos e raios para polar
- Altura de pautas
- Espaçamento de linhas
- Linhas de destaque

**Documentação:**
- README completo
- Guia de instalação
- Exemplos práticos
- Guia de contribuição
- Licença MIT

**🔧 Técnico:**
- Conversão precisa mm→px
- Antialiasing
- Cálculos geométricos
- Canvas redimensionável
- Validação em tempo real

---

### [Não Lançado]

#### Planejado para v2.0

**Em Consideração:**
- [ ] Grade triangular
- [ ] Grade logarítmica
- [ ] Múltiplas páginas por PDF
- [ ] Salvar presets
- [ ] Export PNG/SVG
- [ ] Templates prontos
- [ ] Modo escuro
- [ ] Internacionalização
- [ ] Atalhos de teclado
- [ ] Histórico de configs

**Em Avaliação:**
- [ ] Versão web
- [ ] App móvel
- [ ] CLI tool
- [ ] Plugin editores
- [ ] Cloud sync
- [ ] Marketplace templates

---

## Versionamento Semântico

### Formato: MAJOR.MINOR.PATCH

- **MAJOR**: Quebra compatibilidade
- **MINOR**: Nova funcionalidade compatível
- **PATCH**: Correção compatível

### Exemplos

- `1.0.0` → `1.0.1`: Bug fix
- `1.0.0` → `1.1.0`: Nova funcionalidade
- `1.0.0` → `2.0.0`: Breaking change

---

# 11. Licença

## 📝 MIT License

```
MIT License

Copyright (c) 2025 Gerador de Cadernos Personalizados

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

### O que Significa?

**Você PODE:**
- ✅ Usar comercialmente
- ✅ Modificar o código
- ✅ Distribuir
- ✅ Uso privado

**Você DEVE:**
- ⚠️ Incluir a licença
- ⚠️ Incluir o copyright

**Você NÃO PODE:**
- ❌ Responsabilizar os autores

---

# 12. Recursos Adicionais

## 📚 Links Úteis

### Documentação Oficial

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [Python PEP 8](https://pep8.org/)
- [Git Flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

### Tutoriais

**PyQt5:**
- [PyQt5 Tutorial - Real Python](https://realpython.com/python-pyqt-gui-calculator/)
- [PyQt5 Official Tutorial](https://doc.qt.io/qt-5/qtwidgets-tutorials-gettingstarted-example.html)

**Python:**
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

---

### Comunidades

- [r/Python](https://reddit.com/r/Python)
- [r/learnpython](https://reddit.com/r/learnpython)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pyqt5)
- [Python Discord](https://pythondiscord.com/)

---

### Ferramentas

**IDEs:**
- [VS Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Sublime Text](https://www.sublimetext.com/)

**Design:**
- [Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html)
- [Figma](https://www.figma.com/) (mockups)

**Version Control:**
- [Git](https://git-scm.com/)
- [GitHub Desktop](https://desktop.github.com/)
- [GitKraken](https://www.gitkraken.com/)

---

## 🎓 Aprenda Mais

### Python

**Básico:**
- Variáveis e tipos
- Estruturas de controle
- Funções
- Orientação a objetos

**Avançado:**
- Decorators
- Context managers
- Generators
- Async/await

### PyQt5

**Básico:**
- Widgets
- Layouts
- Signals & Slots
- Event handling

**Avançado:**
- Custom widgets
- Graphics View Framework
- Model/View programming
- Threading

### Git

**Básico:**
- clone, add, commit, push
- branches
- pull requests

**Avançado:**
- rebase
- cherry-pick
- submodules

---

## 💬 Suporte

### Precisa de Ajuda?

**Documentação:**
- 📖 [README.md](https://github.com/seu-usuario/gerador-cadernos/blob/main/README.md)
- 📖 [Wiki](https://github.com/seu-usuario/gerador-cadernos/wiki)

**Comunidade:**
- 💬 [Discussões](https://github.com/seu-usuario/gerador-cadernos/discussions)
- 🐛 [Issues](https://github.com/seu-usuario/gerador-cadernos/issues)

**Contato:**
- 📧 Email: seu-email@exemplo.com
- 💼 LinkedIn: [Seu Perfil](https://linkedin.com/in/seu-perfil)
- 🐦 Twitter: [@seu_usuario](https://twitter.com/seu_usuario)

---

## 🗺️ Roadmap

### Versão 2.0 (Planejada)

**Q1 2026:**
- [ ] Múltiplas páginas por PDF
- [ ] Templates pré-configurados
- [ ] Salvar/carregar presets
- [ ] Export PNG/SVG

**Q2 2026:**
- [ ] Modo escuro
- [ ] Internacionalização (EN, ES)
- [ ] Atalhos de teclado
- [ ] Undo/Redo

**Q3 2026:**
- [ ] Grade triangular
- [ ] Grade logarítmica
- [ ] Integração impressão
- [ ] Batch processing

### Versão 3.0 (Futuro)

**Exploração:**
- App móvel (Android/iOS)
- Versão web
- Cloud storage
- Colaboração em tempo real
- Marketplace de templates
- API pública

---

## 🙏 Agradecimentos

### Tecnologias

- **Python** - Linguagem incrível
- **PyQt5** - Framework poderoso
- **NumPy** - Cálculos eficientes
- **Git** - Controle de versão

### Comunidade

- Todos os contribuidores
- Usuários que reportam bugs
- Pessoas que dão feedback
- Open source community

---

## 👨‍💻 Autores

### Desenvolvedor Principal

**Claude**
- 📧 Email: seu-email@exemplo.com
- 🐙 GitHub: [@seu-usuario](https://github.com/seu-usuario)
- 💼 LinkedIn: [Seu Nome](https://linkedin.com/in/seu-perfil)

### Contribuidores

Veja a lista completa de [contribuidores](https://github.com/seu-usuario/gerador-cadernos/graphs/contributors) que participaram deste projeto.

---

## ⭐ Mostre seu Apoio

Gostou do projeto? Considere:

- ⭐ Dar uma estrela no GitHub
- 🍴 Fork e contribuir
- 📢 Compartilhar com amigos
- 💬 Deixar feedback
- ☕ [Buy me a coffee](https://buymeacoffee.com/seu-usuario)

---

## 📊 Status do Projeto

![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento%20Ativo-brightgreen)
![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Última Atualização](https://img.shields.io/badge/última%20atualização-Outubro%202025-orange)
![Licença](https://img.shields.io/badge/licença-MIT-green)

**Estatísticas:**
- 🌟 Stars: 0
- 🍴 Forks: 0
- 📋 Issues Abertas: 0
- 🔀 Pull Requests: 0

---

## 📱 Redes Sociais

Siga para novidades:

- 🐦 Twitter: [@gerador_cadernos](https://twitter.com/gerador_cadernos)
- 📘 Facebook: [Gerador Cadernos](https://facebook.com/gerador-cadernos)
- 📷 Instagram: [@gerador.cadernos](https://instagram.com/gerador.cadernos)
- 🎥 YouTube: [Canal Gerador Cadernos](https://youtube.com/c/gerador-cadernos)

---

## 💻 Desenvolvido Com

- ❤️ Amor por código
- ☕ Muito café
- 🎵 Boa música
- 🌙 Noites de programação
- 🧠 Muita criatividade

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

---

Desenvolvido com ❤️ pela equipe Seeds Aura
**⭐ Se este projeto foi útil, considere dar uma estrela!**

**[⬆ Voltar ao Topo](#-gerador-de-cadernos-personalizados---documentação-completa)**

---

© 2025 Gerador de Cadernos Personalizados. Todos os direitos reservados.

</div>
