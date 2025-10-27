# 🎨 Procedural Explorer

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**Procedural Explorer** é uma ferramenta educativa interativa para explorar algoritmos de geração procedural e visualização de dados. Com uma interface gráfica intuitiva, você pode experimentar com 15 algoritmos diferentes, ajustar parâmetros em tempo real e visualizar os resultados instantaneamente.

![Screenshot](https://via.placeholder.com/800x500/1e1e1e/ffffff?text=Procedural+Explorer+Screenshot)

---

## ✨ Características

- 🎯 **15 Algoritmos Implementados** - De Perlin Noise a Voxel Grids 3D
- 🎛️ **Controles Dinâmicos** - Parâmetros específicos para cada algoritmo
- 📚 **Descrições Educativas** - Aprenda sobre cada algoritmo enquanto experimenta
- 🖼️ **Exportação de Imagens** - Salve seus resultados em PNG, JPG ou SVG
- ⚡ **Preview em Tempo Real** - Visualização imediata com Matplotlib
- 🌱 **Sistema de Seeds** - Reproduza e compartilhe resultados

---

## 📦 Instalação

### Pré-requisitos

```bash
Python 3.7 ou superior
```

### Instalar Dependências

```bash
pip install PyQt5 matplotlib numpy
```

### Executar o Programa

```bash
python procedural_explorer_improved.py
```

---

## 🎮 Algoritmos Disponíveis

### 🌊 Algoritmos 2D

#### 1. **Perlin Noise**
Ruído coerente criado por Ken Perlin em 1983. Gera padrões suaves e naturais, ideal para texturas de nuvens, terrenos e efeitos orgânicos.

**Parâmetros:**
- Largura/Altura (64-1024)
- Escala (10-200)
- Oitavas (1-8)
- Seed

**Aplicações:** Texturas procedurais, mapas de terreno, efeitos atmosféricos

---

#### 2. **Worley Noise F1 / F2**
Também chamado de Cellular Noise, cria padrões celulares baseados em distâncias a pontos.
- **F1**: Distância ao ponto mais próximo
- **F2**: Distância ao segundo ponto mais próximo

**Parâmetros:**
- Largura/Altura (64-1024)
- Pontos (10-200)
- Seed

**Aplicações:** Texturas de pedra, células biológicas, padrões de mármore

---

#### 3. **Voronoi Diagram**
Partição espacial que divide o espaço em regiões baseadas na proximidade a pontos.

**Parâmetros:**
- Largura/Altura (64-1024)
- Pontos (10-150)
- Seed

**Aplicações:** Mapeamento territorial, análise espacial, arte generativa

---

#### 4. **Maze (Recursive Backtracker)**
Gerador de labirintos perfeitos usando algoritmo de retrocesso recursivo.

**Parâmetros:**
- Células X (5-50)
- Células Y (5-50)
- Seed

**Aplicações:** Jogos, puzzles, geração de dungeons

---

#### 5. **DLA (Diffusion-Limited Aggregation)**
Simula crescimento de estruturas fractais através da agregação de partículas.

**Parâmetros:**
- Tamanho da Grade (64-512)
- Partículas (100-5000)
- Seed

**Aplicações:** Simulação de cristais, corais, relâmpagos, crescimento natural

---

#### 6. **K-Means Clustering**
Algoritmo de aprendizado não-supervisionado que agrupa pontos em K clusters.

**Parâmetros:**
- Pontos (100-1000)
- K - Número de Clusters (2-15)
- Seed

**Aplicações:** Análise de dados, segmentação, compressão de imagens

---

#### 7. **Quadtree**
Estrutura de dados hierárquica que particiona o espaço recursivamente.

**Parâmetros:**
- Largura/Altura (100-1000)
- Pontos (50-1000)
- Capacidade (1-20)
- Profundidade Máxima (3-12)
- Seed

**Aplicações:** Otimização de buscas espaciais, detecção de colisão, LOD

---

#### 8. **Circle Packing**
Algoritmo que empacota círculos sem sobreposição dentro de um container.

**Parâmetros:**
- Raio do Container (50-300)
- Número de Círculos (20-300)
- Raio Mínimo/Máximo (2-50)
- Seed

**Aplicações:** Design gráfico, visualização de dados, arte generativa

---

#### 9. **Domain Warping**
Técnica avançada que distorce o domínio antes de amostrar ruído, criando padrões complexos.

**Parâmetros:**
- Largura/Altura (64-1024)
- Escala Base (20-150)
- Força de Warp (0.5-5.0)
- Seed

**Aplicações:** Texturas orgânicas avançadas, nuvens realistas, terrenos complexos

---

### 🏔️ Algoritmos 3D

#### 10. **Esfera Paramétrica**
Superfície 3D gerada por equações paramétricas matemáticas.

**Parâmetros:**
- Resolução (20-150)

**Aplicações:** Modelagem procedural, demonstração de superfícies paramétricas

---

#### 11. **Terreno Diamond-Square**
Algoritmo clássico de geração de heightmaps fractais para terrenos.

**Parâmetros:**
- Rugosidade (0.1-1.5)
- Seed

**Aplicações:** Jogos (usado desde anos 80), simuladores, visualização de terrenos

---

#### 12. **Terreno Fault Formation**
Simula formação geológica de terrenos através de falhas tectônicas.

**Parâmetros:**
- Tamanho (40-200)
- Iterações (100-5000)
- Seed

**Aplicações:** Simulação geológica, terrenos naturais, jogos

---

#### 13. **Voxel Grid (Esfera)**
Representação volumétrica 3D usando cubos (voxels).

**Parâmetros:**
- Tamanho da Grade (10-40)
- Raio (3-20)

**Aplicações:** Minecraft-style, simulações volumétricas, modelagem 3D

---

#### 14. **Superfície Perlin (Heightmap)**
Terreno 3D gerado usando Perlin Noise para elevações.

**Parâmetros:**
- Resolução (40-220)
- Escala (10-150)
- Oitavas (1-8)
- Seed

**Aplicações:** Terrenos orgânicos, mapas de jogos, visualização de dados

---

## 🎯 Guia de Uso

### Fluxo de Trabalho Básico

1. **Selecione um Algoritmo**
   - Use o menu dropdown para escolher
   - Leia a descrição para entender o algoritmo

2. **Ajuste os Parâmetros**
   - Cada algoritmo tem controles específicos
   - Intervalos maiores facilitam ver diferenças
   - Seeds com incremento de 100 para exploração rápida

3. **Execute e Visualize**
   - Clique em "▶ Executar"
   - Veja o resultado instantaneamente
   - Experimente com diferentes seeds

4. **Salve seus Resultados**
   - Clique em "💾 Salvar imagem"
   - Escolha formato: PNG, JPG ou SVG
   - Imagens salvas em alta resolução (300 DPI)

### Dicas para Exploração

- 🎲 **Seeds**: Mude em incrementos de 100 para variações significativas
- 📏 **Escala**: Valores maiores = padrões maiores/menos detalhes
- 🔢 **Oitavas**: Mais oitavas = mais detalhes finos
- 🎯 **Pontos**: Quantidade afeta densidade e complexidade
- ⚡ **Iterações**: Mais iterações = resultados mais desenvolvidos

---

## 🏗️ Arquitetura do Código

### Estrutura Principal

```
procedural_explorer_improved.py
│
├── Utilidades Matemáticas
│   ├── clamp01()
│   ├── lerp()
│   └── smoothstep()
│
├── Algoritmos de Ruído
│   ├── Perlin2D (classe)
│   ├── perlin_noise_2d_map()
│   ├── domain_warping_map()
│   ├── worley_noise_2d()
│   └── voronoi_distance_map()
│
├── Algoritmos de Estrutura
│   ├── maze_recursive_backtracker()
│   ├── dla()
│   ├── k_means_demo()
│   ├── Quadtree (classe)
│   └── circle_packing()
│
├── Algoritmos 3D
│   ├── diamond_square()
│   ├── fault_formation()
│   ├── voxel_grid_sphere()
│   └── sphere_parametric()
│
└── Interface Gráfica (PyQt5)
    ├── DynamicControlPanel (classe)
    └── ProceduralExplorer (classe)
```

### Componentes Chave

#### `DynamicControlPanel`
Gerencia controles dinâmicos que mudam conforme o algoritmo selecionado.

```python
panel.add_spinbox('name', 'Label', min, max, default, step)
panel.add_doublespinbox('name', 'Label', min, max, default, step)
panel.get_value('name')
```

#### `ProceduralExplorer`
Janela principal que coordena interface, execução e visualização.

---

## 🔬 Detalhes Técnicos

### Perlin Noise Implementation

```python
class Perlin2D:
    def __init__(self, w, h, seed=0):
        # Gera gradientes aleatórios normalizados
        self.grad = rng.rand(w+1, h+1, 2)*2 - 1
        
    def sample(self, x, y):
        # Interpolação suave com smoothstep
        sx = smoothstep(x - x0)
        sy = smoothstep(y - y0)
        # Interpolação bilinear dos gradientes
        return lerp(ix0, ix1, sy)
```

### Domain Warping

```python
def domain_warping_map(...):
    # Gera campos de deslocamento com Perlin
    warp_u = perlin_noise_2d_map(...)
    warp_v = perlin_noise_2d_map(...)
    
    # Distorce coordenadas antes de amostrar
    sx = (x + du[y, x]) / base_scale
    sy = (y + dv[y, x]) / base_scale
```

### Quadtree Spatial Partitioning

```python
class Quadtree:
    def insert(self, pt):
        if len(self.points) < capacity:
            # Adiciona ao nó atual
        else:
            # Subdivide em 4 quadrantes
            self.subdivide()
```

---

## 📊 Comparação de Algoritmos

| Algoritmo | Tipo | Complexidade | Melhor Para |
|-----------|------|--------------|-------------|
| Perlin Noise | Ruído | O(n²) | Terrenos naturais, nuvens |
| Worley | Ruído | O(n²·p) | Texturas celulares, pedras |
| Voronoi | Partição | O(n²·p) | Territórios, mosaicos |
| Maze | Geração | O(w·h) | Labirintos perfeitos |
| DLA | Simulação | O(p·s) | Crescimento fractal |
| K-Means | ML | O(n·k·i) | Clustering de dados |
| Quadtree | Estrutura | O(log n) | Buscas espaciais |
| Circle Packing | Geometria | O(n²) | Design gráfico |
| Domain Warp | Ruído | O(n²) | Texturas complexas |

**Legenda:** n=pixels, p=pontos, w=largura, h=altura, k=clusters, i=iterações, s=steps

---

## 🎓 Recursos Educacionais

### Para Aprender Mais

**Perlin Noise:**
- [Original Paper (1985)](https://mrl.cs.nyu.edu/~perlin/paper445.pdf)
- [Understanding Perlin Noise](https://adrianb.io/2014/08/09/perlinnoise.html)

**Worley Noise:**
- [Worley's Original Paper](https://www.rhythmiccanvas.com/research/papers/worley.pdf)

**DLA:**
- [Wikipedia - DLA](https://en.wikipedia.org/wiki/Diffusion-limited_aggregation)

**Voronoi:**
- [Red Blob Games - Voronoi](https://www.redblobgames.com/x/1842-delaunay-voronoi-sphere/)

**Maze Generation:**
- [Think Labyrinth - Algorithms](http://www.astrolog.org/labyrnth/algrithm.htm)

**Quadtrees:**
- [Quadtree Visualization](https://jimkang.com/quadtreevis/)

---

## 🛠️ Personalização e Extensão

### Adicionar Novo Algoritmo

1. **Implemente a função do algoritmo:**

```python
def my_new_algorithm(width, height, param1, param2, seed=0):
    # Sua implementação aqui
    result = np.zeros((height, width))
    # ...
    return result
```

2. **Adicione à lista de algoritmos:**

```python
ALGOS = [
    # ... algoritmos existentes
    "2D - Meu Algoritmo",
]
```

3. **Adicione a descrição:**

```python
ALGORITHM_DESCRIPTIONS = {
    "2D - Meu Algoritmo": """DESCRIÇÃO EDUCATIVA
    
    Explicação do que o algoritmo faz...
    
    Parâmetros:
    • Param1: O que faz (range)
    • Param2: O que faz (range)
    """,
}
```

4. **Configure os controles:**

```python
elif algo_name == "2D - Meu Algoritmo":
    self.control_panel.add_spinbox('param1', 'Parâmetro 1:', 1, 100, 50)
    self.control_panel.add_doublespinbox('param2', 'Parâmetro 2:', 0.1, 10.0, 1.0)
```

5. **Adicione a execução:**

```python
elif algo == "2D - Meu Algoritmo":
    img = my_new_algorithm(
        width=p.get_value('width'),
        height=p.get_value('height'),
        param1=p.get_value('param1'),
        param2=p.get_value('param2'),
        seed=p.get_value('seed')
    )
    ax = self.fig.add_subplot(111)
    ax.imshow(img, origin='upper', cmap='viridis')
    ax.set_title(algo, fontsize=14, fontweight='bold')
    ax.axis('off')
```

---

## 🐛 Troubleshooting

### Problemas Comuns

**Erro: "No module named 'PyQt5'"**
```bash
pip install PyQt5
```

**Erro: "No module named 'matplotlib'"**
```bash
pip install matplotlib
```

**Renderização lenta em 3D:**
- Reduza a resolução dos algoritmos 3D
- Diamond-Square: use tamanho fixo de 129
- Voxels: mantenha grid abaixo de 30

**Imagem não salva:**
- Verifique permissões da pasta
- Certifique-se de ter executado o algoritmo antes

---

## 🚀 Roadmap Futuro

- [ ] Mais algoritmos de ruído (Simplex, Gabor)
- [ ] Animações e exportação de vídeo
- [ ] Modo batch para gerar múltiplas variações
- [ ] Presets salvos e compartilháveis
- [ ] Shader GLSL em tempo real
- [ ] Suporte a GPU com CUDA/OpenCL
- [ ] Plugin system para algoritmos customizados
- [ ] Modo comparação lado-a-lado

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. 🐛 Reportar bugs
2. 💡 Sugerir novos algoritmos
3. 📝 Melhorar documentação
4. 🔧 Enviar pull requests

### Como Contribuir

```bash
# Fork o projeto
git clone https://github.com/seu-usuario/procedural-explorer.git

# Crie uma branch
git checkout -b feature/novo-algoritmo

# Faça suas mudanças e commit
git commit -m "Adiciona algoritmo X"

# Push e abra um Pull Request
git push origin feature/novo-algoritmo
```

---

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

```
MIT License

Copyright (c) 2025 Procedural Explorer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 👨‍💻 Autor

Desenvolvido com ❤️ para a comunidade de computação gráfica e geração procedural.

**Contato:**
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Email: seu-email@example.com

---

## 🌟 Agradecimentos

- **Ken Perlin** - Por inventar o Perlin Noise
- **Steven Worley** - Pela técnica de Worley Noise
- **Comunidade PyQt5** - Pela excelente documentação
- **Matplotlib Team** - Por tornar visualização fácil
- **Todos os contribuidores** - Por melhorar este projeto

---

## 📸 Galeria

### Perlin Noise
![Perlin](https://via.placeholder.com/300x300/88bb44/ffffff?text=Perlin+Noise)

### Worley F1
![Worley](https://via.placeholder.com/300x300/4488bb/ffffff?text=Worley+F1)

### Domain Warping
![Warp](https://via.placeholder.com/300x300/bb4488/ffffff?text=Domain+Warping)

### DLA
![DLA](https://via.placeholder.com/300x300/ff6644/ffffff?text=DLA)

### Terrain
![Terrain](https://via.placeholder.com/300x300/44bb88/ffffff?text=Terrain)

---

## 📚 Referências

1. Perlin, K. (1985). "An Image Synthesizer". SIGGRAPH '85
2. Worley, S. (1996). "A Cellular Texture Basis Function"
3. Witten, T. A., & Sander, L. M. (1981). "Diffusion-Limited Aggregation"
4. MacQueen, J. (1967). "Some Methods for classification and Analysis of Multivariate Observations"
5. Fournier, A., Fussell, D., & Carpenter, L. (1982). "Computer Rendering of Stochastic Models"

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela!**

[🐛 Report Bug](https://github.com/seu-usuario/procedural-explorer/issues) · 
[✨ Request Feature](https://github.com/seu-usuario/procedural-explorer/issues) · 
[📖 Documentation](https://github.com/seu-usuario/procedural-explorer/wiki)

</div>

---

**Versão:** 2.0  
**Última Atualização:** Janeiro 2025  
**Status:** ✅ Ativo e Mantido
