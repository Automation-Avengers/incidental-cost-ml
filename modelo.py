import pandas as pd
import numpy as np
import streamlit as st
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt

# Função para carregar os dados
def load_data(uploaded_file):
    df = pd.read_excel(uploaded_file)
    colunas_excluir = ["Key", "Type", "OBU", "Sum of Type"]
    df.drop(columns=colunas_excluir, inplace=True, errors="ignore")

    # Garantir que apenas colunas numéricas sejam usadas
    df = df.select_dtypes(include=[np.number])
    return df

# Função para detectar anomalias
def detect_anomalies(df, contamination=0.10):
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    # Aplicar Isolation Forest
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    df["Anomalia_IF"] = iso_forest.fit_predict(df_scaled)

    # Aplicar Local Outlier Factor (LOF)
    lof = LocalOutlierFactor(n_neighbors=5, contamination=contamination)
    df["Anomalia_LOF"] = lof.fit_predict(df_scaled)

    # Marcar anomalias (valores -1)
    df["Anomalia_Detectada"] = ((df["Anomalia_IF"] == -1) | (df["Anomalia_LOF"] == -1)).astype(int)

    return df

# Função para avaliar o modelo
def evaluate_model(df):
    anomalias = df["Anomalia_Detectada"].sum()
    normais = len(df) - anomalias

    # Garantir que há ambos os casos para cálculo de métricas
    if anomalias == 0 or normais == 0:
        return 0, 0, 0, np.array([[normais, 0], [0, anomalias]])

    # Cálculo da matriz de confusão baseado em um limite estatístico
    df["Anomalia_Real"] = (df.iloc[:, :-3] > df.iloc[:, :-3].mean() + 3 * df.iloc[:, :-3].std()).any(axis=1).astype(int)

    accuracy = accuracy_score(df["Anomalia_Real"], df["Anomalia_Detectada"])
    precision = precision_score(df["Anomalia_Real"], df["Anomalia_Detectada"], zero_division=0)
    recall = recall_score(df["Anomalia_Real"], df["Anomalia_Detectada"], zero_division=0)
    cm = confusion_matrix(df["Anomalia_Real"], df["Anomalia_Detectada"])

    return accuracy, precision, recall, cm

# Interface Web com Streamlit
st.title("Detecção de Anomalias em Dados Financeiros")
st.write("Carregue seu arquivo Excel para detectar anomalias nos dados financeiros.")

uploaded_file = st.file_uploader("Carregar arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write("📂 Dados carregados com sucesso!")
    st.dataframe(df.head())

    # Definir um valor fixo para contaminação
    contamination = 0.10  # 10% de anomalias esperadas

    if st.button("🔍 Detectar Anomalias"):
        df = detect_anomalies(df, contamination)
        accuracy, precision, recall, cm = evaluate_model(df)

        st.write(f"⚠️  Anomalias detectadas: {df['Anomalia_Detectada'].sum()}")

        # Exibir matriz de confusão
        st.write("📌 Matriz de Confusão:")
        st.write(cm)

        st.write(f"✅ Acurácia: {accuracy:.2f}")
        st.write(f"🎯 Precisão: {precision:.2f}")
        st.write(f"🔄 Recall: {recall:.2f}")

        # Visualização das anomalias
        st.write("📊 Distribuição das anomalias")
        fig, ax = plt.subplots()
        ax.hist(df["Anomalia_Detectada"], bins=3, edgecolor="black")
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["Normal", "Anomalia"])
        ax.set_ylabel("Frequência")
        st.pyplot(fig)

        # Permitir download do arquivo corrigido
        caminho_saida = "anomalias_detectadas.xlsx"
        df.to_excel(caminho_saida, index=False)

        with open(caminho_saida, "rb") as file:
            st.download_button("📥 Baixar Resultados", file, file_name=caminho_saida)
