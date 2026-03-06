import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Análise de Dados com o Dataset Tips no Streamlit")

st.title("Atividade - Streamlit + Dataset Tips")

df = sns.load_dataset("tips")

st.subheader("Prévia do DataSet")
st.dataframe(df)

st.subheader("Existe correlação entre o valor total da conta (total_bill) e o valor da gorjeta (tip)")