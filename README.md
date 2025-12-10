# Vehicle Analytics & Recommendation System
Unsupervised ML · Deep Learning · Clustering · PCA · Collaborative Filtering

This repository contains the full pipeline for our vehicle analytics project, including data ingestion, preprocessing, clustering, recommendation systems, and deep-learning embeddings.  
It supports PostgreSQL (local + AWS RDS), Kaggle dataset ingestion, and multiple ML experiments developed through Jupyter notebooks.

---

## Repository Structure

### Datasets & Raw Assets

#### `cars_with_coords.csv`
Cleaned dataset with geolocation fields used for clustering, PCA, and deep-learning experiments.

---

## SQL Files

### `columns_all_tables.sql`
Lists all columns across all tables in the Postgres schema.

### `uci_data_profiling.sql`
Initial profiling queries for the UCI Automobile dataset.  
Used during early AWS RDS schema validation.

---

## Python Scripts

### `create_schema.py`
Creates the project's database schema in Postgres.  
Ensures consistent and reproducible table creation.

### `test_database_connection.py`
Tests database connectivity to local or AWS RDS Postgres.  
Supports `.env` credential configuration.

---

## Jupyter Notebooks

### `datasets.ipynb`
Baseline end-to-end data pipeline:
- Pull Kaggle datasets using API/KaggleHub  
- Load datasets into Postgres  
- Preview and validate data  

---

### `geo_clustering.ipynb`
Reference notebook for geographical clustering:
- Latitude/longitude cleaning  
- K-Means and GMM clustering  
- Visual cluster analysis  

---

### `item_based_collab_filter.ipynb`
Implements item-based collaborative filtering:
- User preference template  
- Cosine similarity scoring  
- Range filtering (price, year, mileage)  
- Top-N recommendation output  

---

### `mvp_clustering_before_cleaning.ipynb`
Contains early clustering experiments **before** full preprocessing, useful for comparing raw vs cleaned data behavior.

---

### `mvp_cars_final_Deep_learning.ipynb`
Implements the final deep learning autoencoder:
- 71-dimensional input  
- Encoder → 16-dim latent space → decoder  
- Reconstruction loss  
- Embedding extraction for similarity search  
- PCA visualization of latent embeddings  
- Comparison vs collaborative filtering recommendations  

---

## Project Overview

This repository implements the full analytical workflow for market segmentation and vehicle recommendation.

### 1. Data Cleaning & Integration
- Merged multiple Kaggle datasets  
- Handled 30–40% missing values  
- Fixed invalid geographic points  
- Encoded categorical variables  
- Standard scaling  

### 2. Unsupervised Learning
- PCA for dimensionality reduction  
- K-Means clustering  
- Gaussian Mixture Models (GMM)  
- Identification of 5–11 clusters depending on preprocessing  
- Detection of outliers (e.g., Ferrari luxury outlier)  

### 3. Recommender Systems
- Item-based collaborative filtering  
- Cosine similarity across standardized features  
- Top-N recommendations  

### 4. Deep Learning Autoencoder
- Network: 71 → 128 → 64 → 16 → 64 → 128 → 71  
- Extracts meaningful latent embeddings  
- Embedding-based similarity search  
- PCA visualization shows structure similar to GMM clusters  

### 5. Results Summary
- Deep learning and CF recommenders agree on 4/5 results  
- GMM captures overlapping clusters more naturally than K-Means  
- PCA reveals interpretable axes:
  - Drive configuration  
  - Age-value tradeoff  
  - Engine efficiency  

---

## Future Improvements
- Deploy recommender with FastAPI  
- Add Streamlit user interface  
- Vector embeddings served via FAISS or pgvector  
- Automated cleaning + model training pipelines  

---

## Team
Ibraheem Khan  
Sristi Prasad  
Patrick Nguyen  
Northeastern University – DS5230
