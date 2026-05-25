---
title: "StatQuest: Logistic Regression"
url: "https://www.youtube.com/watch?v=yIYKR4sgzI8"
category: source
tags: [logistic-regression, classification, statistics, machine-learning, sigmoid, video, statquest]
author: Josh Starmer
publisher: YouTube
speaker: Josh Starmer
created: 2026-05-25
updated: 2026-05-25
---

# StatQuest: Logistic Regression

## Source Details

- **URL:** [https://www.youtube.com/watch?v=yIYKR4sgzI8](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- **Channel:** [StatQuest with Josh Starmer](https://www.youtube.com/@statquest)
- **Presenter:** [[josh-starmer]]
- **Published:** 2018
- **Duration:** ~11 minutes
- **Views:** 3M+
- **Status:** Foundational explainer for logistic regression

## Summary

Starmer explains logistic regression by contrasting it with linear regression. Linear regression predicts continuous values, but what if the outcome is binary (e.g., obese vs. not obese)? A straight line predicts values outside [0, 1], which makes no sense for probabilities. The solution: wrap the linear predictor in the sigmoid (logistic) function, which squashes outputs to probabilities between 0 and 1. Starmer then explains log-odds, maximum likelihood estimation (MLE), and how to interpret logistic regression coefficients.

## Key Claims

- **Logistic regression is classification, not regression** — despite the name, it predicts probabilities of class membership, not continuous values.
- **The sigmoid function maps any real number to (0, 1)** — enabling probability outputs.
- **Log-odds (logit) is the linear part** — the model is linear in log-odds space, non-linear in probability space.
- **Maximum Likelihood Estimation (MLE) finds the best parameters** — unlike least squares, MLE finds the parameters that maximize the probability of observing the actual data.
- **Odds ratios interpret coefficients multiplicatively** — a coefficient of 0.5 means the odds of the outcome increase by a factor of e^0.5 when the predictor increases by 1 unit.

## Entities Mentioned

- [[josh-starmer]] — Creator and presenter of StatQuest

## Concepts Discussed

- [[logistic-regression]] — Binary classification using a sigmoid link function
- [[sigmoid-function]] — S-shaped function mapping real numbers to (0, 1)
- [[log-odds]] — Logarithm of the odds ratio; the linear predictor in logistic regression
- [[maximum-likelihood-estimation]] — Parameter estimation by maximizing the likelihood of observed data
- [[odds-ratio]] — Multiplicative factor by which odds change with a unit increase in predictor

## Source References

- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8) — Original video
