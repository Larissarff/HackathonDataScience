# Relatório Operacional de Manutenção Preditiva

**Operação Sinal Fraco — Data Crisis 2026**

**Central Integrada de Operações de Nova Aurora**

---

## 1. Resumo Executivo e Resposta Final

A pergunta central da operação — **"Quais unidades apresentam maior risco de falha crítica nas próximas horas?"** — foi respondida por meio do ranqueamento contínuo de probabilidades preditas pelo modelo **Random Forest**.

Caso a cidade envie as **20 equipes de manutenção disponíveis**, as unidades prioritárias para intervenção imediata são:

| Ranking | Unidade ID | Probabilidade de Falha | Classe Prevista |
| --- | --- | --- | --- |
| **1º** | `OP00327` | **80,50%** | 1 |
| **2º** | `OP00050` | **79,50%** | 1 |
| **3º** | `OP00104` | **78,50%** | 1 |
| **4º** | `OP00256` | **77,50%** | 1 |
| **5º** | `OP01137` | **77,50%** | 1 |
| **6º** | `OP00991` | **76,50%** | 1 |
| **7º** | `OP00116` | **74,50%** | 1 |
| **8º** | `OP00833` | **72,00%** | 1 |
| **9º** | `OP01094` | **70,00%** | 1 |
| **10º** | `OP01068` | **69,50%** | 1 |
| **11º** | `OP00891` | **69,50%** | 1 |
| **12º** | `OP00537` | **69,00%** | 1 |
| **13º** | `OP00280` | **68,50%** | 1 |
| **14º** | `OP00349` | **68,00%** | 1 |
| **15º** | `OP00209` | **68,00%** | 1 |
| **16º** | `OP00643` | **64,50%** | 1 |
| **17º** | `OP01131` | **64,50%** | 1 |
| **18º** | `OP00421` | **63,50%** | 1 |
| **19º** | `OP00090` | **62,50%** | 1 |
| **20º** | `OP01063` | **59,50%** | 1 |

---

## 2. Diagnóstico e Qualidade dos Dados (`preparacao_dos_dados.py`)

A execução do script de preparação analisou **10.000 unidades únicas** (totalizando 10.250 registros antes do expurgo de duplicatas no histórico).

* **Valores Ausentes:** Identificados nas variáveis `temperatura` (568 nulos), `vibracao` (580 nulos) e `latencia_rede` (453 nulos). Foram imputados via **mediana** para evitar distorções causadas por picos operacionais.


* **Tratamento de Outliers:** Identificados desvios expressivos via método IQR em `temperatura` (376 outliers, com pico máximo em $256{,}71^\circ\text{C}$), `vibracao` (231 outliers, máximo de $12{,}27$) e `latencia_rede` (295 outliers).


* **Decisão Operacional:** Devido aos outliers presentes nos dados de temperatura e a informação de que estariam sendo medidos de forma errônea, os dados ** foram descartados**, pois em telemetria industrial representam anomalias físicas que antecedem a quebra iminente, sendo cruciais para o aprendizado do modelo, e por se tratar de uma falha no medidor, não se é possível confiar em nenhum dos dados.




* **Comportamento por Setor:** O setor de **Energia** apresentou a maior taxa histórica de falhas (**15,95%**), seguido por Trânsito (9,94%), Telecom (9,79%), Água (8,96%) e Saúde (7,05%).



---

## 3. Avaliação de Modelos e Análise do Desempenho (`analise_dos_dados.py`)

Com uma proporção desbalanceada de falhas na base de treino (10,68% positivos vs. 89,32% normais), a **Acurácia** foi desconsiderada como métrica de sucesso.

O modelo principal (**Random Forest**) e o secundário (**KNN**) foram avaliados em dados não utilizados no treinamento (Holdout 25%):

### Resultados do Teste (Limiar de Decisão Ajustado = 0,35)

* **Recall (Sensibilidade):** `0.24` (24% das falhas reais foram detectadas no conjunto de teste)


* **Precision (Precisão):** `0.72` (72% das unidades classificadas como falha realmente falhariam)


* **F1-Score:** `0.36`

* **Matriz de Confusão:**

$$\begin{pmatrix} 2208 & 25 \\ 202 & 65 \end{pmatrix}$$


* **Verdadeiros Negativos (VN):** 2.208 unidades saudáveis classificadas corretamente.
* **Falsos Positivos (FP):** 25 alarmes falsos (custo operacional de vistoria preventiva).
* **Falsos Negativos (FN):** 202 falhas não detectadas (risco de paralisação).
* **Verdadeiros Positivos (VP):** 65 falhas identificadas com sucesso.



### Justificativa do Ajuste do Limiar

Em sistemas críticos de infraestrutura pública, o **Falso Negativo** (deixar uma unidade colapsar sem atendimento) é infinitamente mais caro do que um **Falso Positivo** (enviar uma equipe para vistoriar um equipamento saudável). A redução do limiar padrão de $0{,}50$ para $0{,}35$ permitiu alcançar uma **precisão de 72%**, garantindo alta assertividade ao deslocar as poucas equipes operacionais.

---

## 4. Conclusão e Plano de Ação para a Central de Operações

1. **Alocação Imediata:** As 20 equipes de manutenção devem ser despachadas urgentemente para as unidades da lista prioritária, iniciando pela `OP00327` (80,50% de probabilidade de colapso) até a `OP01063` (59,50%).


2. **Entregável Gerado:** O arquivo obrigatório `predicoes_equipe.csv` foi exportado com sucesso no diretório do projeto, contendo o ID, a probabilidade contínua e a classe prevista para toda a base de operação real.

### Integrantes:
Ana Mattos |
Heloiza Custódio |
Larissa Ferreira |
Lucas Frotte |
Pedro Nogueira |
Rafael Peçanha | 
