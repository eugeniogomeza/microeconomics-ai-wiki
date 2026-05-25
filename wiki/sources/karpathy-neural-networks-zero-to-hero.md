---
title: "Andrej Karpathy: Neural Networks: Zero to Hero"
url: "https://www.youtube.com/playlist?list=PLAqhIrjkxAIn_2UMj8s9K2k22VdjCi3"
category: source
tags: [neural-networks, deep-learning, backpropagation, autograd, language-models, transformers, video, karpathy]
author: Andrej Karpathy
publisher: YouTube
speaker: Andrej Karpathy
created: 2026-05-25
updated: 2026-05-25
---

# Neural Networks: Zero to Hero

## Source Details

- **URL:** [https://www.youtube.com/playlist?list=PLAqhIrjkxAIn_2UMj8s9K2k22VdjCi3](https://www.youtube.com/playlist?list=PLAqhIrjkxAIn_2UMj8s9K2k22VdjCi3)
- **Channel:** [Andrej Karpathy](https://www.youtube.com/@karpathy)
- **Presenter:** [[andrej-karpathy]]
- **Published:** 2022–2023
- **Videos:** 7 core videos (~4–5 hours total)
- **Status:** Canonical from-scratch deep learning curriculum

## Summary

A complete bottom-up deep learning course implemented from scratch in Python/NumPy/PyTorch. Andrej Karpathy builds every component by hand: starting with backpropagation and autograd (micrograd), progressing through character-level language models (makemore: bigram, MLP, convolutional, transformer), and culminating in a full GPT implementation (nanoGPT). There are no imported black boxes — every weight initialization, every forward pass, every gradient is written and explained live.

## Key Claims

- **Backpropagation is just the chain rule applied recursively** — micrograd proves this by implementing a complete autograd engine in ~100 lines.
- **Language models are next-token predictors** — every architecture (bigram, MLP, WaveNet, transformer) is just a progressively better way to predict the next character given context.
- **The transformer is the simplest architecture that actually works** — attention replaces recurrence and convolution; the rest is feedforward layers and residual connections.
- **Training is optimization over a loss landscape** — every model is trained by computing a loss, backpropagating gradients, and updating weights via gradient descent.
- **Scaling beats architecture** — once you have a working architecture, the game becomes data, compute, and hyperparameter tuning.

## The makemore Series Breakdown

### 1. Bigram (Counts + Probability)
- The simplest model: count character pairs, normalize to probabilities, sample.
- Loss: negative log-likelihood. No neural network at all.

### 2. MLP (Multi-Layer Perceptron)
- Embeds characters into a continuous space, feeds through hidden layers.
- Introduces gradients, weight updates, and the tensor API.

### 3. ConvNet / WaveNet-style
- Uses dilated convolutions to capture longer contexts.
- Demonstrates that architecture matters before transformers.

### 4. Transformer
- Implements self-attention from scratch: query/key/value matrices, softmax, multi-head attention.
- This is the architecture that powers GPT.

### 5. GPT (nanoGPT)
- Scales the transformer to GPT-2 size (124M parameters).
- Trains on Tiny Shakespeare and OpenWebText.

## Entities Mentioned

- [[andrej-karpathy]] — Creator and presenter

## Concepts Discussed

- [[backpropagation]] — Gradient computation via reverse-mode automatic differentiation
- [[neural-networks]] — Multi-layer computation graphs
- [[transformers]] — Attention-based architecture for sequences
- [[language-models]] — Probabilistic models of text
- [[autoregressive-models]] — Models that predict the next token conditioned on past tokens
- [[tokenization]] — Converting text to integers for model input

## Connections to Other Sources

- [[statquest-neural-networks]] — StatQuest does the arithmetic on a toy example; Karpathy implements it in Python.
- [[3blue1brown-channel]] — 3Blue1Brown visualizes attention; Karpathy codes it.
- [[jeremy-howard-practical-deep-learning]] — fast.ai teaches top-down transfer learning; Zero to Hero is bottom-up from scratch.

## Source References

- [Neural Networks: Zero to Hero playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxAIn_2UMj8s9K2k22VdjCi3)
- [micrograd GitHub](https://github.com/karpathy/micrograd) — Tiny autograd engine
- [nanoGPT GitHub](https://github.com/karpathy/nanoGPT) — Clean GPT implementation
