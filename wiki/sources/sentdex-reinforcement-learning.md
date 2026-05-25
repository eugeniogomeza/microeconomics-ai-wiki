---
title: "Sentdex: Reinforcement Learning with Q-Learning and OpenAI Gym"
url: "https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJF5U7e2P1F3Jz_kGIPUr"
category: source
tags: [reinforcement-learning, q-learning, dqn, openai-gym, python, video, sentdex]
author: Harrison Kinsley
publisher: YouTube
speaker: Harrison Kinsley
created: 2026-05-25
updated: 2026-05-25
---

# Sentdex: Reinforcement Learning with Q-Learning and OpenAI Gym

## Source Details

- **URL:** [https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJF5U7e2P1F3Jz_kGIPUr](https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJF5U7e2P1F3Jz_kGIPUr)
- **Channel:** [Sentdex](https://www.youtube.com/@sentdex)
- **Presenter:** [[harrison-kinsley]]
- **Published:** ~2019–2020
- **Duration:** ~15–30 minutes per video, ~20 videos in series
- **Views:** 2M+ across series
- **Status:** Practical RL from first principles

## Summary

Harrison Kinsley implements reinforcement learning algorithms from scratch in Python and applies them to classic OpenAI Gym environments. Starting with tabular Q-learning on deterministic grid worlds, the series progresses to Deep Q-Networks (DQN) for continuous Atari games. He covers epsilon-greedy exploration, experience replay, target networks, and policy gradient methods — showing both the theory and the bugs that arise when you actually try to make RL work.

## Key Claims

- **Q-learning learns a value function** — the Q-table (or Q-network) stores the expected return of taking action a in state s.
- **Exploration vs. exploitation is the core challenge** — epsilon-greedy balances random exploration with greedy exploitation of known rewards.
- **Deep Q-Networks scale Q-learning to large state spaces** — a neural network replaces the Q-table, using experience replay and target networks for stability.
- **Experience replay breaks correlation** — storing and randomly sampling past transitions prevents the network from overfitting to recent experiences.
- **Target networks stabilize learning** — using a separate, slowly updated network for Q-value targets prevents oscillation.
- **RL is notoriously hard to get working** — hyperparameters, reward shaping, and environment dynamics matter enormously.

## Concepts Discussed

- [[reinforcement-learning]] — Learning by trial and error with environmental rewards
- [[q-learning]] — Model-free RL algorithm that learns a state-action value function
- [[deep-q-networks]] — Neural network approximator for Q-values in large/continuous spaces
- [[epsilon-greedy]] — Exploration strategy: random action with probability ε, greedy action otherwise
- [[experience-replay]] — Storing past transitions and sampling minibatches for training
- [[policy-gradient]] — Methods that directly optimize the policy rather than value functions

## Connections to Other Sources

- [[andrej-karpathy-channel]] — Karpathy's Pong from pixels (REINFORCE) is a spiritual predecessor; Sentdex covers DQN in more depth.
- [[ibm-what-are-ai-agents]] — RL is the technique used to align agent behavior with goals.

## Source References

- [Sentdex: RL with Q-Learning playlist](https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJF5U7e2P1F3Jz_kGIPUr)
- [OpenAI Gym documentation](https://www.gymlibrary.dev/)
