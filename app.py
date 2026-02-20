import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Esse é o titulo do meu primeiro projeto StreamLit")
st.write("Esse é um texto qualquer.")

st.map()

st.button('Clique aqui')

st.file_uploader('Faça o upload do arquivo aqui')

st.text_input('Input de texto')

st.title("Aula 01 - Streamlit + Dataset Iris")

df = sns.load_dataset("iris")

#df = dataframe

st.subheader("Prévia do DataSet")
#st.dataframe(df)
st.dataframe(df.head())
st.dataframe(df.tail())
#na primeira vez demora renderizar

st.subheader("Dimensões")
st.write(f"Dimensões: {df.shape}")
#tupla - é um método
st.write(f"Linhas: {df.shape[0]}")
st.write(f"Colunas: {df.shape[1]}")

st.subheader("Tipos")
st.write(df.dtypes)

st.subheader("Resumo do DF")
st.write(df.describe())

st.sidebar.header("Filtros")
#st.sidebar.write("Teste")

species = df['species'].unique()
choice = st.sidebar.selectbox('Espécies: ', species)
st.sidebar.write(choice)

df_filtered = df[df["species"] == choice]

st.dataframe(df_filtered)