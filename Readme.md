# 🧠 Bank Customer Segmentation using Clustering

This project uses **Unsupervised Machine Learning** to segment bank customers into distinct behavioral groups for marketing and business strategy purposes.

---

## 📌 Project Summary

- **Goal**: Cluster customers to target personalized offers
- **Techniques**: EDA, Feature Scaling, Outlier Detection, K-Means, Hierarchical Clustering, PCA
- **Libraries**: pandas, matplotlib, seaborn, scikit-learn, scipy

---

## 📁 Files in This Repo

| File                         | Purpose                            |
|------------------------------|------------------------------------|
| `Bank_Segmentation.ipynb`    | Jupyter Notebook with code & output |
| `bank_data.csv`              | Dataset used for clustering        |
| `requirements.txt`           | List of required Python packages   |
| `.gitignore`                 | Ignored files for clean GitHub repo |
| `README.md`                  | Project overview (this file)       |

---

## 📊 Clustering Techniques Used

### 🔁 K-Means Clustering
- Elbow method for optimal k
- Silhouette Score: **0.452**
- Visualized using **PCA** and **pairplots**

### 🧬 Hierarchical Clustering
- Dendrogram for structure
- Silhouette Score: **0.393**

---

## 📈 Visualization Tools
- Boxplots, KDE, Correlation Heatmap
- PCA-based 2D cluster visualization

---

## 🧪 Evaluation

| Criteria               | Hierarchical           | K-Means                  |
|------------------------|------------------------|--------------------------|
| **Silhouette Score**   | 0.393                  | 0.452                    |
| **Interpretability**   | Dendrogram             | Requires fixed `k`       |
| **Scalability**        | ❌ Poor on large data   | ✅ Highly scalable        |

---

## 🚀 Run in Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/an-up-am/Bank-Customer-Segmentation/blob/main/Bank_Segmentation.ipynb)

---

## 👨‍💻 Developed By

**Anupam Chauhan** 

📫 [LinkedIn](https://www.linkedin.com/in/anupam-iit-kgp/)  
