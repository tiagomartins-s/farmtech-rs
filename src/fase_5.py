
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def executar_fase_5():
    st.header("Fase 5 - Análise de Dados de Produtividade Agrícola")

    uploaded_file = st.file_uploader("Envie o arquivo crop_yield.csv", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Pré-visualização dos Dados")
        st.write(df.head())

        st.subheader("Estatísticas Descritivas")
        st.write(df.describe())

        st.subheader("Seleção de Coluna Numérica para Clusterização")
        numerical_columns = df.select_dtypes(include=np.number).columns.tolist()
        feature = st.selectbox("Escolha a coluna para clusterização", numerical_columns)

        if feature:
            df_cluster = df[[feature]].copy()

            scaler = StandardScaler()
            df_scaled = scaler.fit_transform(df_cluster)

            n_clusters = st.slider("Número de clusters (K)", 2, 10, 3)

            model = KMeans(n_clusters=n_clusters, random_state=0)
            clusters = model.fit_predict(df_scaled)

            df['cluster'] = clusters

            st.subheader("Resultados da Clusterização")
            st.write(df[[feature, 'cluster']].head())

            st.subheader("Visualização dos Clusters")
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=feature, hue='cluster', multiple='stack', ax=ax)
            st.pyplot(fig)
