---
title: "StatQuest: Neural Networks"
url: "https://www.youtube.com/watch?v=Czx4u3TeJGY"
category: source
tags: [neural-networks, backpropagation, gradient-descent, deep-learning, video, statquest]
author: Josh Starmer
publisher: YouTube
speaker: Josh Starmer
created: 2026-05-25
updated: 2026-05-25
---

# StatQuest: Neural Networks

## Source Details

- **URL:** [https://www.youtube.com/watch?v=Czx4u3TeJGY](https://www.youtube.com/watch?v=Czx4u3TeJGY)
- **Channel:** [StatQuest with Josh Starmer](https://www.youtube.com/@statquest)
- **Presenter:** [[josh-starmer]]
- **Published:** 2017
- **Duration:** ~26 minutes
- **Views:** 1.5M+
- **Status:** Canonical step-by-step neural network explainer

## Summary

A three-part StatQuest series covering neural networks from absolute first principles. Starmer builds a tiny network by hand using a toy example (predicting movie enjoyment based on popcorn and soda consumption). He shows forward propagation — computing the output by passing inputs through weighted connections and an activation function — then walks through backpropagation: how the error flows backward, how each weight's contribution to the error is calculated via the chain rule, and how gradient descent updates the weights.

## Key Claims

- **Neural networks are just stacks of weighted sums with activation functions** — the "magic" is in the learning, not the architecture.
- **Forward propagation** — multiply inputs by weights, sum, apply activation function, repeat for each layer.
- **Activation functions introduce non-linearity** — without them, a deep network collapses to a single linear transformation.
- **Backpropagation uses the chain rule** — the derivative of the loss with respect to each weight is computed by multiplying partial derivatives along the path from output back to that weight.
- **Gradient descent updates weights proportionally to their error contribution** — large errors get larger updates; the learning rate controls step size.
- **Vanishing gradients are a real problem** — in deep networks with sigmoid activations, gradients can shrink to near-zero, preventing lower layers from learning.

## Entities Mentioned

- [[josh-starmer]] — Creator and presenter of StatQuest

## Concepts Discussed

- [[neural-networks]] — Biologically inspired computational models
- [[backpropagation]] — Algorithm for computing gradients in neural networks
- [[gradient-descent]] — Optimization algorithm that minimizes loss by following gradients
- [[activation-function]] — Non-linear function applied to neuron outputs (sigmoid, ReLU, etc.)
- [[chain-rule]] — Fundamental calculus rule enabling backpropagation
- [[vanishing-gradient]] — Problem where gradients become too small to update weights effectively

## Connections to Other Sources

- [[3blue1brown-channel]] — 3Blue1Brown gives the geometric intuition; StatQuest does the arithmetic.
- [[jeremy-howard-practical-deep-learning]] — fast.ai shows how to train real models with modern libraries; StatQuest explains what the library is doing under the hood.

## Source References

- [StatQuest: Neural Networks Part 1](https://www.youtube.com/watch?v=Czx4u3TeJGY) — Introduction and forward propagation
- [StatQuest: Neural Networks Part 2](https://www.youtube.com/watch?v=SpMK1V9XFsM) — Backpropagation step-by-step
- [StatQuest: Neural Networks Part 3](https://www.youtube.com/watch?v=ILsA4HwGVAo) — Implementing a neural network in R
