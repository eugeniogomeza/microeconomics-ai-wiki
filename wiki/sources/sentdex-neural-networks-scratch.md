---
title: "Sentdex: Neural Networks from Scratch"
url: "https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAiw2DyTQA-CCu8jkH"
category: source
tags: [neural-networks, backpropagation, numpy, python, deep-learning, video, sentdex]
author: Harrison Kinsley
publisher: YouTube
speaker: Harrison Kinsley
created: 2026-05-25
updated: 2026-05-25
---

# Sentdex: Neural Networks from Scratch

## Source Details

- **URL:** [https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAiw2DyTQA-CCu8jkH](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAiw2DyTQA-CCu8jkH)
- **Channel:** [Sentdex](https://www.youtube.com/@sentdex)
- **Presenter:** [[harrison-kinsley]]
- **Published:** ~2017–2018
- **Duration:** ~10–20 minutes per video, ~15 videos in series
- **Views:** 4M+ across series
- **Status:** Practical NumPy-only neural network implementation

## Summary

Harrison Kinsley builds a fully functional neural network using only NumPy — no TensorFlow, no PyTorch, no autograd. Starting from raw Python lists, he implements layers, activation functions (ReLU, sigmoid, softmax), loss functions (MSE, categorical cross-entropy), and full backpropagation with gradient descent. The series culminates in a network trained on MNIST that achieves respectable accuracy, all without touching a deep learning framework.

## Key Claims

- **You don't need a framework to understand neural networks** — NumPy arrays and matrix multiplication are sufficient.
- **Layers are just matrix operations** — weights × inputs + bias → activation. Repeat.
- **Backpropagation is manual chain rule application** — Kinsley computes gradients for each layer by hand and propagates backward through the network.
- **Numerical stability matters** — softmax with large exponentials overflows; subtracting the max before exponentiation fixes it.
- **Initialization matters** — random weights with proper scaling prevent vanishing/exploding signals.
- **MNIST is the canonical hello-world** — training a network on handwritten digits is the standard first validation of any neural net implementation.

## Concepts Discussed

- [[neural-networks]] — Feedforward computation graphs
- [[backpropagation]] — Computing gradients layer by layer
- [[activation-function]] — ReLU, sigmoid, softmax
- [[gradient-descent]] — Updating weights to minimize loss
- [[cross-entropy-loss]] — Standard classification loss function
- [[softmax]] — Normalizing logits to probability distributions

## Connections to Other Sources

- [[karpathy-neural-networks-zero-to-hero]] — Karpathy builds micrograd (autograd) and trains character-level models; Sentdex builds a feedforward classifier by hand.
- [[statquest-neural-networks]] — StatQuest does the arithmetic on a toy network; Sentdex scales it up to MNIST.
- [[tech-with-tim-learn-ml-ai-fast]] — Tim tells you what to learn; Sentdex shows you every line.

## Source References

- [Sentdex: Neural Networks from Scratch playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAiw2DyTQA-CCu8jkH)
- [Sentdex website](https://pythonprogramming.net/) — Accompanying written tutorials
