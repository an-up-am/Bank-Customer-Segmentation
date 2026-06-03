# Bank Customer Segmentation using Unsupervised Machine Learning

A data analytics project that segments bank customers into distinct behavioral groups using K-Means and Hierarchical Clustering — enabling targeted marketing campaigns and personalized credit strategies.

---

## Problem Statement

A private sector bank wanted to move away from one-size-fits-all promotional campaigns. The goal was to segment customers based on their financial behavior so that marketing efforts could be more cost-efficient, targeted, and effective.

---

## Objective

Apply unsupervised machine learning to identify hidden customer patterns and group them into meaningful clusters. These insights help the bank:

- Understand distinct customer types (e.g., high spenders, conservative payers, credit-dependent users)
- Customize product recommendations and promotional offers
- Improve marketing ROI by reducing wasteful outreach

---

## Dataset Overview

~20,000 anonymized customer records with the following features:

| Feature | Description |
|---|---|
| `SPENDING` | Average amount spent by the customer |
| `ADVANCE_PAYMENTS` | Total advance payments made |
| `PROBABILITY_OF_FULL_PAYMENTS` | Likelihood of paying full balance |
| `CURRENT_BALANCE` | Current account balance |
| `CREDIT_LIMIT` | Credit card / account limit |
| `MIN_PAYMENT_AMT` | Minimum monthly payment amount |
| `MAX_SPENT_IN_SINGLE_SHOPPING` | Highest spend in a single transaction |

> Since features vary significantly in scale, **StandardScaler** was applied before clustering.

---

## Techniques & Tools

- **EDA** — Distribution analysis, outlier detection, correlation heatmap
- **Feature Scaling** — StandardScaler for distance-based algorithms
- **K-Means Clustering** — Optimal k via Elbow Method + Silhouette Score
- **Hierarchical Clustering** — Dendrogram-based analysis
- **PCA** — 2D dimensionality reduction for cluster visualization
- **Streamlit** — Interactive web app for segmentation exploration

**Libraries:** `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, `streamlit`

---

## Model Evaluation

| Criteria | Hierarchical | K-Means |
|---|---|---|
| Silhouette Score | 0.393 | **0.452** |
| Interpretability | Dendrogram | Fixed k required |
| Scalability | Slow on large data | Highly scalable |

**K-Means (k=3) was selected** as the final model based on higher silhouette score and scalability.

---

## Customer Segments Identified

Three distinct clusters emerged from the analysis:

- **Cluster 0 — Conservative Payers:** Low spending, high probability of full payments, low credit utilization
- **Cluster 1 — High Spenders:** High spending and balance, significant single-transaction purchases
- **Cluster 2 — Credit-Dependent Users:** Low balance, high advance payments, lower payment probability

---

## Repository Structure

| File | Description |
|---|---|
| `Bank_Customer_Segmentation.ipynb` | Full notebook — EDA, preprocessing, clustering, profiling |
| `Bank_Customer_Segmentation.csv` | Dataset used for analysis |
| `app.py` | Streamlit web app for interactive segmentation |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Clean repo structure |

---

## 🚀 Run the Project

**Web App (Live Demo)**

**(https://bank-customers-segmentation.streamlit.app/)**  

**Jupyter Notebook (Google Colab)**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/an-up-am/Bank-Customer-Segmentation/blob/main/Bank_Customer_Segmentation.ipynb)

**Run Locally**

```bash
git clone https://github.com/your-username/bank-customer-segmentation
cd bank-customer-segmentation
pip install -r requirements.txt
streamlit run app.py
```

---

## 👤 Author

**Anupam Chauhan**
[LinkedIn](#) · [GitHub](#)
