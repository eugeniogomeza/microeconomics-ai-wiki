---
title: Logistic Regression
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [statistics, supervised-learning, classification, binary-classification]
status: active
---

# Logistic Regression

**AKA:** binary logistic regression, logit model  
**Related:** [[linear-regression]], [[sigmoid-function]], [[maximum-likelihood-estimation]], [[odds-ratio]]

## TL;DR

Despite its name, logistic regression is a classification algorithm, not a regression algorithm. It predicts the probability that a given input belongs to a particular class (usually binary: yes/no, True/False, 0/1). It does this by passing the linear prediction through a sigmoid function, squashing outputs to the range (0, 1), which is then thresholded to make a discrete decision.

## Explanation

The model predicts log-odds as a linear function of inputs:
ln(p/(1−p)) = β₀ + β₁x₁ + ... + βₙxₙ

Where p is the probability of the positive class. To get p, we apply the sigmoid:
p = 1 / (1 + e^-(β₀ + β₁x₁ + ...))

Parameters are estimated via **maximum likelihood estimation** (MLE), not least squares. Each coefficient βᵢ represents the change in log-odds for a one-unit increase in the corresponding predictor.

## Sources

- [[statquest-logistic-regression]] — Intuitive derivation using obesity classification example

## Connections

- [[linear-regression]] — Logistic regression borrows the linear predictor structure but uses it for classification probabilities.
- [[neural-networks]] — A single-layer neural network with sigmoid output is equivalent to logistic regression.
- [[sigmoid-function]] — The non-linear function that enables probability outputs.

## Open Questions

- How should we handle class imbalance in logistic regression?
- When does logistic regression outperform simple neural networks?
