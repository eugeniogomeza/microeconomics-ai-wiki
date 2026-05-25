---
title: Linear Regression
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [statistics, supervised-learning, regression, least-squares]
status: active
---

# Linear Regression

**AKA:** ordinary least squares (OLS), simple linear regression  
**Related:** [[logistic-regression]], [[multiple-regression]], [[least-squares]]

## TL;DR

The foundational supervised learning method. Linear regression models a continuous target variable as a weighted linear combination of input features. It finds the best-fitting straight line (or hyperplane) by minimizing the sum of squared prediction errors. Despite its simplicity, it remains a baseline and building block for more complex models.

## Explanation

For a single predictor: y = β₀ + β₁x + ε

The least-squares estimation finds β₀ and β₁ that minimize:
Σ(yᵢ − ŷᵢ)²

Key assumptions:
- Linearity: the true relationship is linear.
- Independence: residuals are independent.
- Homoscedasticity: constant variance of residuals.
- Normality: residuals are normally distributed (for valid inference).

## Sources

- [[statquest-linear-regression]] — Step-by-step derivation from a scatter plot of mice

## Connections

- [[logistic-regression]] — Generalizes linear regression to classification via a sigmoid link.
- [[multiple-regression]] — Extends to two or more predictors.
- [[neural-networks]] — A single-layer neural network with no hidden layers is equivalent to linear regression.

## Open Questions

- When is regularization (Ridge/Lasso) necessary vs. harmful?
- How should we handle multicollinearity in multiple predictors?
