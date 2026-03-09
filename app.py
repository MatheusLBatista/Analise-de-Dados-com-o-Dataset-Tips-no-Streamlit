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
