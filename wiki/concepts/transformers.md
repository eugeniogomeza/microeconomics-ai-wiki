---
title: Transformers
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [deep-learning, architecture, attention, language-models, sequence-modeling]
status: active
---

# Transformers

**AKA:** transformer architecture, self-attention network  
**Related:** [[self-attention]], [[language-models]], [[neural-networks]], [[gpt]], [[backpropagation]]

## TL;DR

The transformer is a deep learning architecture introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al. It replaced recurrent (RNN/LSTM) and convolutional approaches to sequence modeling by using **self-attention** mechanisms that can attend to any position in a sequence simultaneously. This parallelization made training dramatically faster and enabled the scaling that produced GPT, BERT, and virtually all modern large language models.

## Explanation

A transformer block consists of:

1. **Multi-Head Self-Attention** — Each token queries all other tokens to produce a context-aware representation. Multiple "heads" learn different types of relationships.
2. **Feedforward Network** — A position-wise fully connected layer (usually two linear transformations with a non-linearity in between).
3. **Residual Connections + Layer Normalization** — Skip connections around both attention and feedforward, with layer norm applied before each sub-block (pre-norm) or after (post-norm).

The original "encoder-decoder" architecture (for translation) has two streams:
- **Encoder** — processes the input sequence bidirectionally.
- **Decoder** — generates outputs autoregressively (one token at a time).

GPT uses only the decoder stack. BERT uses only the encoder stack.

Why transformers won:
- **Parallelism** — unlike RNNs, all tokens are processed simultaneously.
- **Long-range dependencies** — attention can directly connect any two positions regardless of distance.
- **Scalability** — training time grows linearly with sequence length, and the architecture scales cleanly with more compute and data.

## Sources

- [[karpathy-build-gpt]] — Full transformer implemented from scratch in ~300 lines of PyTorch
- [[karpathy-neural-networks-zero-to-hero]] — Self-attention built step by step in the makemore series
- [[3blue1brown-channel]] — Visual intuition for how attention works

## Connections

- [[neural-networks]] — Transformers are a type of neural network; the key difference is the attention mechanism replacing recurrence.
- [[language-models]] — Transformers are the dominant architecture for modern LLMs.
- [[backpropagation]] — Transformers are trained end-to-end with backpropagation and gradient descent, just like all other neural networks.

## Open Questions

- Are transformers the final architecture for sequence modeling, or will something more efficient emerge?
- How do we reduce the O(n²) attention complexity for very long sequences?
