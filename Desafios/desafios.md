
# Desafios

 ## Desafio 1 — Escolha do Dataset

 Optamos pelo **dataset antigo**, pois ele possui a variável `codigo_manutencao`, que apresenta as classificações:

 - **NORMAL**
- **URGENTE**
- **CRÍTICO**

 Essas classificações estão diretamente relacionadas ao objetivo do projeto, que é **identificar situações de risco nos equipamentos**.

 Além disso, o dataset novo possui **duas variáveis a menos**, reduzindo a quantidade de informações disponíveis para a análise e para a construção do modelo.

---

 ## Desafio 2 — Variável `temperatura`

 Durante a análise exploratória dos dados, foram identificados **valores discrepantes (outliers)** na variável `temperatura`, possivelmente relacionados a falhas de instrumentação ou problemas na coleta dos dados.

 Em vez de substituir esses valores pela média ou mediana, optamos por **preservar os dados originais**, evitando introduzir alterações artificiais na base.

 Por esse motivo, a variável `temperatura` foi **desconsiderada na etapa de modelagem**.

---

 ## Desafio 3 — Seleção das Variáveis

 A seleção dos atributos foi realizada com base na sua relevância para a **identificação de falhas e situações críticas** nos equipamentos.

 Foram priorizadas as seguintes variáveis:

 - `vibracao`
- `consumo_energia`
- `latencia`
- `carga_sistema`
- `erros_recentes`
- `manutencoes`
- `idade_equipamento`
- `umidade`
- `fluxo_dados`

 Além da **acurácia (Accuracy)**, serão utilizadas métricas como:

 - **Precision**
- **Recall**
- **F1-Score**

 Essas métricas permitem uma avaliação mais completa do desempenho do modelo, principalmente por se tratar de um problema de classificação em que a **identificação correta das situações de risco** é importante.

---

 ## Desafio 4 — Erro Sistemático de `Latencia_Redes`

 Foi identificado um possível **erro sistemático na variável `Latencia_Redes`**.

 Esse tipo de problema pode influenciar os resultados da análise e prejudicar o desempenho do modelo de classificação.

 Por isso, essa variável deverá ser analisada com atenção antes da etapa de treinamento, verificando:

 - existência de valores anormais;
- inconsistências nos registros;
- padrões repetitivos ou inesperados;
- possíveis problemas no processo de coleta;
- impacto da variável no desempenho do modelo.

 Após essa análise, será avaliado se a variável deverá ser **corrigida, transformada ou removida** da etapa de modelagem.

---

 ## Conclusão

 A análise inicial permitiu identificar características importantes do dataset e possíveis problemas de qualidade nos dados.

 A estratégia adotada será **preservar os dados originais sempre que possível**, evitando alterações artificiais, enquanto variáveis que apresentarem problemas relevantes serão avaliadas individualmente.

 Com isso, a próxima etapa será realizar o **tratamento e preparação dos dados**, seguida pelo treinamento e avaliação dos modelos de classificação utilizando métricas como **Accuracy, Precision, Recall e F1-Score**.