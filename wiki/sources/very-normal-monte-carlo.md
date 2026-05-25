---
title: Very Normal — Monte Carlo Simulation Crash Course
created: 2026-05-25
updated: 2026-05-25
category: source
tags: [video, youtube, statistics, monte-carlo, simulation, r-programming, hypothesis-testing]
author: Christian (Very Normal)
publisher: YouTube
url: https://www.youtube.com/watch?v=OdWLP8umw3A
status: active
---

# Very Normal — Monte Carlo Simulation Crash Course

**Author:** [[christian-very-normal]]  
**Channel:** Very Normal ([@very-normal](https://www.youtube.com/@very-normal))  
**Published:** 2025-01-31  
**URL:** [youtu.be/OdWLP8umw3A](https://www.youtube.com/watch?v=OdWLP8umw3A)  
**Length:** 28:30  
**Original file:** (none — fetched directly)

## TL;DR

A comprehensive crash course on Monte Carlo simulation studies for statistics and machine learning. Christian walks through three levels of complexity — from a simple laptop-sized loop comparing hypothesis tests, to a tidyverse structured approach with saving/parallelization, to running 180,000 replications on an HPC cluster with SLURM job scheduling.

## Key Claims

1. **Monte Carlo is the most important skill in statistics** — When you need to choose among methods before seeing real data, simulation is the only way to estimate power and robustness realistically.
2. **Three levels of simulation** — Level 1: simple for-loop on a laptop. Level 2: structured tibble design with `expand.grid`, `pwalk`, automated saving, checkpointing, and parallel computing with `furrr`. Level 3: HPC cluster with SLURM array jobs and script-based submission.
3. **Effect sizes standardize comparison** — Cohen's d and median shifts let you compare methods across different distributions (normal vs. Cauchy) without getting confused by scale.
4. **Parametric vs. non-parametric matters** — When data has outliers (Cauchy), non-parametric tests outperform t-tests dramatically. Simulations reveal this empirically.
5. **HPC practical knowledge** — FileZilla for file transfer, `vim` for batch script editing, `sbatch` for job submission, `sq` for monitoring, and the critical mental model of distributing mutually exclusive replications across cluster nodes using `SLURM_ARRAY_TASK_ID`.

## Entities Mentioned

- [[r-project]] — Programming language and environment used throughout.
- [[tidyverse]] — Collection of R packages (`tidyr`, `dplyr`, `furrr`, `future`) for data manipulation and parallel iteration.
- [[slurm]] — Workload manager / job scheduler for HPC clusters.
- [[mit-press]] — Publisher of related academic works (indirect connection).

## Concepts Discussed

- [[monte-carlo-simulation]] — Generating synthetic data and running repeated experiments to estimate power, bias, or method performance.
- [[statistical-power]] — The probability of correctly rejecting a false null hypothesis.
- [[effect-size]] — Standardized measure of difference magnitude, typically Cohen's d for continuous data.
- [[parallel-computing]] — Using multiple CPU cores or cluster nodes to run independent replications simultaneously.
- [[high-performance-computing]] — Cluster computing for large-scale simulations.
- [[hypothesis-testing]] — t-test, Welch's t-test, Mann-Whitney U / Wilcoxon test.
- [[parametric-vs-non-parametric]] — Normal distribution assumptions versus robust methods for outlier-prone data (Cauchy).

## Notable Quotes

> "What is the best way to analyze a given data set? By choosing a method that closely models the processes that create the data."

> "The answer is Monte Carlo simulations, which I've previously called the most important skill in statistics."

> "If you've only run code on your own computer then you're probably used to working with just a graphical interface... when you're working with an HPC you're most likely going to have to interact with it through a command line."

## Connections to Other Sources

- (none yet)

## Agent Notes

- Extremely practical for anyone doing quantitative research or A/B testing.
- Level 2 (structured tibble + parallel) is likely sufficient for most users before jumping to HPC.
- The HPC walkthrough is rare in YouTube tutorials — very valuable for grad students.
- Complements economic/AI research methods where simulations are used to evaluate models.
