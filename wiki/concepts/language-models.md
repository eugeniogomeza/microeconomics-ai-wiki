---
title: Language Models
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [nlp, ai, machine-learning, text-generation, next-token-prediction]
status: active
---

# Language Models

**AKA:** LMs, large language models (LLMs), foundation models  
**Related:** [[transformers]], [[tokenization]], [[autoregressive-models]], [[neural-networks]]

## TL;DR

A language model is a probabilistic model that assigns probabilities to sequences of text. Modern language models (especially large language models, or LLMs) are neural networks trained on vast amounts of text data to predict the next token in a sequence. Despite this simple objective, they acquire broad linguistic, reasoning, and world knowledge — making them the foundation of chatbots, code assistants, search engines, and AI agents.

## Explanation

Language models come in two flavors:

**Autoregressive (e.g., GPT)** — Predict the next token conditioned on all previous tokens. Training uses next-token prediction: given "The cat sat on the __", predict "mat".

**Masked (e.g., BERT)** — Predict masked-out tokens given surrounding context. Given "The [MASK] sat on the mat", predict "cat".

The modern LLM training pipeline typically has three stages:
1. **Pre-training** — Next-token prediction on massive text corpora (billions to trillions of tokens). This is where the model learns language, facts, and reasoning patterns.
2. **Supervised Fine-Tuning (SFT)** — Fine-tune on instruction-answer pairs to teach the model to follow instructions and converse.
3. **Alignment (RLHF, DPO)** — Further tune to match human preferences for helpfulness, harmlessness, and honesty.

Key properties that emerge at scale:
- **In-context learning** — The model can perform new tasks from examples in the prompt.
- **Chain-of-thought reasoning** — Prompting the model to "think step by step" dramatically improves reasoning performance.
- **Emergent capabilities** — Abilities like arithmetic, translation, and code generation appear at certain scale thresholds.

## Sources

- [[karpathy-state-of-gpt]] — Full training pipeline: pre-training, SFT, reward modeling, RLHF
- [[karpathy-build-gpt]] — Autoregressive next-token prediction implemented from scratch
- [[3blue1brown-channel]] — Visual explanation of how transformers enable language modeling

## Connections

- [[transformers]] — The dominant architecture for modern language models.
- [[tokenization]] — Text must be converted to integer tokens before a language model can process it.
- [[ai-agent-harness]] — LLMs are the reasoning engine inside most agent systems.

## Open Questions

- How much of LLM reasoning is "real" vs. sophisticated pattern matching?
- Will scaling alone get us to AGI, or are architectural innovations needed?
