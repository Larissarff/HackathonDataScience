import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Leitura de arquivo
df = pd.read_csv("Dados/dados_historicos.csv")

## Primeiras Linhas
print(df.head())

## Dimensões[cite: 7]
print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])

## Nomes das colunas[cite: 7]
print(df.columns.tolist())

## Tipos das variáveis[cite: 7]
print(df.dtypes)

df.info()

## Resumo estatístico[cite: 7]
print(df.describe(include="all"))

## Quantidade de valores ausentes por coluna[cite: 7]
print("Dados Ausentes:")
print(df.isnull().sum())

# Remover duplicados[cite: 3, 7]
df = df.drop_duplicates()

# Dados duplicados[cite: 7]
print("Duplicados restantes:")
print(df.duplicated().sum())

## Outliers (método IQR)[cite: 3, 7]
colunas = ["temperatura", "vibracao", "consumo_energia", "latencia_rede",
           "carga_sistema", "erros_24h", "manutencoes_30d",
           "idade_equipamento_meses", "umidade", "fluxo_dados"]
for c in colunas:
    q1 = df[c].quantile(0.25)
    q3 = df[c].quantile(0.75)
    iqr = q3 - q1
    out = df[(df[c] < q1 - 1.5*iqr) | (df[c] > q3 + 1.5*iqr)]
    print(c, "outliers:", len(out))

## Analise exploratoria[cite: 3, 8]
print("\nFrequência de Falhas:\n", df["falha"].value_counts())
print("\nTaxa de Falha por Setor:\n", df.groupby("setor")["falha"].mean())
df[colunas].hist(figsize=(15, 8))
plt.tight_layout()
plt.show()

# Salva os dados sem duplicatas para o script do modelo utilizar
df.to_csv("Dados/dados_historicos_tratados.csv", index=False)