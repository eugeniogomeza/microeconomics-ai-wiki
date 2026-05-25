---
title: "Andrej Karpathy: Let's Build GPT: From Scratch, in Code, Spelled Out"
url: "https://www.youtube.com/watch?v=kCc8FmEb1nY"
category: source
tags: [transformers, gpt, language-models, attention, self-attention, pytorch, video, karpathy]
author: Andrej Karpathy
publisher: YouTube
speaker: Andrej Karpathy
created: 2026-05-25
updated: 2026-05-25
---

# Let's Build GPT: From Scratch, in Code, Spelled Out

## Source Details

- **URL:** [https://www.youtube.com/watch?v=kCc8FmEb1nY](https://www.youtube.com/watch?v=kCc8FmEb1nY)
- **Channel:** [Andrej Karpathy](https://www.youtube.com/@karpathy)
- **Presenter:** [[andrej-karpathy]]
- **Published:** 2023
- **Duration:** 2:13:00
- **Views:** 5M+
- **Status:** Best single-resource implementation of a transformer from scratch

## Summary

In a single two-hour session, Andrej Karpathy implements a GPT-like transformer from absolute scratch in PyTorch and trains it on the Tiny Shakespeare dataset. Starting with tokenization, he builds every transformer component by hand: token and positional embeddings, causal self-attention with masked softmax, multi-head attention, feedforward layers, layer normalization, residual connections, dropout, and the full training loop. The final model generates plausible Shakespearean prose.

## Key Claims

- **A transformer is surprisingly simple to implement** — the core architecture fits in roughly 300 lines of PyTorch.
- **Attention is all you need — literally** — the entire model is stacks of attention + feedforward with residual connections and layer norm.
- **Causal (autoregressive) self-attention** — the model only attends to previous tokens, enforced by a triangular mask on the attention scores.
- **Token + positional embeddings** — tokens are embedded into vectors; positional encodings tell the model "where" each token is in the sequence.
- **Layer normalization stabilizes training** — normalizes activations across the feature dimension, enabling deeper networks.
- **Dropout prevents overfitting** — randomly zeroes activations during training; applied after attention and during residual connections.
- **The training loop is identical across architectures** — forward, loss, backward, step; what changes is the model definition.

## Architecture Built

1. **Token embedding** — maps vocabulary indices to dense vectors.
2. **Positional encoding** — adds position information (learned in this implementation).
3. **Transformer block** (repeated N times):
   - Layer Norm → Multi-Head Self-Attention → Residual
   - Layer Norm → Feedforward (up-project → ReLU → down-project) → Residual
4. **Final Layer Norm → Linear → Softmax** — outputs next-token probabilities.

## Entities Mentioned

- [[andrej-karpathy]] — Creator and presenter

## Concepts Discussed

- [[transformers]] — Attention-based sequence-to-sequence architecture
- [[self-attention]] — Each token attends to all previous tokens to compute contextual representations
- [[tokenization]] — Mapping raw text to integer token IDs
- [[language-models]] — Probabilistic models that predict the next token
- [[autoregressive-models]] — Generate text one token at a time, conditioning on all previous tokens
- [[layer-normalization]] — Normalizing across features for training stability

## Connections to Other Sources

- [[3blue1brown-channel]] — 3Blue1Brown's transformers series visualizes attention; this video implements it.
- [[jeremy-howard-practical-deep-learning]] — Fast.ai shows how to *use* transformers; Karpathy shows how to *build* them.

## Source References

- [Let's Build GPT video](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Full implementation walkthrough
- [nanoGPT GitHub](https://github.com/karpathy/nanoGPT) — The code written in the video
