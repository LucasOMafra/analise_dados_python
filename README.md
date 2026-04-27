# 📊 Análise Exploratória de Dados — Vendas

Projeto de análise de dados com Python, utilizando **NumPy**, **Pandas** e **Matplotlib** para explorar um dataset sintético de vendas e gerar insights visuais.

---

## 🗂️ Estrutura do Projeto

analise_dados_python/
├── analise.py 
├── data/
│   └── vendas.csv
├── outputs/
│   └── dashboard_vendas.png
├── requirements.txt
└── README.md

---

## 📌 O que o projeto faz

1. **Geração de dados sintéticos** — cria 200 registros de vendas com categorias, meses, descontos e receitas
2. **Estatísticas descritivas** — média, mediana, desvio padrão e totais por variável
3. **Análise por categoria** — agrupamento de receita líquida por tipo de produto
4. **Análise mensal** — evolução da receita ao longo dos 12 meses
5. **Visualizações** — dashboard com 4 gráficos:
   - 📊 Receita total por categoria (barras)
   - 📈 Receita mensal ao longo do ano (linha)
   - 📉 Distribuição da receita por transação (histograma)
   - 🥧 Participação de cada categoria (pizza)
6. **Análise de correlação** entre as variáveis numéricas

---

## 🛠️ Tecnologias utilizadas

| Biblioteca | Uso |
|---|---|
| `numpy` | Geração de dados e operações numéricas |
| `pandas` | Manipulação e agrupamento de dados |
| `matplotlib` | Visualização e geração dos gráficos |

---

## 🚀 Como executar

**1. Clone o repositório**
git clone https://github.com/LucasOMafra/analise_dados_python.git
cd analise_dados_python

**2. Instale as dependências**
pip install -r requirements.txt

**3. Execute a análise**
python analise.py

Os resultados serão salvos em data/ e outputs/.

---

## 📈 Exemplo de saída

Receita Líquida Total : R$ 845.430,33
Média por transação   : R$ 4.227,15
Mediana               : R$ 4.221,07
Desvio Padrão         : R$ 1.427,06

---

## 👨‍💻 Autor

**Lucas Mafra**
LinkedIn: https://linkedin.com/in/lucasomafra
GitHub: https://github.com/LucasOMafra
