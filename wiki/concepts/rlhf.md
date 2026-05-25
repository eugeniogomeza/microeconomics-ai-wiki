---
title: Reinforcement Learning from Human Feedback
alias: rlhf
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [alignment, fine-tuning, reinforcement-learning, llm, human-feedback]
status: active
---

# Reinforcement Learning from Human Feedback

**AKA:** RLHF, human preference learning, alignment training  
**Related:** [[language-models]], [[transformers]], [[ai-agent-harness]]

## TL;DR

RLHF is the technique used to align large language models with human preferences. After pre-training and supervised fine-tuning, a language model often produces outputs that are fluent but unhelpful, biased, or harmful. RLHF addresses this by training a reward model on human rankings of responses, then using reinforcement learning (typically PPO) to fine-tune the LLM to maximize that reward. It was a key innovation behind ChatGPT's usability and is now standard in production LLM development.

## Explanation

RLHF has three stages:

1. **Train a reward model** — Humans compare pairs of model outputs and label which is better. A separate "reward model" is trained to predict these human preference scores.

2. **Fine-tune the policy (LLM) with PPO** — Use the reward model as a reward signal. The LLM generates text; the reward model scores it; reinforcement learning updates the LLM's weights to produce higher-scoring outputs.

3. **KL regularization** — Constrain the RL-tuned model from drifting too far from the supervised fine-tuned version, preserving language quality.

### Alternatives to RLHF

- **DPO (Direct Preference Optimization)** — A simpler method that directly optimizes from preference pairs without a separate reward model. Gaining popularity for being more stable.
- **Constitutional AI** — Anthropic's method where the model critiques and revises its own outputs against a set of principles.

### Limitations

- **Reward hacking** — The model finds shortcuts to maximize the reward score without actually improving quality.
- **Preference bias** — Human annotators may have systematic biases that get baked into the model.
- **Scalability** — Manual human labeling is expensive; synthetic feedback (e.g., from larger models) is an active research direction.

## Sources

- [[karpathy-state-of-gpt]] — Step-by-step breakdown of reward modeling and PPO fine-tuning
- [[ibm-what-are-ai-agents]] — Agents depend on aligned LLMs; RLHF is how they get aligned

## Connections

- [[language-models]] — RLHF is applied after pre-training and SFT to align LLM behavior with human values.
- [[ai-agent-harness]] — An agent's reliability depends heavily on the alignment of its underlying LLM.

## Open Questions

- Can we fully automate alignment without human labeling?
- How do we align models on values that humans themselves disagree about?
