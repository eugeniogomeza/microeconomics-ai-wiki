---
title: Reinforcement Learning
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [machine-learning, ai, agent, q-learning, deep-q-networks, policy-gradients]
status: active
---

# Reinforcement Learning

**AKA:** RL, trial-and-error learning  
**Related:** [[ai-agent-harness]], [[deep-q-networks]], [[policy-gradient]], [[neural-networks]]

## TL;DR

Reinforcement learning is a machine learning paradigm where an **agent** learns to make decisions by interacting with an **environment**. The agent takes **actions**, receives **rewards** (or penalties), and learns a **policy** — a mapping from states to actions — that maximizes cumulative reward over time. RL powers game-playing AI (AlphaGo, OpenAI Five), robotics, recommendation systems, and LLM alignment techniques like RLHF.

## Explanation

RL is formalized as a **Markov Decision Process (MDP)**:
- **State (s)** — the current situation.
- **Action (a)** — what the agent can do.
- **Reward (r)** — feedback signal from the environment.
- **Transition dynamics** — P(s' | s, a): probability of moving to state s' given action a in state s.
- **Policy (π)** — the agent's strategy: π(a | s).

The goal is to maximize expected cumulative discounted reward:
E[Σ γ^t r_t] where γ is a discount factor (0 < γ ≤ 1).

### Key Algorithms

- **Q-Learning** — Learns a value function Q(s,a): the expected return of taking action a in state s and then following the optimal policy. Model-free.
- **Deep Q-Networks (DQN)** — Uses a neural network to approximate the Q-function, enabling RL in high-dimensional spaces (e.g., raw pixels).
- **Policy Gradient Methods** — Directly optimize the policy parameters using gradients of expected reward. REINFORCE, A2C, PPO.
- **Actor-Critic** — Combines value estimation (critic) with policy optimization (actor).

### RLHF (Reinforcement Learning from Human Feedback)

A special case where the "environment" is human preference rankings. Used to align LLMs like ChatGPT. See [[rlhf]] for details.

## Sources

- [[sentdex-reinforcement-learning]] — Practical Q-learning and DQN implementations
- [[ibm-what-are-ai-agents]] — RL is used for agentic decision-making and alignment
- [[karpathy-state-of-gpt]] — RLHF is the final training stage for modern LLMs

## Connections

- [[ai-agent-harness]] — RL is the training paradigm for many agent systems.
- [[neural-networks]] — Deep RL uses neural networks as function approximators for Q-values or policies.
- [[rlhf]] — A specific RL application for aligning language models with human preferences.

## Open Questions

- How do we make RL sample-efficient enough for real-world robotics?
- Can we make RL agents robust to distribution shifts between training and deployment?
