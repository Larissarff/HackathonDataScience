```
# Análise dos Dados

## Desafio 1 — Escolha do Dataset

Optamos pelo **dataset antigo**, pois ele possui a variável `codigo_manutencao`, que apresenta as classificações **NORMAL**, **URGENTE** e **CRÍTICO**. Essas classificações estão diretamente relacionadas ao objetivo do projeto, que é identificar situações de risco nos equipamentos.

Além disso, o dataset novo possui **duas variáveis a menos**, reduzindo a quantidade de informações disponíveis para análise e para a construção do modelo.

## Desafio 2 — Variável `temperatura`

Durante a análise exploratória dos dados, foram identificados **valores discrepantes (outliers)** na variável `temperatura`, possivelmente relacionados a falhas de instrumentação ou problemas na coleta dos dados.

Em vez de substituir esses valores pela média ou mediana, optamos por **preservar os dados originais**, evitando introduzir alterações artificiais na base.

Por esse motivo, a variável `temperatura` foi **desconsiderada na etapa de modelagem**.

## Desafio 3 — Seleção das Variáveis

A seleção dos atributos foi realizada com base na sua relevância para a **identificação de falhas e situações críticas** nos equipamentos.

Foram priorizadas variáveis como:

- `vibracao`
- `consumo_energia`
- `latencia`
- `carga_sistema`
- `erros_recentes`
- `manutencoes`
- `idade_equipamento`
- `umidade`
- `fluxo_dados`

Além da acurácia, serão utilizadas métricas como **Precision**, **Recall** e **F1-Score** para avaliar o desempenho do modelo.

Essa abordagem permite uma avaliação mais completa, principalmente por se tratar de um problema de classificação em que a identificação correta das situações de risco é importante.

## Desafio 4 — Erro Sistemático de `Latencia_Redes`

Foi identificado um possível **erro sistemático na variável `Latencia_Redes`**.

Esse tipo de problema pode influenciar os resultados da análise e prejudicar o desempenho do modelo de classificação. Por isso, essa variável deverá ser analisada com atenção antes da etapa de treinamento, verificando a existência de padrões anormais ou inconsistências nos valores registrados.

## Modelo de Classificação

Para a etapa de modelagem, será utilizado o algoritmo **Random Forest**, aplicado a um problema de **classificação multiclasse**.

O objetivo é identificar a situação de cada equipamento, classificando-o em uma das seguintes categorias:

- `NORMAL`
- `URGENTE`
- `CRÍTICO`

O modelo utilizará as variáveis selecionadas durante a análise exploratória para identificar padrões relacionados às diferentes situações de risco.

O desempenho do modelo será avaliado por meio das métricas de **Precision**, **Recall**, **F1-Score** e **Acurácia**, evitando que a avaliação seja baseada exclusivamente na acurácia.
```