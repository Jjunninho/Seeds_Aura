# 🌱 Seeds Aura - Criador de Malhas Exóticas

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**Seeds Aura** é uma aplicação GUI em PyQt5 para criar e exportar malhas procedurais exóticas de alta qualidade. Ideal para artistas, designers e entusiastas de geometria computacional.

![Banner](https://via.placeholder.com/800x200/1a1a2e/eaeaea?text=Seeds+Aura+-+Malhas+Exóticas)

---

## ✨ Características

- 🎨 **5 Padrões Únicos** de malhas procedurais
- 🔄 **Preview em Tempo Real** com Matplotlib
- 🎲 **Controle de Semente Aleatória** para reprodutibilidade
- ⚙️ **Parâmetros Ajustáveis** específicos para cada padrão
- 💾 **Exportação de Alta Qualidade** em PNG (300 DPI) e PDF vetorial
- 🖥️ **Interface Intuitiva** com PyQt5

---

## 🎭 Padrões Disponíveis

### 1. 🔷 Voronoi Poisson-Disk
Diagrama de Voronoi com pontos distribuídos usando **amostragem Poisson-Disk** (algoritmo de Bridson). Cria células orgânicas com espaçamento uniforme.

**Parâmetros:**
- `W` - Largura da área (2.0 - 40.0)
- `H` - Altura da área (2.0 - 40.0)
- `r` - Raio mínimo entre pontos (0.1 - 2.0)

**Requer:** SciPy

---

### 2. 🍯 Colmeia Curvilínea
Malha hexagonal estilo favo de mel com bordas curvas suaves. Hexágonos com arcos elegantes em vez de linhas retas.

**Parâmetros:**
- `nx` - Número de células horizontais (4 - 64)
- `ny` - Número de células verticais (4 - 64)
- `R` - Raio do hexágono (4.0 - 64.0)
- `bulge` - Curvatura das bordas (0.0 - 0.75)

---

### 3. 🕸️ Malha Topológica (Arcos)
Grade com linhas verticais e conexões horizontais em arco alternadas, criando um padrão ondulado complexo.

**Parâmetros:**
- `nx` - Colunas (4 - 64)
- `ny` - Linhas (4 - 64)
- `sx` - Espaçamento horizontal (0.4 - 3.0)
- `sy` - Espaçamento vertical (0.4 - 3.0)
- `sag_frac` - Curvatura dos arcos (0.05 - 0.9)

---

### 4. 🌀 Quasicristal (Contornos)
Padrão quase-periódico gerado pela soma de ondas planas em ângulos uniformes. Produz simetrias complexas sem repetição.

**Parâmetros:**
- `W` - Largura em pixels (400 - 2200)
- `H` - Altura em pixels (400 - 2200)
- `k` - Número de ondas (3 - 19)
- `scale` - Escala do espaço-k (0.004 - 0.08)
- `levels` - Número de contornos (4 - 64)

---

### 5. 🌊 Grade Senoidal Distorcida
Grade retangular deformada por múltiplas ondas senoidais, criando um efeito de distorção fluida.

**Parâmetros:**
- `W` - Largura em pixels (400 - 2200)
- `H` - Altura em pixels (400 - 2200)
- `n` - Linhas por eixo (4 - 120)
- `amp` - Amplitude da distorção (0.0 - 120.0)
- `freq` - Frequência base das ondas (0.005 - 0.2)

---

## 📦 Instalação

### Requisitos
- Python 3.9 ou superior
- PyQt5
- NumPy
- Matplotlib
- SciPy (opcional, necessário para Voronoi)

### Instalação via pip

```bash
# Instalar todas as dependências
pip install PyQt5 numpy matplotlib scipy
```

### Instalação com ambiente virtual (recomendado)

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install PyQt5 numpy matplotlib scipy
```

---

## 🚀 Como Usar

### Execução Básica

```bash
python seeds_aura_malhas_exoticas_CORRIGIDO.py
```

### Interface

1. **Escolher Padrão:** Selecione um dos 5 padrões no menu dropdown
2. **Ajustar Semente:** Defina uma semente numérica ou clique em "Nova semente"
3. **Configurar Parâmetros:** Ajuste os parâmetros específicos do padrão
4. **Preview:** O preview é atualizado automaticamente
5. **Exportar:** Salve em PNG (300 DPI) ou PDF vetorial

### Atalhos

- **Nova semente:** Gera número aleatório para criar variações
- **Atualizar Preview:** Força redesenho (útil para debugging)
- **Espessura (lw):** Controla a largura das linhas (0.05 - 3.0)

---

## 💡 Exemplos de Uso

### Exemplo 1: Voronoi Orgânico
```python
# Configurações sugeridas:
Padrão: Voronoi Poisson-Disk
Semente: 1234
W: 10.0
H: 10.0
r: 0.45
Espessura: 0.65
```

### Exemplo 2: Favo de Mel Curvo
```python
# Configurações sugeridas:
Padrão: Colmeia Curvilínea
Semente: 42
nx: 16
ny: 12
R: 18.0
bulge: 0.35
Espessura: 0.7
```

### Exemplo 3: Quasicristal Denso
```python
# Configurações sugeridas:
Padrão: Quasicristal (contornos)
Semente: 2025
W: 900
H: 900
k: 12
scale: 0.025
levels: 20
Espessura: 0.5
```

---

## 🔧 Estrutura do Código

```
seeds_aura_malhas_exoticas_CORRIGIDO.py
├── Utilidades
│   ├── set_ax_clean()          # Limpa eixos do matplotlib
│   └── seed_everything()        # Define seeds para reprodutibilidade
│
├── Algoritmos de Padrões
│   ├── poisson_disk_sampling()  # Amostragem Poisson-Disk
│   ├── plot_voronoi_poisson()   # Renderiza Voronoi
│   ├── curved_hex_edges()       # Gera hexágonos curvos
│   ├── plot_curvy_honeycomb()   # Renderiza colmeia
│   ├── generate_topology()      # Gera malha topológica
│   ├── plot_topology()          # Renderiza topologia
│   ├── quasicrystal_field()     # Calcula campo quasicristalino
│   ├── plot_quasicrystal()      # Renderiza quasicristal
│   └── plot_warped_grid()       # Renderiza grade distorcida
│
└── Interface GUI (PyQt5)
    ├── SeedsAuraApp             # Classe principal da aplicação
    ├── reload_controls()        # Atualiza controles por padrão
    ├── update_preview()         # Atualiza preview em tempo real
    ├── save_figure()            # Exporta PNG/PDF
    └── randomize_seed()         # Gera nova semente
```

---

## 🎨 Casos de Uso

### Design Gráfico
- Texturas procedurais para backgrounds
- Padrões para estampas e tecidos
- Elementos decorativos únicos

### Arte Generativa
- Exploração de padrões matemáticos
- Criação de séries com variações controladas
- Estudos de simetria e quase-periodicidade

### Visualização Científica
- Ilustração de conceitos de geometria computacional
- Demonstração de algoritmos (Voronoi, Poisson-Disk)
- Pesquisa em quasicristais

### Arquitetura e Engenharia
- Inspiração para fachadas e elementos estruturais
- Padrões para painéis perfurados
- Estudos de malhas deformáveis

---

## 🐛 Solução de Problemas

### Erro: "SciPy ausente (Voronoi indisponível)"
**Solução:** Instale o SciPy:
```bash
pip install scipy
```

### Erro: "ModuleNotFoundError: No module named 'PyQt5'"
**Solução:** Instale o PyQt5:
```bash
pip install PyQt5
```

### Preview não atualiza automaticamente
**Solução:** Clique no botão "Atualizar Preview" manualmente.

### Exportação está cortada
**Solução:** A exportação usa `bbox_inches="tight"` automaticamente. Se ainda houver problemas, ajuste o tamanho da figura no código (linha 548):
```python
fig = Figure(figsize=(10,10), dpi=300)  # Aumente o figsize
```

---

## 🔬 Algoritmos Implementados

### Poisson-Disk Sampling (Bridson)
Gera pontos com distribuição uniforme mantendo distância mínima entre eles. Tempo: O(n).

### Arcos Circulares Interpolados
Calcula arcos que passam por dois pontos com curvatura especificada usando geometria de círculos.

### Soma de Ondas Planas
Cria padrões quase-periódicos somando k ondas com ângulos uniformemente distribuídos: θᵢ = 2πi/k.

### Distorção Senoidal Multifrecuencial
Aplica transformação não-linear usando composição de ondas senoidais com frequências e fases variadas.

---

## 📊 Desempenho

| Padrão | Tempo Médio* | Qualidade Export |
|--------|-------------|------------------|
| Voronoi Poisson-Disk | ~0.5s | Vetorial (linhas) |
| Colmeia Curvilínea | ~1.2s | Vetorial (curvas) |
| Malha Topológica | ~0.8s | Vetorial (arcos) |
| Quasicristal | ~2.5s | Raster (contornos) |
| Grade Distorcida | ~1.0s | Vetorial (curvas) |

*Tempos aproximados para parâmetros padrão em CPU moderna.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estas etapas:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovosPadroes`)
3. Commit suas mudanças (`git commit -m 'Adiciona novos padrões fractais'`)
4. Push para a branch (`git push origin feature/NovosPadroes`)
5. Abra um Pull Request

### Ideias para Contribuições
- [ ] Novos padrões de malhas (fractais, L-systems, etc.)
- [ ] Exportação para SVG puro
- [ ] Animações de transformação entre padrões
- [ ] Paleta de cores customizável
- [ ] Preset de configurações salvas
- [ ] Batch processing de múltiplas sementes

---

## 📝 Changelog

### Versão 1.1 (Atual)
- ✅ Corrigido bug de incompatibilidade de parâmetros
- ✅ Todas as 5 malhas funcionando corretamente
- ✅ Melhor tratamento de erros
- ✅ Documentação completa

### Versão 1.0
- 🎉 Lançamento inicial
- 5 padrões de malhas procedurais
- Interface GUI com PyQt5
- Exportação PNG/PDF

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

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

## 🙏 Agradecimentos

- **Robert Bridson** - Algoritmo Poisson-Disk Sampling
- **Comunidade PyQt5** - Framework GUI robusto
- **Matplotlib** - Biblioteca de visualização poderosa
- **NumPy/SciPy** - Computação científica em Python

---

## 📬 Contato

- **Desenvolvedor:** Seeds Aura Team
- **GitHub:** [github.com/seu-usuario/seeds-aura](https://github.com)
- **Issues:** [github.com/seu-usuario/seeds-aura/issues](https://github.com)

---

## 🌟 Showcase

Compartilhe suas criações usando #SeedsAura!

```
Criado com amor e matemática 💕➕🔢 = 🎨
```

---

<div align="center">

### ⭐ Se você gostou, deixe uma estrela no repositório! ⭐

Desenvolvido com ❤️ pela equipe Seeds Aura
**⭐ Se este projeto foi útil, considere dar uma estrela!**

[⬆ Voltar ao topo](#-seeds-aura---criador-de-malhas-exóticas)

</div>
