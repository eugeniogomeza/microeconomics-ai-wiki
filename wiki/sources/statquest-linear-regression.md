---
title: "StatQuest: Linear Regression"
url: "https://www.youtube.com/watch?v=PaFPbb66DxQ"
category: source
tags: [linear-regression, statistics, least-squares, machine-learning, video, statquest]
author: Josh Starmer
publisher: YouTube
speaker: Josh Starmer
created: 2026-05-25
updated: 2026-05-25
---

# StatQuest: Linear Regression

## Source Details

- **URL:** [https://www.youtube.com/watch?v=PaFPbb66DxQ](https://www.youtube.com/watch?v=PaFPbb66DxQ)
- **Channel:** [StatQuest with Josh Starmer](https://www.youtube.com/@statquest)
- **Presenter:** [[josh-starmer]]
- **Published:** 2016
- **Duration:** ~9 minutes
- **Views:** 5M+
- **Status:** Foundational explainer for linear regression

## Summary

Starmer explains simple linear regression by starting with a scatter plot of mouse weights vs. sizes. He shows that a straight line can summarize the relationship, then poses the question: which line is best? The answer: the line that minimizes the sum of squared residuals (the least-squares criterion). He derives the formulas for the slope and intercept, explains R-squared as a measure of goodness of fit, and walks through how to interpret the coefficients.

## Key Claims

- **Linear regression finds the best-fitting straight line** — "best" is defined as the line that minimizes the sum of squared vertical distances to each data point.
- **Least squares is the standard approach** — squaring residuals penalizes large errors more than small ones and guarantees a unique solution.
- **Slope = covariance(X,Y) / variance(X)** — the formula emerges directly from minimizing squared error.
- **R-squared measures how much variance the model explains** — it is the proportion of total variance accounted for by the regression line.
- **Residuals should be normally distributed** — a key diagnostic assumption that allows inference (p-values, confidence intervals).

## Entities Mentioned

- [[josh-starmer]] — Creator and presenter of StatQuest

## Concepts Discussed

- [[linear-regression]] — Modeling a continuous response as a linear function of predictors
- [[least-squares]] — Optimization criterion minimizing squared prediction errors
- [[r-squared]] — Proportion of explained variance
- [[residuals]] — Differences between observed and predicted values
- [[covariance]] — Measure of how two variables vary together

## Source References

- [StatQuest: Linear Regression](https://www.youtube.com/watch?v=PaFPbb66DxQ) — Original video
- [StatQuest: Multiple Regression](https://www.youtube.com/watch?v=EkAQAi3zjU) — Extending to multiple predictors
