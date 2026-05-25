---
title: Autoregressive Models
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [generative-models, sequence-modeling, next-token-prediction, language-models, gpt]
status: active
---

# Autoregressive Models

**AKA:** autoregressive generation, left-to-right models  
**Related:** [[language-models]], [[transformers]], [[gpt]]

## TL;DR

Autoregressive models generate sequences one element at a time, where each new element is predicted conditioned on all previously generated elements. GPT is the canonical example: it predicts the next token given all previous tokens, then appends that token to the context and repeats. This simple mechanism underlies virtually all modern text generation, from chatbots to code completion.

## Explanation

The autoregressive objective is deceptively simple:

P(x₁, x₂, ..., xₙ) = P(x₁) × P(x₂|x₁) × P(x₃|x₁,x₂) × ... × P(xₙ|x₁,...,xₙ₋₁)

During training, the model sees the full sequence and learns to maximize the probability of each token given its predecessors. During generation (inference), the model predicts one token, feeds it back into its own context, and repeats.

### Training vs. Inference

- **Training** — Parallel: compute next-token probabilities for all positions at once using a causal mask.
- **Inference** — Sequential: predict one token, append, predict next. Uses KV caching to avoid recomputing past attention.

### Strengths

- **Simple training objective** — just next-token prediction; no need for paired data or labels.
- **Scales well** — larger models + more data = better predictions.
- **Flexible output** — same model can generate text, code, or structured data depending on prompt.

### Limitations

- **Sequential generation** — cannot be parallelized at inference time (one token at a time).
- **Exposure bias** — trained on ground-truth prefixes but generates from its own (sometimes wrong) outputs.
- **Fixed left-to-right order** — cannot revise earlier tokens after generating later ones.

## Sources

- [[karpathy-build-gpt]] — nanoGPT autoregressive generation on Tiny Shakespeare
- [[karpathy-neural-networks-zero-to-hero]] — makemore series: bigram → MLP → transformer, all autoregressive

## Connections

- [[language-models]] — GPT-style language models are autoregressive by design.
- [[transformers]] — Decoder-only transformers implement autoregressive text generation with causal self-attention masking.

## Open Questions

- Can non-autoregressive generation (e.g., parallel decoding, diffusion for text) match or exceed autoregressive quality?
- How should we handle the fact that autoregressive models can only attend to the past during generation?
