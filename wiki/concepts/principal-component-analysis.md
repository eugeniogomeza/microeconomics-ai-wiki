---
title: Neural Networks
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [deep-learning, ai, machine-learning, architecture]
status: active
---

# Neural Networks

**AKA:** artificial neural networks (ANN), deep neural networks (DNN)  
**Related:** [[backpropagation]], [[gradient-descent]], [[transfer-learning]], [[transformers]]

## TL;DR

Neural networks are computational models loosely inspired by biological neurons. They consist of layers of interconnected nodes ("neurons") where each connection has a learnable weight. By composing weighted sums with non-linear activation functions, neural networks can approximate any continuous function and have become the dominant architecture in modern AI — from image recognition to language models.

## Explanation

A basic feedforward neural network processes data as follows:
1. **Input layer** — receives raw features.
2. **Hidden layers** — each neuron computes a weighted sum of its inputs, adds a bias, and applies an activation function.
3. **Output layer** — produces predictions (e.g., class probabilities, continuous values).

Training uses **backpropagation** and **gradient descent** to adjust weights so the network's predictions minimize a loss function.

Modern architectures include:
- **CNNs** — for images and spatial data.
- **RNNs/LSTMs** — for sequences (now largely superseded by transformers).
- **Transformers** — attention-based architecture powering GPT, LLaMA, and virtually all modern language models.

## Sources

- [[statquest-channel]] — Step-by-step derivations of forward propagation and backpropagation
- [[3blue1brown-channel]] — Geometric intuition for how neural networks "learn"
- [[jeremy-howard-practical-deep-learning]] — Practical deep learning from first principles (fast.ai)
- [[tech-with-tim-learn-ml-ai-fast]] — Beginner-friendly ML and neural network roadmap

## Connections

- [[backpropagation]] — The algorithm that makes training deep networks possible.
- [[gradient-descent]] — The optimization routine that backpropagation feeds into.
- [[ai-agent-harness]] — Neural networks are the "brain" inside many agent systems.

## Open Questions

- Why do overparameterized networks generalize well despite fitting random labels?
- What is the best way to interpret what individual neurons or layers represent?
