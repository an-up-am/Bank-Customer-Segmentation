import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bank Customer Segmentation", layout="wide")

st.title("🏦 Bank Customer Segmentation App")
st.write("Upload your dataset and automatically generate customer clusters")

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 📊 Input Data Preview")
    st.dataframe(df.head())

    # --- Feature Scaling ---
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df.select_dtypes(include='number'))

    # --- Train KMeans from scratch ---
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled)

    # --- PCA for 2D Visualization ---
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(scaled)
    df['PCA1'] = reduced[:, 0]
    df['PCA2'] = reduced[:, 1]

    # --- Show Clustered Data ---
    st.write("### 🧮 Clustered Data Preview")
    st.dataframe(df.head())

    # --- Visualization ---
    st.write("### 🎨 Cluster Visualization (PCA 2D)")
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=df, palette='Set2', ax=ax)
    st.pyplot(fig)

    # --- Download clustered data ---
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download Clustered Data as CSV",
        data=csv,
        file_name="clustered_customers.csv",
        mime="text/csv",
    )

else:
    st.info("👆 Please upload a CSV file to start.")
