import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 1. Carregar dados limpos do main.py e dados de operação real

df = pd.read_csv("Dados/dados_historicos_tratados.csv")
operacao_real = pd.read_csv("Dados/operacao_real.csv")

# 2. Seleção de Features

num_cols = ["temperatura", "vibracao", "consumo_energia", "latencia_rede",
            "carga_sistema", "erros_24h", "manutencoes_30d",
            "idade_equipamento_meses", "umidade", "fluxo_dados"]
cat_cols = ["setor"]

X = df[num_cols + cat_cols]
y = df["falha"]

# 3. Divisão Treino/Teste

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=2026, stratify=y
)

# 4. Pipeline de Pré-processamento

preprocessor = ColumnTransformer(
    transformers=[
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ]), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ]
)

# 5. Treinamento: Random Forest (Principal) e KNN (Secundário)

rf_pipe = Pipeline([
    ("prep", preprocessor),
    ("rf", RandomForestClassifier(n_estimators=200, random_state=2026, class_weight="balanced"))
])
knn_pipe = Pipeline([
    ("prep", preprocessor),
    ("knn", KNeighborsClassifier(n_neighbors=5))
])

rf_pipe.fit(X_train, y_train)
knn_pipe.fit(X_train, y_train)

# 6. Avaliação (Limiar focado em Recall)

LIMIAR = 0.35
prob_rf_test = rf_pipe.predict_proba(X_test)[:, 1]
pred_rf_test = (prob_rf_test >= LIMIAR).astype(int)

print(f"--- Desempenho Random Forest no Teste (Limiar {LIMIAR}) ---")
print(f"Recall: {recall_score(y_test, pred_rf_test):.2f}")
print(f"Precision: {precision_score(y_test, pred_rf_test):.2f}")
print(f"F1-Score: {f1_score(y_test, pred_rf_test):.2f}")
print("Matriz de Confusão:\n", confusion_matrix(y_test, pred_rf_test))

# 7. Previsão na Operação Real e Arquivo Final

X_op = operacao_real[num_cols + cat_cols]
prob_op = rf_pipe.predict_proba(X_op)[:, 1]

predicoes_equipe = pd.DataFrame({
    "unidade_id": operacao_real["unidade_id"],
    "probabilidade_falha": np.round(prob_op, 4),
    "classe_prevista": (prob_op >= LIMIAR).astype(int)
})
predicoes_equipe.to_csv("predicoes_equipe.csv", index=False)

# 8. RESPOSTA À PERGUNTA FINAL: TOP 20 UNIDADES PRIORITÁRIAS

top_20 = predicoes_equipe.sort_values(by="probabilidade_falha", ascending=False).head(20)

print("\n=================================================================")
print("RESPOSTA FINAL: 20 UNIDADES COM MAIOR RISCO DE FALHA CRÍTICA")
print("=================================================================")
print(top_20.to_string(index=False))