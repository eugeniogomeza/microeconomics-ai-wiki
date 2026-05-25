---
title: "StatQuest: Principal Component Analysis (PCA)"
url: "https://www.youtube.com/watch?v=FgakZw6K1QQ"
category: source
tags: [pca, dimensionality-reduction, statistics, machine-learning, eigenvectors, eigenvalues, video, statquest]
author: Josh Starmer
publisher: YouTube
speaker: Josh Starmer
created: 2026-05-25
updated: 2026-05-25
---

# StatQuest: Principal Component Analysis (PCA)

## Source Details

- **URL:** [https://www.youtube.com/watch?v=FgakZw6K1QQ](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- **Channel:** [StatQuest with Josh Starmer](https://www.youtube.com/@statquest)
- **Presenter:** [[josh-starmer]]
- **Published:** 2017
- **Duration:** ~22 minutes
- **Views:** 10M+
- **Status:** Canonical explainer for PCA

## Summary

Josh Starmer's most-viewed video. He explains Principal Component Analysis using a simple 2D dataset of mice weights and gene activity levels. The core insight: PCA finds new axes (principal components) that capture the maximum variance in the data, allowing us to reduce dimensions while preserving the signal. Starmer walks through every step: centering the data, finding the direction of greatest variance (PC1), projecting points onto it, and interpreting what the new components actually mean biologically.

## Key Claims

- **PCA is a dimensionality reduction technique** — it transforms data into a new coordinate system where the axes are ordered by variance captured.
- **Principal components are linear combinations of original features** — PC1 is the direction in the data along which variance is maximized.
- **Centering is essential** — PCA requires mean-centered data or the first component will just point toward the mean.
- **Eigenvectors and eigenvalues come from the covariance matrix** — eigenvectors are the principal component directions; eigenvalues are the amount of variance each component captures.
- **Interpretation matters** — Starmer emphasizes that PC1 might represent a biological trait (e.g., "size") that is a combination of multiple measured variables.

## Entities Mentioned

- [[josh-starmer]] — Creator and presenter of StatQuest

## Concepts Discussed

- [[principal-component-analysis]] — Dimensionality reduction via eigendecomposition of the covariance matrix
- [[eigenvectors]] — Directions of maximum variance in the data
- [[covariance-matrix]] — Captures how features vary together
- [[dimensionality-reduction]] — Reducing feature count while preserving signal

## Source References

- [StatQuest: PCA Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) — Original video
- [StatQuest: PCA in Python](https://www.youtube.com/watch?v=Lsue2gWM9y0) — Code walkthrough
- [StatQuest: PCA in R](https://www.youtube.com/watch?v=0Jp4gsfOLMs) — Code walkthrough
