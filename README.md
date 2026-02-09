# Physics-Driven Machine Learning for Event Classification

This repository presents a physics-motivated machine learning study for event classification, focusing on the relationship between variance structure, linear separability, and nonlinear decision boundaries.  
The analysis emphasizes interpretability, robustness, and physics-aware evaluation rather than black-box optimization.

---

## Project Motivation

In high-energy physics analyses, classification performance is often constrained by the structure of the available observables rather than by model complexity.  
This project investigates whether dominant variance directions correspond to discriminative power, and whether nonlinear models provide meaningful improvements over linear baselines.

---

## Analysis Overview

The workflow follows a structured, research-oriented pipeline:

1. Data cleaning and preprocessing using reusable utility functions
2. Exploratory data analysis
3. Dimensionality reduction via Principal Component Analysis (PCA)
4. Linear classification as an interpretable baseline
5. Nonlinear classification to probe weak nonlinear structure
6. Physics-motivated evaluation using weighted metrics and signal significance

---

## Repository Structure and File Description

### Notebooks/

#### **1_Exploration.ipynb**
- Initial data inspection and exploratory analysis
- Feature distributions and class imbalance
- Validation of event weights and basic statistics

#### **2_LogisticRegression.ipynb**
- Logistic Regression as a linear baseline
- Weighted ROC and Precision–Recall evaluation
- Threshold scans and physics-motivated signal significance
- Serves as an interpretable reference model

#### **3_PCA.ipynb**
- Principal Component Analysis of the feature space
- Variance explained by leading components
- 2D and 3D PCA visualizations
- Demonstrates misalignment between variance-dominant directions and class separation

#### **4_SVM.ipynb**
- Linear SVM as a robust baseline
- RBF kernel SVM to probe nonlinear discriminative structure
- Validation-based hyperparameter selection
- ROC, Precision–Recall, and physics-motivated threshold optimization
- Explicit discussion of computational cost and overfitting considerations

---

### Preprocessing/

#### **data_preprocessing.py**
- Centralized data cleaning and preprocessing utilities
- Feature selection, scaling, and weight handling
- Ensures consistency across all notebooks
- Designed for reuse and modularity

---

## Key Findings

- The leading PCA components capture a large fraction of the total variance but do not provide strong class separation.
- Linear models already capture most of the discriminative power in the data.
- Nonlinear kernels introduce only modest performance improvements, indicating weak nonlinear structure.
- Optimal physics performance is achieved through decision threshold optimization rather than reliance on global metrics alone.

---

## Methodological Notes

- All models are evaluated using weighted metrics to account for physical cross sections.
- Model selection is performed exclusively on validation data.
- Final performance is reported on an independent test set.
- Emphasis is placed on robustness and interpretability rather than aggressive hyperparameter tuning.

---

## Scope

This project is intended as a research-oriented study suitable for graduate-level applications in particle physics and machine learning.  
It prioritizes physical insight and methodological clarity over benchmark-driven performance.

