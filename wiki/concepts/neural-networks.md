---
title: Principal Component Analysis
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [dimensionality-reduction, linear-algebra, statistics, machine-learning]
status: active
---

# Principal Component Analysis

**AKA:** PCA  
**Related:** [[dimensionality-reduction]], [[eigenvectors]], [[covariance-matrix]], [[linear-regression]]

## TL;DR

PCA is a dimensionality reduction technique that transforms data into a new coordinate system where the axes (principal components) are ordered by the amount of variance they capture. By selecting only the top components, we can reduce the feature space while retaining most of the signal — making visualization, storage, and modeling more tractable.

## Explanation

Given a dataset with many features, PCA:
1. Centers the data (subtracts the mean).
2. Computes the covariance matrix to see how features vary together.
3. Finds the eigenvectors and eigenvalues of the covariance matrix.
4. Sorts eigenvectors by eigenvalue (largest first) — these are the principal components.
5. Projects the original data onto the top k components to produce a lower-dimensional representation.

The first principal component is the direction in the data along which variance is maximized. The second is the direction of maximum variance orthogonal to the first, and so on.

## Sources

- [[statquest-pca]] — Step-by-step derivation with biological interpretation
- [[3blue1brown-channel]] — Geometric intuition (linear algebra series)

## Connections

- [[dimensionality-reduction]] — PCA is the most widely used linear dimensionality reduction method.
- [[neural-networks]] — Autoencoders can learn non-linear equivalents of PCA.
- [[linear-regression]] — Both use covariance structure, but PCA is unsupervised while regression is supervised.

## Open Questions

- When is PCA preferable to t-SNE or UMAP for visualization?
- How does whitening (scaling by eigenvalues) affect downstream models?
