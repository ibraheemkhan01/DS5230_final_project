Vehicle Analytics & Recommendation System

Unsupervised ML • Clustering • PCA • Collaborative Filtering • Deep Learning

This repository contains the full pipeline for a vehicle-analytics project, including data ingestion, preprocessing, clustering, recommendation systems, and deep-learning embeddings. It supports PostgreSQL (local and AWS RDS), Kaggle dataset ingestion, and multiple ML experiments developed through Jupyter notebooks.

Repository Structure
Datasets & Raw Assets

cars_with_coords.csv
Cleaned dataset with geolocation fields used for clustering, PCA, and deep-learning experiments.

SQL Files

columns_all_tables.sql
Query to list all columns across all tables in the connected Postgres schema.

uci_data_profiling.sql
Initial profiling queries for the UCI Automobile dataset. Used during the first RDS setup and schema validation.

Python Scripts

create_schema.py
Creates the project’s database schema in Postgres. Replaces earlier notebook-based schema setup.

test_database_connection.py
Tests connectivity to the Postgres instance (local or AWS RDS). Supports .env file credential loading.

Jupyter Notebooks

datasets.ipynb
End-to-end pipeline for pulling Kaggle datasets, loading them into Postgres, and performing initial exploration.

geo_clustering.ipynb
Reference implementation for geographic clustering, including coordinate cleaning, K-means, GMM, and cluster visualization.

item_based_collab_filter.ipynb
Implements the item-based collaborative filtering recommender system:

user preference input

cosine similarity

filtering by price, year, odometer

top-N recommendation output

mvp_clustering_before_cleaning.ipynb
Early clustering experiments before full data preprocessing. Useful for comparing raw vs cleaned outcomes.

mvp_cars_final_Deep_learning.ipynb
Final deep-learning notebook implementing the autoencoder architecture:

71-dimensional input

128 → 64 → 16 latent → 64 → 128 layers

reconstruction loss

embedding extraction for recommendation

PCA visualization of learned embeddings

cross-validation against GMM clusters

Project Overview
1. Data Cleaning and Integration

Combined several Kaggle datasets

Addressed 30–40% missing values

Corrected invalid geolocation points

Encoded categorical variables

Applied standardized scaling

Engineered new features for clustering and PCA

2. Unsupervised Learning

PCA for dimensionality reduction (18 components explain 95% variance)

K-Means and Gaussian Mixture Models

Identification of 5–11 meaningful market clusters

Discovery of anomalies and outlier vehicles

3. Recommender Systems

Item-based collaborative filtering

Cosine similarity over normalized features

Range filtering for price, year, and odometer

Top-N recommendation results

4. Deep Learning Autoencoder

Encoder: 71 → 128 → 64 → 16 latent

Decoder: 16 → 64 → 128 → 71

Latent embeddings used for similarity search

Recommendations compared with collaborative filtering

PCA visualization confirms clustering consistency with GMM

5. Key Results

Collaborative filtering and deep learning agree on 4 of 5 recommendations

GMM produces cleaner, probabilistic, and more realistic clusters

PCA reveals meaningful axes such as drive type, age-value patterns, and engine characteristics

Future Improvements

Deploy the recommender using FastAPI

Add a Streamlit web interface for user interaction

Introduce a vector database (FAISS or pgvector) for embedding search

Build automated preprocessing and model-training pipelines

Team

Ibraheem Khan
Sristi Prasad
Patrick Nguyen
Northeastern University – DS5230
