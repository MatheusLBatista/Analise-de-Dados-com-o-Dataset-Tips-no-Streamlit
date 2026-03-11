# Matheus Lucas Batista - ADS 2024

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Atividade - Streamlit + Dataset Tips")

df = sns.load_dataset("tips")

st.subheader("Prévia do DataSet")
st.dataframe(df)

st.subheader("1 - Existe correlação entre o valor total da conta (total_bill) e o valor da gorjeta (tip)?")

fig, ax = plt.subplots()

sns.regplot(
    data = df, 
    x = "total_bill",
    y = "tip",
    ax = ax
)

ax.set_title("Correlação entre valor total da conta e valor da gorjeta")
ax.set_xlabel("Valor da conta")
ax.set_ylabel("Gorjetas")

st.pyplot(fig)

st.write("Sim, há uma correlação positiva entre o valor total da conta e o valor da gorjeta. À medida que o valor total da conta aumenta, o valor da gorjeta também tende a aumentar. Isso se torna visível no gráfico, onde os pontos apresentados formam uma tendência ascendente, evidenciando que os clientes tendem a dar gorjetas maiores quando a conta é mais cara.")

st.subheader("2 - Quanto maior a conta, maior tende a ser a gorjeta?")

corr = df['total_bill'].corr(df['tip'])
st.write("Coeficiente de correlação:", corr)

st.write("O coeficiente de correlação entre total_bill e tip foi de aproximadamente 0.67, indicando uma correlação positiva entre moderada e forte. No entando, a correlação não é perfeita pois existem variações nos comportamentos dos clientes.")

st.subheader("3 - Qual dia da semana apresenta a maior média de gorjeta? Mostre isso visualmente e explique sua conclusão.")

weekday_average = df.groupby('day')['tip'].mean()

st.write(weekday_average)

sns.barplot(
    data = df,
    x = 'day',
    y = 'tip',
    estimator = 'mean',
    ax = ax
)

st.pyplot(fig)

st.write("Com base no gráfico de barras acima, podemos visualizar os dias com maiores gorjetas por meio da média. Sendo domingo o dia com maior gorjetas.")

st.subheader("4 - Qual dia da semana possui o maior faturamento total do restaurante, considerando a soma de total_bill?")

faturamento = df.groupby("day")["total_bill"].sum()

st.write("Faturamento total por dia: ", faturamento)

sns.barplot(
    data = df,
    x = "day",
    y = "total_bill",
    estimator = sum,
    ax = ax
)

st.pyplot(fig)

st.write("Com base no gráfico acima, podemos visualizar os dias com maior faturamento total do restaurante, considerando a soma dos valores das contas e gorjetas.")

st.subheader("5 - Existe relação entre o número de pessoas na mesa (size) e o valor da gorjeta (tip)?")

fig, ax = plt.subplots()

sns.regplot(
    data=df,
    x="size",
    y="tip",
    ax=ax
)

ax.set_title("Correlação entre número de pessoas e valor da gorjeta")
ax.set_xlabel("Número de pessoas")
ax.set_ylabel("Gorjetas")

st.pyplot(fig)

corr = df['size'].corr(df['tip'])

st.write('Correlação: ', corr)

st.write("Existe uma correlação positiva entre o número de pessoas na mesa e o valor da gorjeta, indicando que, em geral, mesas com mais pessoas tendem a receber gorjetas maiores. No entanto, a correlação não é muito forte, sugerindo que outros fatores também influenciam o valor da gorjeta.")

st.subheader("6 - Existe relação entre o número de pessoas na mesa (size) e o valor total da conta (total_bill)?")

fig, ax = plt.subplots()

sns.regplot(
    data=df,
    x="size",
    y="total_bill",
    ax=ax
)

ax.set_title("Correlação entre número de pessoas e valor total da conta")
ax.set_xlabel("Número de pessoas")
ax.set_ylabel("Valor total da conta")

st.pyplot(fig)

corr = df["size"].corr(df["total_bill"])

st.write("Correlação:", round(corr,2))

st.write("Existe uma correlação positiva entre o número de pessoas na mesa e o valor total da conta, indicando que, em geral, mesas com mais pessoas tendem a ter contas maiores. No entanto, a correlação não é muito forte, em torno de 0.6, sugerindo que outros fatores também influenciam o valor total da conta.")

st.subheader("7 - Qual é o valor médio gasto por pessoa em cada dia da semana?")

df['spending_per_person'] = df['total_bill'] / df['size']

average_spending_per_day = df.groupby('day')['spending_per_person'].mean()

fig, ax = plt.subplots()

sns.barplot(
    data=df,
    x="day",
    y="spending_per_person",
    estimator=np.mean,
    ax=ax
)

ax.set_title("Valor médio gasto por pessoa por dia")
ax.set_ylabel("Gasto médio por pessoa")
ax.set_xlabel("Dia da semana")

st.pyplot(fig)

st.write("O valor médio gasto por pessoa em cada dia da semana varia, com o domingo apresentando o maior gasto médio por pessoa, seguido pelo sábado. Os dias de semana tendem a ter um gasto médio por pessoa mais baixo em comparação com os fins de semana, possivelmente devido a diferentes padrões de consumo e comportamento dos clientes durante a semana e nos fins de semana.")

st.subheader("8 - Homens e mulheres deixam gorjetas diferentes, em média?")
tip_per_gender = df.groupby("sex")["tip"].mean()

st.write(tip_per_gender)

fig, ax = plt.subplots()

sns.barplot(
    data=df,
    x="sex",
    y="tip",
    estimator=np.mean,
    ax=ax
)

ax.set_title("Média de gorjetas por gênero")
ax.set_xlabel("Gênero")
ax.set_ylabel("Média de gorjetas")

st.pyplot(fig)

st.write("Sim, há uma pequena diferença na média de gorjetas deixadas por homens e mulheres. De acordo com os dados, os homens tendem a deixar gorjetas maiores em média do que as mulheres.")

st.subheader("9 - Fumantes e não fumantes apresentam comportamentos diferentes em relação ao valor da gorjeta?")

tip_per_smoker = df.groupby("smoker")['tip'].mean()

st.write(tip_per_smoker)

fig, ax = plt.subplots()

sns.barplot(
    data = df,
    x = 'smoker', 
    y = 'tip',
    estimator = np.mean,
    ax = ax
)

ax.set_title("Média de gorjetas por fumantes")
ax.set_xlabel("Fumante")
ax.set_ylabel("Média de gorjetas")

st.pyplot(fig)

st.write("Sim, há uma diferença muito pequena na média de gorjetas deixadas por fumantes e não fumantes. De acordo com os dados, os fumantes tendem a deixar gorjetas maiores em média do que os não fumantes.")

st.subheader("10 - O turno da refeição (time) influencia no valor da conta ou da gorjeta?")

tip_per_time = df.groupby("time")['tip'].mean()

st.write(tip_per_time)

fig, ax = plt.subplots()

sns.barplot(
    data = df,
    x = 'time',
    y = 'tip',
    estimator = np.mean,
    ax = ax
)

ax.set_title("Média de gorjetas por refeição")
ax.set_xlabel("Refeições")
ax.set_ylabel("Média de gorjetas")

st.pyplot(fig)

st.write("Sim, como visto no gráfico de barras, o turno da refeição influencia no valor da gorjeta. De acordo com os dados, as refeições durante o jantar tendem a receber gorjetas maiores em média do que as refeições durante o almoço.")

st.subheader("11 - Qual grupo parece deixar a maior gorjeta proporcional à conta?")

df['tip_porcentage'] = df['tip'] / df['total_bill'] * 100

for col in ['sex', 'smoker', 'time', 'day']:
    st.write(f"Analisando a coluna {col}:")
    st.write(df.groupby(col)['tip_porcentage'].mean().round(2))

    fig, ax = plt.subplots()
    sns.barplot(
        data=df,
        x=col,
        y='tip_porcentage',
        estimator=np.mean,
        ax=ax
    )
    ax.set_title(f"Gorjeta proporcional por {col}")
    ax.set_xlabel(col)
    ax.set_ylabel("Gorjeta (%)")
    st.pyplot(fig)

st.write("Com base na análise dos gráficos, os grupos que tendem a deixar a maior gorjeta proporcional à conta são: mulheres, fumantes, clientes do almoço e clientes de sexta-feira.")

st.subheader("12 - Existem valores atípicos (outliers) no valor da conta ou da gorjeta?")

st.write("Boxplot do valor total da conta")

fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    y="total_bill",
    ax=ax
)

ax.set_ylabel("Valor da conta")

st.pyplot(fig)

st.write("Boxplot do valor da gorjeta")

fig, ax = plt.subplots()

sns.boxplot(
    data=df,
    y="tip",
    ax=ax
)

ax.set_ylabel("Gorjeta")

st.pyplot(fig)

st.write("Existem valores atípicos tanto no valor total da conta e da gorjeta. No gráfico de boxplot do valor total da conta e de gorjeta, podemos observar que há alguns pontos acima do limite superior. A influência desses outliers pode ser significativa, pois eles podem distorcer as médias e afetam a interpretação dos dados. É importante considerar esses outliers ao analisar o comportamento dos clientes e ao tomar decisões com base nesses dados.")

st.subheader("13 - As distribuições de total_bill e tip são equilibradas ou concentradas em determinadas faixas de valores?")

fig, ax = plt.subplots()

sns.histplot(
    data = df,
    x = 'total_bill',
    kde = True,
    bins = 20,
    ax = ax
)

ax.set_xlabel("Valor total da conta")

st.pyplot(fig)
st.write("A distribuição do valor total da conta é concentrada em faixas de valores mais baixos, com a maioria das contas situando-se entre 10 e 30 dólares. Há uma barra longa que se estende para valores mais altos, indicando que existem algumas contas maiores, porém a maioria dos dados está concentrada em torno de valores mais baixos.")

st.subheader("14 - Se você fosse gerente do restaurante, quais insights esse dataset oferece sobre o comportamento dos clientes?")

st.write("""
Com base nas análises realizadas, os principais insights são:

1. **Foco no fim de semana**: sábado e domingo concentram o maior faturamento. Vale reforçar equipe e estoque nesses dias.

2. **Jantar é mais lucrativo em gorjetas**: clientes do jantar tendem a deixar gorjetas maiores. Investir no atendimento noturno pode aumentar a satisfação.

3. **Grupos grandes geram mais receita**: mesas com mais pessoas resultam em contas maiores. Priorizar assentos para grupos é estratégico.

4. **Perfil do cliente**: homens e fumantes tendem a deixar gorjetas ligeiramente maiores. Conhecer o perfil do cliente ajuda a personalizar o atendimento.

5. **Outliers**: algumas contas muito altas sugerem eventos especiais. Criar pacotes ou menus para grupos pode capturar esse público.
""")