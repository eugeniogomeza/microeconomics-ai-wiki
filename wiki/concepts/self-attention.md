---
title: Self-Attention
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [transformers, attention, deep-learning, sequence-modeling]
status: active
---

# Self-Attention

**AKA:** scaled dot-product attention, intra-attention  
**Related:** [[transformers]], [[language-models]], [[neural-networks]]

## TL;DR

Self-attention is the core mechanism inside transformers. It allows each token in a sequence to "attend to" (compute relevance with) all other tokens simultaneously, producing a context-aware representation for every position. Unlike RNNs, which process sequences sequentially, self-attention captures long-range dependencies directly and in parallel — making it the engine that powers modern language models.

## Explanation

For each token, self-attention computes three vectors:
- **Query (Q)** — "What am I looking for?"
- **Key (K)** — "What do I contain?"
- **Value (V)** — "What information do I have?"

The attention score between two tokens is computed as: Attention(Q, K, V) = softmax(QK^T / √d_k) × V

Where:
- QK^T computes how relevant each token is to every other token.
- √d_k scales the scores to prevent softmax from saturating.
- softmax normalizes scores to sum to 1 (attention weights).
- The weighted sum of Value vectors produces the output for each token.

**Causal (masked) self-attention** — used in GPT. The model can only attend to previous tokens, enforced by masking future positions with −∞ before softmax.

**Multi-head attention** — runs multiple attention operations in parallel with different learned projections, enabling the model to attend to different aspects of the sequence simultaneously.

## Sources

- [[karpathy-build-gpt]] — Self-attention implemented from scratch in nanoGPT (~50 lines)
- [[3blue1brown-channel]] — Visual intuition for how attention "looks" across a sequence

## Connections

- [[transformers]] — Self-attention is the defining operation of the transformer architecture.
- [[language-models]] — GPT's ability to model long-range dependencies comes entirely from self-attention.

## Open Questions

- Can we replace self-attention with more efficient mechanisms (e.g., linear attention, state space models) without losing quality?
- Why do multi-head attention heads specialize into interpretable roles (e.g., positional, syntactic, semantic)?
