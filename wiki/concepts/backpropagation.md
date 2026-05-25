---
title: Backpropagation
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [neural-networks, deep-learning, calculus, optimization, chain-rule]
status: active
---

# Backpropagation

**AKA:** backward propagation of errors  
**Related:** [[gradient-descent]], [[chain-rule]], [[neural-networks]]

## TL;DR

Backpropagation is the algorithm that makes training deep neural networks computationally feasible. It calculates the gradient of the loss function with respect to every weight in the network by working backward from the output layer, applying the chain rule from calculus at each step. This enables efficient gradient descent updates across millions of parameters.

## Explanation

The core idea:
1. **Forward pass** — compute the network's output and the loss.
2. **Backward pass** — compute how much each weight contributed to the loss by applying the chain rule recursively from output to input.
3. **Weight update** — adjust each weight in the direction that reduces loss, scaled by the learning rate.

Without backpropagation, computing gradients for a network with millions of parameters would be computationally intractable. With backpropagation, it scales linearly with the number of layers.

Key issues:
- **Vanishing gradients** — in deep networks with sigmoid activations, gradients can shrink exponentially, preventing lower layers from learning.
- **Exploding gradients** — gradients can grow exponentially in recurrent networks, causing unstable training.

Modern mitigations include ReLU activations, batch normalization, residual connections, and skip connections.

## Sources

- [[statquest-neural-networks]] — Hand-calculated step-by-step backpropagation on a toy network
- [[3blue1brown-channel]] — Visual intuition for how gradients flow backward
- [[jeremy-howard-practical-deep-learning]] — Practical backpropagation in modern frameworks

## Connections

- [[gradient-descent]] — Backpropagation provides the gradients; gradient descent uses them.
- [[chain-rule]] — The calculus operation that makes backpropagation possible.
- [[neural-networks]] — Backpropagation is the universal training method for feedforward networks.

## Open Questions

- Why does stochastic gradient descent with backprop generalize so well?
- Can we train deep networks without backpropagation (e.g., with local learning rules or Hebbian learning)?
