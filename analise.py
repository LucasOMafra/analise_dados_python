"""
Análise Exploratória de Dados - Vendas fictícias
Autor: Lucas Mafra
Data: Abril de 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── Configurações gerais ──────────────────────────────────────────────────────
np.random.seed(42)
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── 1. Geração de dados sintéticos ────────────────────────────────────────────
print("=" * 50)
print("  ANÁLISE EXPLORATÓRIA DE DADOS - VENDAS")
print("=" * 50)

n = 200
meses = np.arange(1, 13)
categorias = ["Eletrônicos", "Roupas", "Alimentos", "Livros", "Esportes"]

df = pd.DataFrame({
    "mes":        np.random.choice(meses, n),
    "categoria":  np.random.choice(categorias, n),
    "vendas":     np.random.normal(loc=5000, scale=1500, size=n).clip(500),
    "unidades":   np.random.randint(1, 100, size=n),
    "desconto":   np.random.uniform(0, 0.3, size=n),
})
df["receita_liquida"] = df["vendas"] * (1 - df["desconto"])

# Salva CSV
csv_path = os.path.join("data", "vendas.csv")
df.to_csv(csv_path, index=False)
print(f"\n✔ Dataset salvo em '{csv_path}' ({len(df)} registros)\n")

# ── 2. Estatísticas descritivas ───────────────────────────────────────────────
print("── Estatísticas Descritivas ──────────────────")
print(df[["vendas", "unidades", "desconto", "receita_liquida"]].describe().round(2))

total = df["receita_liquida"].sum()
media = df["receita_liquida"].mean()
mediana = df["receita_liquida"].median()
desvio = df["receita_liquida"].std()

print(f"\nReceita Líquida Total : R$ {total:,.2f}")
print(f"Média por transação   : R$ {media:,.2f}")
print(f"Mediana               : R$ {mediana:,.2f}")
print(f"Desvio Padrão         : R$ {desvio:,.2f}")

# ── 3. Análise por categoria ──────────────────────────────────────────────────
print("\n── Receita por Categoria ─────────────────────")
por_cat = (
    df.groupby("categoria")["receita_liquida"]
    .agg(total="sum", media="mean", transacoes="count")
    .sort_values("total", ascending=False)
)
print(por_cat.round(2).to_string())

# ── 4. Análise por mês ────────────────────────────────────────────────────────
por_mes = df.groupby("mes")["receita_liquida"].sum().reindex(meses, fill_value=0)

# ── 5. Visualizações ──────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Análise de Vendas — Dashboard Geral", fontsize=15, fontweight="bold", y=1.01)

cores = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]

# --- 5a. Barras por categoria ---
ax = axes[0, 0]
bars = ax.bar(por_cat.index, por_cat["total"], color=cores)
ax.set_title("Receita Total por Categoria")
ax.set_ylabel("Receita Líquida (R$)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))
ax.tick_params(axis="x", rotation=15)
for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.01,
            f"R${bar.get_height()/1000:.1f}k", ha="center", fontsize=8)

# --- 5b. Linha mensal ---
ax = axes[0, 1]
ax.plot(meses, por_mes.values, marker="o", color="#4C72B0", linewidth=2, markersize=6)
ax.fill_between(meses, por_mes.values, alpha=0.15, color="#4C72B0")
ax.set_title("Receita Mensal")
ax.set_xlabel("Mês")
ax.set_ylabel("Receita Líquida (R$)")
ax.set_xticks(meses)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"R${x/1000:.0f}k"))

# --- 5c. Histograma ---
ax = axes[1, 0]
ax.hist(df["receita_liquida"], bins=25, color="#55A868", edgecolor="white", alpha=0.85)
ax.axvline(media,   color="red",    linestyle="--", linewidth=1.5, label=f"Média: R${media:,.0f}")
ax.axvline(mediana, color="orange", linestyle=":",  linewidth=1.5, label=f"Mediana: R${mediana:,.0f}")
ax.set_title("Distribuição da Receita por Transação")
ax.set_xlabel("Receita Líquida (R$)")
ax.set_ylabel("Frequência")
ax.legend(fontsize=8)

# --- 5d. Pizza de participação ---
ax = axes[1, 1]
wedges, texts, autotexts = ax.pie(
    por_cat["total"],
    labels=por_cat.index,
    autopct="%1.1f%%",
    colors=cores,
    startangle=140,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
)
for t in autotexts:
    t.set_fontsize(8)
ax.set_title("Participação por Categoria (%)")

plt.tight_layout()
chart_path = os.path.join(OUTPUT_DIR, "dashboard_vendas.png")
plt.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"\n✔ Dashboard salvo em '{chart_path}'")

# ── 6. Correlação ─────────────────────────────────────────────────────────────
print("\n── Correlação entre variáveis numéricas ──────")
corr = df[["vendas", "unidades", "desconto", "receita_liquida"]].corr().round(3)
print(corr.to_string())

print("\n✔ Análise concluída com sucesso!\n")
