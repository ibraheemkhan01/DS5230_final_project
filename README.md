Vehicle Analytics & Recommendation System

Unsupervised ML · Clustering · PCA · Collaborative Filtering · Deep Learning

This repository contains the full pipeline for our vehicle-analytics project, including data ingestion, preprocessing, clustering, recommendation systems, and deep-learning embeddings.
It supports PostgreSQL (local + AWS RDS), Kaggle dataset ingestion, and multiple ML experiments developed through Jupyter notebooks.

Repository Structure
Datasets & Raw Assets
cars_with_coords.csv

Cleaned dataset with geolocation fields used for clustering, PCA, and deep-learning experiments.

SQL Files
columns_all_tables.sql

Query to list all columns across all tables in the connected Postgres schema.

uci_data_profiling.sql

Initial profiling queries used for the UCI Automobile dataset.
Part of the first RDS setup and schema verification.

Python Scripts
create_schema.py

Creates the project’s database schema in Postgres.
Replaces earlier ad-hoc SQL blocks or notebooks and ensures reproducible schema creation.

test_database_connection.py

Simple connectivity test to the Postgres instance (local or AWS RDS).
Supports .env files for credentials.

Jupyter Notebooks
datasets.ipynb

End-to-end pipeline for:

Pulling Kaggle datasets using API/KaggleHub

Loading them into Postgres

Performing basic previews & sanity checks

This notebook establishes the project’s data baseline.

geo_clustering.ipynb

Reference implementation for geographical clustering, including experiments with:

Latitude/longitude cleaning

K-means and GMM clustering

Visualizing cluster regions

item_based_collab_filter.ipynb

Core implementation of the item-based collaborative filtering recommender:

User preference template

Similarity computation (cosine)

Filtering by price/year/odometer ranges

Top-N recommendation output

Fully functional & tested with final results.

mvp_clustering_before_cleaning.ipynb

Intermediate notebook containing clustering experiments before full preprocessing.
Useful for comparing raw vs cleaned data behavior.

mvp_cars_final_Deep_learning.ipynb

Final notebook implementing the deep learning autoencoder, including:

71-dimensional input pipeline

Encoder → latent (16-dim embeddings) → decoder architecture

Reconstruction loss

Embedding extraction for similarity search

Comparison vs collaborative filtering

PCA visualization of learned embeddings

This is the model used to cross-validate the cluster structure independently of GMM.

Supporting Files
.gitignore

Standard ignore rules for Python/Jupyter/virtual-envs and datasets.

Project Overview

This repo implements the full analytical stack for used-vehicle market segmentation and recommendation:

1. Data Cleaning & Integration

Combining 3+ Kaggle datasets

Handling 30–40% missing values

Fixing invalid geolocation points

Encoding categorical variables

Standardized scaling

2. Unsupervised Learning

PCA for dimensionality reduction (18 components → 95% variance explained)

K-Means and Gaussian Mixture Models (GMM)

Identification of 5–11 market clusters depending on feature engineering

Discovery of anomalous vehicles (e.g., Ferrari outlier)

3. Recommender Systems

Item-based collaborative filtering

Cosine similarity over normalized feature sets

Range-based filtering on price, year, mileage

4. Deep Learning Autoencoder

71 → 128 → 64 → 16-dim latent space → 64 → 128 → 71

Embedding-based similarity recommendations

PCA visualization shows latent clustering consistent with GMM

5. Results

Collaborative filtering and deep learning agree on 4/5 recommendations

GMM captures overlapping clusters better than K-means

PCA reveals meaningful axes: drive type, age-value tradeoff, engine efficiency

Future Improvements

User vs item-based filtering

Add Streamlit UI for user interaction

Build automated pipelines for cleaning & model training

Team

Ibraheem Khan, Sristi Prasad, Patrick Nguyen
Northeastern University – DS5230
