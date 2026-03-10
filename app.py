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

