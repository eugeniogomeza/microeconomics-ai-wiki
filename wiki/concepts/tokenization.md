---
title: Tokenization
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [nlp, preprocessing, text, vocabulary, subword]
status: active
---

# Tokenization

**AKA:** text tokenization, subword tokenization  
**Related:** [[language-models]], [[transformers]], [[gpt]]

## TL;DR

Tokenization is the process of converting raw text into a sequence of integers that a language model can process. It is not a simple split-by-spaces operation — modern tokenizers use subword algorithms (like Byte Pair Encoding) to handle rare words, misspellings, and languages with large vocabularies efficiently. Tokenization is the unavoidable bridge between human-readable text and machine-readable numbers.

## Explanation

Every language model has a **vocabulary** — a fixed-size set of tokens (typically 32,000 to 200,000 tokens). The tokenizer maps text to token IDs and back.

### Common Tokenization Approaches

- **Word-level** — Split on spaces. Fails on rare words, typos, and out-of-vocabulary tokens.
- **Character-level** — No OOV problem, but sequences are very long and lose word semantics.
- **Subword (BPE, WordPiece, SentencePiece)** — The modern standard. Starts with character-level vocabulary and iteratively merges the most frequent adjacent pairs. Words are split into frequent subwords: "unhappiness" → ["un", "happiness"] or ["un", "happ", "iness"].

### Why Tokenization Matters

- **Vocabulary size vs. sequence length tradeoff** — Larger vocabularies mean fewer tokens per sentence but more parameters in the embedding layer.
- **Tokenizer quirks** — GPT-2's tokenizer handles whitespace in unusual ways; "  hello" and "hello" get different token IDs.
- **Multilingual challenges** — Languages with different scripts or no whitespace (e.g., Chinese, Thai) require different tokenization strategies.

### Key Algorithms

- **Byte Pair Encoding (BPE)** — Iteratively merges frequent character pairs. Used in GPT-2, GPT-3, GPT-4.
- **WordPiece** — Similar to BPE but maximizes likelihood of training data. Used in BERT.
- **SentencePiece** — Directly trains on raw text without pre-tokenization. Used in T5, LLaMA.

## Sources

- [[karpathy-build-gpt]] — Token embedding layer in the nanoGPT implementation
- [[karpathy-neural-networks-zero-to-hero]] — Character-level tokenization in makemore

## Connections

- [[language-models]] — Tokenization is the mandatory first step before any language model can process text.
- [[transformers]] — The input to a transformer is always a sequence of token embeddings.

## Open Questions

- How will "tokenization-free" models (e.g., byte-level or continuous representations) affect performance?
- Can we design tokenizers that are more robust to adversarial inputs?
