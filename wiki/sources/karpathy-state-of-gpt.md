---
title: "Andrej Karpathy: The State of GPT"
url: "https://www.youtube.com/watch?v=bZQun8Y4L2A"
category: source
tags: [gpt, transformers, large-language-models, rlhf, training, tokenization, video, karpathy]
author: Andrej Karpathy
publisher: YouTube
speaker: Andrej Karpathy
created: 2026-05-25
updated: 2026-05-25
---

# The State of GPT

## Source Details

- **URL:** [https://www.youtube.com/watch?v=bZQun8Y4L2A](https://www.youtube.com/watch?v=bZQun8Y4L2A)
- **Channel:** [Andrej Karpathy](https://www.youtube.com/@karpathy)
- **Presenter:** [[andrej-karpathy]]
- **Published:** 2023
- **Duration:** ~1:15:00
- **Views:** 3M+
- **Status:** Widely cited explainer on how GPT works and how it's trained

## Summary

A comprehensive lecture breaking down the full GPT training and inference pipeline. Karpathy walks through the four stages of modern LLM creation: (1) pre-training on massive internet text, (2) supervised fine-tuning (SFT) on instruction-following data, (3) reward modeling where humans rank outputs, and (4) Reinforcement Learning from Human Feedback (RLHF) to align the model with human preferences. He also covers inference-time strategies like temperature sampling, top-k/top-p filtering, and system prompts.

## Key Claims

- **LLM training has four stages**:
  1. **Pre-training** — Train on massive corpus to learn language, reasoning, and world knowledge. This is where scale matters most.
  2. **Supervised Fine-Tuning (SFT)** — Fine-tune on high-quality instruction-answer pairs to teach the model to follow instructions.
  3. **Reward Modeling** — Train a separate model to score how "good" a response is, based on human preference rankings.
  4. **RLHF (PPO)** — Use the reward model to fine-tune the LLM via policy gradient methods, maximizing human preference scores.
- **GPT is a "stochastic parrot" AND a reasoning engine** — it statistically predicts next tokens, but emergent reasoning capabilities arise from the training objective and scale.
- **Context length is the new parameter count** — researchers are shifting focus from scaling model size to scaling context windows (e.g., 1M+ tokens).
- **System prompts are the new programming** — how you prompt a model changes its behavior more than any single weight.
- **LLM limitations are fundamental, not just engineering** — hallucinations, reasoning failures, and knowledge cutoff are intrinsic to the training paradigm.

## Entities Mentioned

- [[andrej-karpathy]] — Presenter
- OpenAI — GPT developer

## Concepts Discussed

- [[transformers]] — Architecture powering GPT
- [[language-models]] — Next-token prediction as a universal task
- [[rlhf]] — Reinforcement Learning from Human Feedback
- [[fine-tuning]] — Adapting a pre-trained model to a specific task
- [[tokenization]] — Text-to-integer mapping
- [[temperature-sampling]] — Controlling randomness in text generation
- [[hallucination]] — Generating plausible but false information

## Connections to Other Sources

- [[ibm-what-are-ai-agents]] — Agents use LLMs as reasoning engines; this video explains how those engines are built and aligned.
- [[chip-huyen-ai-engineering]] — Huyen discusses production LLM systems; Karpathy explains the training stack.

## Source References

- [The State of GPT video](https://www.youtube.com/watch?v=bZQun8Y4L2A) — Full lecture
- [Building LLMs from the Ground Up (MS Build 2024)](https://www.youtube.com/watch?v=7xTGNNLPyH8) — Karpathy's updated 2024 version
