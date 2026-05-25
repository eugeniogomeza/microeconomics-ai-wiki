---
title: Monte Carlo Simulation
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [statistics, simulation, r-programming, power-analysis, computational-methods]
status: active
---

# Monte Carlo Simulation

**AKA:** Simulation study, repeated sampling experiment, Monte Carlo method  
**Related:** [[very-normal-monte-carlo]], [[statistical-power]], [[effect-size]], [[r-project]]

## TL;DR

Monte Carlo simulation is the use of repeated random sampling to estimate the properties of statistical methods, models, or decisions. It is especially valuable when theoretical analysis is intractable — e.g., comparing hypothesis tests under non-normal distributions or evaluating complex decision rules.

## Explanation

### Core Idea

1. **Generate synthetic data** from known distributions with a known "truth" (e.g., a true effect size).
2. **Apply the method** you want to evaluate (e.g., a hypothesis test, a machine learning model).
3. **Repeat thousands of times** to estimate performance metrics (power, Type I error, bias, MSE).
4. **Analyze results** across different parameter combinations.

### Three Levels

**Level 1: Laptop-scale**
- Simple `for` loop
- Single parameter set
- Fast enough for 10k replications

**Level 2: Structured local**
- `expand.grid` + `pwalk` (tidyrverse)
- Parameter sweeps across tests, effect sizes, distributions
- Parallelization with `furrr`/`future`
- Auto-saving and checkpointing to resume crashed runs

**Level 3: HPC cluster**
- SLURM array jobs for massive parameter sweeps
- 100k+ replications
- File transfer via FileZilla, batch scripts via `vim`
- Mutual exclusion via `SLURM_ARRAY_TASK_ID`

### Key Considerations

- **Effect sizes** standardize comparisons across different scales (Cohen's d, median shift).
- **Distributional assumptions matter** — A method that works for normal data may fail catastrophically for Cauchy (heavy-tailed) data.
- **Reproducibility** — Always set seeds and save intermediate results.
- **Parallelization** — Replications are embarrassingly parallel; scale linearly with cores.

## Sources

- [[very-normal-monte-carlo]] — Practical crash course through all three levels.

## Connections

- [[economics-of-ai]] — Simulation is essential for evaluating AI-driven decisions and models.
- [[ai-agent-harness]] — Testing agent behavior across stochastic environments.
- [[statistical-power]] — The most common target metric in a simulation study.

## Open Questions

- When does simulation become more informative than theory, and vice versa?
- How should we report simulation uncertainty (Monte Carlo error) in published work?
- What are best practices for sharing simulation code and data to ensure reproducibility?
