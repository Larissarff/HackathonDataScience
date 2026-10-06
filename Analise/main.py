import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##Leitura de arquivo
df = pd.read_csv("dados_historicos.csv")

##Primeiras Linhas
print(df.head())

##Dimensões
print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])

##Nomes das colunas
print(df.columns.tolist())

##Tipos das variáveis
print(df.dtypes)


df.info()

##Resumo estatístico
print(df.describe(include="all"))

##Quantidade de valores ausentes por coluna
print("Dados Ausentes:")
print(df.isnull().sum())

#remover duplicados
df = df.drop_duplicates()

#Dados duplicados
print("Duplicados:")
print(df.duplicated().sum())
##print(df.duplicated(subset=["unidade_id"]).sum())

##Outliers (método IQR)
colunas = ["temperatura", "vibracao", "consumo_energia", "latencia_rede",
           "carga_sistema", "erros_24h", "manutencoes_30d",
           "idade_equipamento_meses", "umidade", "fluxo_dados"]
for c in colunas:
    q1 = df[c].quantile(0.25)
    q3 = df[c].quantile(0.75)
    iqr = q3 - q1
    out = df[(df[c] < q1 - 1.5*iqr) | (df[c] > q3 + 1.5*iqr)]
    print(c, "outliers:", len(out))


##Analise exploratoria
print(df["falha"].value_counts())
print(df.groupby("setor")["falha"].mean())
df[colunas].hist(figsize=(15, 8))







