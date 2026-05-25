---
title: Andrej Karpathy — Deep Learning Education and Research
created: 2026-05-25
updated: 2026-05-25
category: source
tags: [video, youtube, education, deep-learning, neural-networks, transformers, language-models, ai]
creator: Andrej Karpathy
publisher: YouTube
url: https://www.youtube.com/@karpathy
status: active
---

# Andrej Karpathy

**Creator:** [[andrej-karpathy]]  
**Channel:** [youtube.com/@karpathy](https://www.youtube.com/@karpathy)  
**Twitter/X:** [@karpathy](https://twitter.com/karpathy)  
**GitHub:** [github.com/karpathy](https://github.com/karpathy)  
**Subscribers:** 1M+  
**Related:** [[3blue1brown-channel]], [[jeremy-howard-practical-deep-learning]], [[welch-labs-channel]]

## TL;DR

Andrej Karpathy is one of the most influential AI researchers and educators today. A founding member of OpenAI (2015), former Director of AI at Tesla (Autopilot), and now building his own AI companies, Karpathy's YouTube channel stands out for one reason: he implements everything from scratch. From neural networks to GPT-2 to tokenizers, his videos are rigorous, code-forward walkthroughs where every line is typed live and explained.

## Why It's Here

Karpathy bridges research, engineering, and education in a way no one else does. He doesn't summarize papers or explain concepts at a high level — he builds working systems from first principles. His "Zero to Hero" series is the closest thing to a complete deep learning curriculum implemented in raw Python/NumPy.

## Standout Content

### Neural Networks: Zero to Hero Series (2022–2023)
- [The spelled-out intro to neural networks and backpropagation: building micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0) — Implements an autograd engine from scratch.
- [The makemore series](https://www.youtube.com/playlist?list=PLAqhIrjkxAIn_2UMj8s9K2k22VdjCi3) — Builds character-level language models from scratch: bigram, MLP, WaveNet/convolutional, transformer, and GPT.
- **[llm.c](https://github.com/karpathy/llm.c)** — A pure C implementation of GPT-2 training (parallel with the educational videos).

### Let's Build GPT: From Scratch, in Code, Spelled Out (2023)
- Full implementation of a GPT-like transformer trained on the Tiny Shakespeare dataset.
- Covers self-attention, multi-head attention, feedforward layers, layer norm, positional encodings, and the full training loop.
- Written in roughly 300 lines of PyTorch.
- This video alone is arguably the best single-resource introduction to how transformers work under the hood.

### The State of GPT (2023)
- Karpathy's widely cited keynote/lecture breaking down how GPT works: tokenization, embeddings, attention, sampling, and the training pipeline.
- Explains RLHF (Reinforcement Learning from Human Feedback) and the "stochastic parrot" vs. "reasoning engine" debate.

### Let's Build the GPT Tokenizer (2024)
- Implements a Byte Pair Encoding (BPE) tokenizer from scratch.
- Covers merges, vocabularies, and the GPT-2 tokenizer quirks (e.g., handling whitespace, special tokens).

### Let's Reproduce GPT-2 (124M) (2024)
- Full reproduction of GPT-2 (124M parameters) from scratch in roughly 4 hours of video.
- Builds nanoGPT (~300 lines), then scales it up to match GPT-2's architecture and training data (the OpenWebText corpus).
- Demonstrates that the architecture is simple; the challenge is scale.

## Philosophy

> "Neural networks are not that complicated. The hard part is getting the data and the compute."

Karpathy's pedagogy is unapologetically bottom-up. He assumes you know basic Python and some calculus, then builds every layer, every activation, every gradient from first principles. There are no abstractions he doesn't unpack.

## Key Projects

- **[micrograd](https://github.com/karpathy/micrograd)** — A tiny autograd engine (~100 lines) implementing backpropagation over a dynamically built DAG.
- **[nanoGPT](https://github.com/karpathy/nanoGPT)** — The cleanest, smallest, fastest repository for training/fine-tuning medium-sized GPTs.
- **[llm.c](https://github.com/karpathy/llm.c)** — Training LLMs in pure C/CUDA for maximum performance and educational clarity.
- **Tesla Autopilot** — As Director of AI, led the neural network architecture and training for Tesla's FSD stack (2021–2022).
- **OpenAI** — Founding member and research scientist (2015–2017), contributed to early GPT and robotics research.

## Connections to Wiki

- [[3blue1brown-channel]] — 3Blue1Brown visualizes attention and neural networks; Karpathy implements them.
- [[jeremy-howard-practical-deep-learning]] — fast.ai teaches top-down applied deep learning; Karpathy teaches bottom-up from scratch.
- [[statquest-neural-networks]] — StatQuest does the arithmetic step by step; Karpathy does it in code.
- [[tech-with-tim-learn-ml-ai-fast]] — Tim gives a high-level roadmap; Karpathy shows you the actual engine.
- [[backpropagation]] — micrograd is literally a hand-rolled backpropagation engine.

## Who Should Watch

- Developers who want to understand what `torch.nn.Linear` actually does.
- Students who have taken ML courses but still can't implement a model from scratch.
- Researchers who want the clearest possible reference implementation of transformers.
- Anyone who wants to understand why GPT-2 fits in a few hundred lines of PyTorch.

## Agent Notes

- The "Zero to Hero" series is the single highest-leverage deep learning self-study resource available for free.
- nanoGPT is widely forked and used as a starter template for custom transformer experiments.
- llm.c demonstrates that the training algorithm is simple enough to implement in C — the complexity is data and compute engineering.
- Karpathy left Tesla in 2022, returned to OpenAI briefly, then left in 2024 to start his own AI company.
