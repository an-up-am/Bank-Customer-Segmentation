# 🏦 Bank Customer Segmentation using Machine Learning

🎯 **[Live Demo → Click Here](https://bank-customers-segmentation.streamlit.app/)**  
🚀 Built and deployed by **Anupam Chauhan | Data Analyst, Accenture AI**

---

## 📌 Project Overview

This project applies **Unsupervised Machine Learning** to segment bank customers into distinct behavioral groups — helping banks and marketers target customers with **personalized offers** and **data-driven strategies**.

---

## 🧠 Techniques & Tools

- **Goal:** Cluster customers for marketing segmentation  
- **Techniques:** EDA, Feature Scaling, Outlier Detection, K-Means, Hierarchical Clustering, PCA  
- **Libraries:** `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `streamlit`

---

## 📁 Files in This Repository

| File | Description |
|------|--------------|
| `Bank_Customer_Segmentation.ipynb` | Complete Jupyter Notebook with EDA, training & clustering |
| `Bank_Customer_Segmentation.csv` | Dataset used for model training |
| `app.py` | Streamlit web app for interactive segmentation |
| `requirements.txt` | Python dependencies for local / cloud deployment |
| `.gitignore` | Clean GitHub repo structure |
| `README.md` | Project documentation (this file) |

---

## 📊 Clustering Techniques Used

### 🔹 **K-Means Clustering**
- Optimal cluster count using **Elbow Method**
- **Silhouette Score:** `0.452`
- **Visualized with PCA** for 2D cluster mapping

### 🔹 **Hierarchical Clustering**
- Dendrogram visualization
- **Silhouette Score:** `0.393`

---

## 📈 Visualization & Analysis

- Boxplots and KDE plots for feature distribution  
- Correlation heatmap for feature relationships  
- PCA-based visualizations for cluster interpretation  

---

## 🧪 Model Evaluation

| Criteria | Hierarchical | K-Means |
|-----------|--------------|---------|
| **Silhouette Score** | 0.393 | 0.452 |
| **Interpretability** | ✅ Dendrogram | ⚙️ Fixed `k` required |
| **Scalability** | ❌ Slow on large data | ✅ Highly scalable |

---

## 🚀 Try It Yourself

### ▶️ **Run the Web App**
👉 [Live Streamlit App](https://bank-customers-segmentation.streamlit.app/)

### 💻 **Run the Notebook**
Open directly in Google Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/an-up-am/Bank-Customer-Segmentation/blob/main/Bank_Customer_Segmentation.ipynb)

---

## 👨‍💻 Developed By

**Anupam Chauhan**  
Data Analyst | Accenture AI  

📫 [LinkedIn](https://www.linkedin.com/in/anupam-iit-kgp/)  
⭐ Star this repo if you found it useful!

---

