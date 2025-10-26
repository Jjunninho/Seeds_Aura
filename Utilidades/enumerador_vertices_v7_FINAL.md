# 📐 Enumerador de Vértices - Seeds Aura

**Versão:** 7.0 Final  
**Desenvolvido por:** Seeds Aura  
**Data:** Outubro 2025

---

## 🎯 Descrição

O **Enumerador de Vértices** é uma ferramenta profissional para detecção, classificação e numeração automática de vértices em imagens de malhas estruturais, redes hexagonais, grafos e estruturas geométricas.

O programa utiliza algoritmos avançados de visão computacional (detecção de cantos Shi-Tomasi, clustering DBSCAN adaptativo e análise de vizinhança) para identificar e classificar diferentes tipos de pontos em malhas complexas.

---

## ✨ Principais Funcionalidades

### 🔍 Detecção Inteligente
- Detecção automática de vértices usando algoritmo Shi-Tomasi
- Clustering adaptativo para agrupar pontos próximos
- Remoção inteligente de duplicatas
- Suporte a imagens PNG, JPG, BMP, TIFF

### 📊 Classificação Automática
O programa classifica automaticamente os vértices em três categorias:

1. **🔶 Junções (Vértices)** - Pontos onde 3 ou mais arestas se encontram (centros de interseção)
2. **🔷 Centros de Aresta** - Pontos localizados no meio das linhas da malha
3. **🔵 Centros de Célula** - Pontos isolados no centro dos polígonos/hexágonos

### 🔢 Enumeração Flexível
- Enumere **todos os pontos** ou apenas um tipo específico
- Numeração sequencial inteligente (linha por linha, esquerda → direita)
- Ordenação automática otimizada

### 🎨 Personalização Visual
- **6 cores disponíveis:** Vermelho, Azul, Verde, Preto, Branco, Laranja
- **Tamanho ajustável:** 0.30 a 2.50
- **Espessura ajustável:** 1 a 5
- Atualização em tempo real

### 💾 Exportação de Dados
- **PNG:** Imagem numerada em alta qualidade
- **CSV:** Coordenadas (id, x, y) para análise posterior
- Nomes de arquivo automáticos e descritivos

---

## 🚀 Como Usar

### Passo 1: Abrir Imagem
1. Clique em **📁 Abrir Imagem**
2. Selecione uma imagem de malha (PNG, JPG, BMP ou TIFF)
3. A imagem será exibida na área de preview

### Passo 2: Detectar Vértices
1. Clique em **⚙️ Detectar Vértices**
2. O programa irá:
   - Detectar bordas e cantos
   - Agrupar pontos próximos
   - Remover duplicatas
   - Classificar os vértices automaticamente

### Passo 3: Escolher o que Enumerar
Selecione uma das opções:
- **Todos os pontos** - Enumera todos os vértices detectados
- **Apenas JUNÇÕES** - Enumera apenas os centros de interseção
- **Apenas CENTROS DE ARESTA** - Enumera apenas pontos nas linhas
- **Apenas CENTROS DE CÉLULA** - Enumera apenas centros dos polígonos

### Passo 4: Ajustar Aparência
- Escolha a **cor** dos números
- Ajuste o **tamanho** da fonte
- Ajuste a **espessura** dos números
- A visualização atualiza automaticamente

### Passo 5: Salvar Resultados
- **💾 Salvar PNG** - Salva a imagem numerada
- **📊 Salvar CSV** - Salva as coordenadas em formato CSV

### Extra: Botão Limpar
- **🧹 Limpar Numeração** - Remove os números mas mantém os vértices detectados
- Útil para testar diferentes configurações visuais sem reprocessar

---

## ⚙️ Parâmetros Avançados

### Parâmetros de Detecção (Colapsável)

#### Raio de fusão (3.0 - 30.0)
- Controla o agrupamento de pontos próximos
- **Valor maior** = mais agressivo, remove mais duplicatas
- **Valor menor** = mais conservador, detecta mais pontos
- **Padrão:** 10.0

#### Dist. mínima (2.0 - 20.0)
- Distância mínima entre vértices distintos
- Previne duplicatas após o clustering
- **Valor maior** = pontos mais espaçados
- **Valor menor** = permite pontos mais próximos
- **Padrão:** 8.0

#### Vizinhos p/ junção (2 - 8)
- Número mínimo de vizinhos para classificar como junção
- **Valor maior** = apenas interseções muito densas são junções
- **Valor menor** = mais pontos classificados como junções
- **Padrão:** 3

#### Tolerância linha (0.01 - 0.15)
- Controla o agrupamento vertical para ordenação
- **Valor menor** = numeração mais estrita (linha por linha)
- **Valor maior** = agrupa mais pontos na mesma "linha"
- **Padrão:** 0.040

---

## 📋 Formato de Saída

### Arquivo PNG
- Formato: PNG de 32 bits com transparência preservada
- Sufixos automáticos:
  - `_todos.png` - Todos os pontos
  - `_juncoes.png` - Apenas junções
  - `_centros_aresta.png` - Apenas centros de aresta
  - `_centros_celula.png` - Apenas centros de célula

### Arquivo CSV
- Formato: `id,x,y`
- Encoding: UTF-8
- Separador: vírgula
- Primeira linha: cabeçalho
- Coordenadas em pixels (origem: canto superior esquerdo)

**Exemplo:**
```csv
id,x,y
1,125.50,89.32
2,201.75,90.18
3,278.00,91.05
```

---

## 🔧 Requisitos Técnicos

### Dependências Python
```bash
pip install numpy opencv-python PyQt5 scipy
```

**Versões mínimas:**
- **Python:** 3.7 ou superior
- **NumPy:** ≥1.19.0
- **OpenCV:** ≥4.5.0
- **PyQt5:** ≥5.15.0
- **SciPy:** ≥1.7.0

### Sistema Operacional
- ✅ Windows 7/8/10/11
- ✅ Linux (Ubuntu, Fedora, etc.)
- ✅ macOS 10.13 ou superior

### Instalação Rápida

#### Windows
```bash
# Instale o Python 3.7+ primeiro (python.org)
pip install numpy opencv-python PyQt5 scipy

# Execute o programa
python enumerador_vertices_v7_FINAL.py
```

#### Linux/macOS
```bash
# Certifique-se de ter Python 3.7+
pip3 install numpy opencv-python PyQt5 scipy

# Execute o programa
python3 enumerador_vertices_v7_FINAL.py
```

---

## 💡 Dicas de Uso

### Para Melhores Resultados:

✅ **Use imagens com bom contraste** - Bordas bem definidas facilitam a detecção

✅ **Resolução adequada** - Mínimo 800x600 pixels recomendado

✅ **Formato PNG com fundo transparente** - Detecção mais precisa

✅ **Comece com parâmetros padrão** - Ajuste apenas se necessário

### Resolução de Problemas:

#### ❌ "Nenhum canto detectado"
**Soluções:**
- Aumente o contraste da imagem
- Reduza o valor de "Dist. mínima"
- Use imagem em escala de cinza ou com transparência

#### ❌ Números duplicados no mesmo ponto
**Soluções:**
- Aumente "Raio de fusão" (ex: 12-15)
- Aumente "Dist. mínima" (ex: 10-12)

#### ❌ Pontos faltando
**Soluções:**
- Diminua "Raio de fusão" (ex: 6-8)
- Diminua "Dist. mínima" (ex: 4-6)

#### ❌ Numeração desordenada
**Soluções:**
- Ajuste "Tolerância linha" (ex: 0.03 para mais rigor)
- Verifique se a malha está alinhada horizontalmente

---

## 📚 Aplicações

O Enumerador de Vértices pode ser utilizado em diversas áreas:

### 🏗️ Engenharia
- Análise de elementos finitos
- Malhas de vigas e estruturas
- Simulações computacionais

### 🔬 Ciência
- Grafos e redes complexas
- Estruturas celulares hexagonais
- Redes cristalinas
- Análise topológica

### 🏛️ Arquitetura
- Estruturas geométricas
- Padrões arquitetônicos
- Design paramétrico

### 📖 Educação
- Ensino de geometria
- Estruturas de dados
- Teoria dos grafos

### 🎨 Design
- Padrões geométricos
- Arte generativa
- Tessellações

---

## 🎓 Fundamentos Técnicos

### Algoritmos Utilizados

#### 1. Detecção de Cantos (Shi-Tomasi)
O algoritmo de Shi-Tomasi é uma melhoria do detector de cantos Harris, identificando pontos de interesse com alta precisão baseado em gradientes de intensidade.

#### 2. Clustering Adaptativo (DBSCAN-like)
Um algoritmo de clustering que agrupa pontos próximos iterativamente:
- Mescla pontos dentro de um raio (eps)
- Não requer número pré-definido de clusters
- Robusto a ruído e outliers

#### 3. Análise de Vizinhança
Classifica pontos baseado no número de vizinhos:
- Calcula matriz de distâncias
- Conta vizinhos dentro de um raio
- Classifica em junções, arestas ou células

#### 4. Ordenação Sequencial
Ordena pontos para numeração consistente:
- Agrupa por "linhas" horizontais
- Ordena esquerda→direita em cada linha
- Tolerância ajustável para robustez

---

## 🔐 Limitações e Considerações

### Limitações Conhecidas:
- ⚠️ Malhas muito densas (>2000 vértices) podem demorar mais para processar
- ⚠️ Imagens com baixo contraste podem ter detecção imprecisa
- ⚠️ Estruturas muito irregulares podem precisar ajuste manual de parâmetros

### Recomendações:
- Para malhas muito grandes, processe em seções menores
- Pré-processe imagens com baixo contraste usando ferramentas de edição
- Salve diferentes versões com parâmetros variados para comparação

---

## 🆘 Suporte e Contato

Para dúvidas, problemas ou sugestões:

**Seeds Aura**  
📧 Email: contato@seedsaura.com  
🌐 Website: www.seedsaura.com  
📱 Suporte: suporte@seedsaura.com

---

## 📝 Notas de Versão

### v7.0 (Atual) - Outubro 2025
- ✨ **Novo:** Grupo de parâmetros colapsável para economizar espaço
- ✨ **Novo:** Botão "Limpar Numeração" para remover números sem reprocessar
- ✨ **Novo:** Atualização visual em tempo real ao mudar aparência
- 🐛 **Correção:** Algoritmo de detecção de duplicatas aprimorado
- 🎨 **Melhoria:** Interface otimizada e mais intuitiva
- 🎨 **Melhoria:** Feedback visual aprimorado com cores e status

### v6.0 - Outubro 2025
- 🎨 Interface lateral compacta
- 🎨 Área de preview maximizada
- 🎨 Organização em grupos lógicos
- 📊 Painel de informações detalhado

### v5.0 - Outubro 2025
- ⚙️ Controle de tolerância de linha
- 💬 Feedback visual melhorado
- 💡 Tooltips explicativos em todos os controles

### v4.0 - Outubro 2025
- 🔢 Sistema de classificação de vértices
- 📊 Três categorias: Junções, Arestas, Células
- 🎯 Enumeração seletiva por tipo

### v3.0 - Outubro 2025
- 🐛 Correção de duplicatas na numeração
- ⚙️ Algoritmo de clustering melhorado
- 🎨 Interface com grupos expansíveis

### v2.0 - Outubro 2025
- 🔧 Controles de clustering ajustáveis
- 💾 Exportação em CSV
- 🎨 Personalização de cores e tamanhos

### v1.0 - Outubro 2025
- 🎉 Versão inicial
- 🔍 Detecção básica de vértices
- 💾 Exportação em PNG

---

## 📄 Licença

© 2025 Seeds Aura - Todos os direitos reservados

Este software é propriedade da Seeds Aura. O uso, cópia, modificação e distribuição são permitidos apenas mediante autorização expressa.

---

## 🙏 Agradecimentos

Desenvolvido com dedicação pela equipe Seeds Aura.

Tecnologias utilizadas:
- **Python** - Linguagem de programação
- **OpenCV** - Visão computacional
- **NumPy** - Computação numérica
- **SciPy** - Algoritmos científicos
- **PyQt5** - Interface gráfica

---

## 📖 Referências

### Documentação Técnica:
- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [SciPy Documentation](https://docs.scipy.org/)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)

### Artigos Científicos:
- Shi, J., & Tomasi, C. (1994). "Good features to track"
- Ester, M., et al. (1996). "A density-based algorithm for discovering clusters"

---

**Versão 7.0 Final - Seeds Aura**  
**Última atualização: Outubro 2025**

*Desenvolvido com ❤️ pela equipe Seeds Aura*
