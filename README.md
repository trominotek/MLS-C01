# MLS-C01

## Index

- [Feature Engineering](#feature-engineering)
  - [1. Data Cleaning](#1-data-cleaning)
  - [2. Feature Creation](#2-feature-creation)
  - [3. Feature Selection](#3-feature-selection)
  - [4. Feature Transformation](#4-feature-transformation)
  - [5. Handling Imbalanced Data](#5-handling-imbalanced-data)

## Feature Engineering

### 1. Data Cleaning
- [1.1 Handling Missing Values](#11-handling-missing-values)
- [1.2 Removing Duplicates](#12-removing-duplicates)
- [1.3 Outlier Detection and Treatment](#13-outlier-detection-and-treatment)
- [1.4 Data Normalization and Standardization](#14-data-normalization-and-standardization)

### 2. Feature Creation
- [2.1 Polynomial Features](#21-polynomial-features)
- [2.2 Interaction Terms](#22-interaction-terms)
- [2.3 Binning](#23-binning)
- [2.4 Domain-Specific Feature Engineering](#24-domain-specific-feature-engineering)

### 3. Feature Selection
- [3.1 Filter Methods](#31-filter-methods)
- [3.2 Wrapper Methods](#32-wrapper-methods)
- [3.3 Embedded Methods](#33-embedded-methods)
- [3.4 Dimensionality Reduction (e.g., PCA, LDA)](#34-dimensionality-reduction-eg-pca-lda)

### 4. Feature Transformation
- [4.1 Scaling and Normalization](#41-scaling-and-normalization)
- [4.2 Logarithmic and Power Transformations](#42-logarithmic-and-power-transformations)
- [4.3 Encoding Categorical Variables](#43-encoding-categorical-variables)
- [4.4 Handling Skewed Data](#44-handling-skewed-data)

### 5. Handling Imbalanced Data
- [5.1 Over-Sampling Techniques (e.g., SMOTE)](#51-over-sampling-techniques-eg-smote)
- [5.2 Under-Sampling Techniques](#52-under-sampling-techniques)
- [5.3 Synthetic Data Generation](#53-synthetic-data-generation)
- [5.4 Cost-Sensitive Learning](#54-cost-sensitive-learning)

# MLS-C01

## Feature Engineering
Preprocessing, transforming , cleaning data before it is used for ML model traning or Inference.

### 1. Data Cleaning
- **1.1 Handling Missing Values**
   If a feature is missing in more than 70% of the data, drop it. For features with 70% or fewer missing values, fill in the gaps using the mean or median (for numerical features) or the mode (for categorical features). This ensures data integrity while handling missing values efficiently.
   [imputation](MLS-C01/Data_Cleaning/imputation.py)
   [Drop Feature](MLS-C01/Data_Cleaning/drop_feature.py)
- **1.2 Removing Duplicates**
   [Remove Dupes](MLS-C01/Data_Cleaning/remove_dupes.py)

- **1.3 Outlier Detection and Treatment**
- **1.4 Data Normalization and Standardization**

### 2. Feature Creation
- **2.1 Polynomial Features**
- **2.2 Interaction Terms**
- **2.3 Binning**
- **2.4 Domain-Specific Feature Engineering**

### 3. Feature Selection
- **3.1 Filter Methods**
- **3.2 Wrapper Methods**
- **3.3 Embedded Methods**
- **3.4 Dimensionality Reduction (e.g., PCA, LDA)**

### 4. Feature Transformation
- **4.1 Scaling and Normalization**
- **4.2 Logarithmic and Power Transformations**
- **4.3 Encoding Categorical Variables**
- **4.4 Handling Skewed Data**

### 5. Handling Imbalanced Data
- **5.1 Over-Sampling Techniques (e.g., SMOTE)**
- **5.2 Under-Sampling Techniques**
- **5.3 Synthetic Data Generation**
- **5.4 Cost-Sensitive Learning**

