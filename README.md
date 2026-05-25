# Microeconomics & AI Wiki

> Curated knowledge base on AI, deep learning, and the microeconomics of artificial intelligence.

## What This Is

A systematically maintained personal knowledge base ("second brain") that catalogs sources, concepts, and cross-references across two domains:

1. **The microeconomics of AI** — AI as prediction technology, market structures, pricing, and policy implications (building on Joshua Gans, Agrawal, and Goldfarb's work).
2. **Deep learning & AI education** — Transformer architectures, reinforcement learning, generative models, and the pedagogical landscape (building on sources like Andrej Karpathy, 3Blue1Brown, and StatQuest).

## Structure

```
llm-wiki/
├── AGENTS.md              # Wiki schema and conventions
├── README.md              # This file
├── raw/                   # Immutable source materials
│   └── assets/            # Downloaded images
├── wiki/                  # Knowledge base (Obsidian-compatible)
│   ├── _index.md          # Catalog of all pages
│   ├── _log.md            # Chronological operations log
│   ├── _templates.md      # Page templates
│   ├── 00-overview.md     # High-level synthesis
│   ├── sources/           # Summaries of ingested sources (32)
│   ├── entities/          # People, orgs, products (30)
│   ├── concepts/          # Ideas, frameworks, theories (18)
│   ├── questions/         # Open questions (1)
│   └── outputs/           # Generated analyses (1)
└── tools/
    ├── search.py          # Full-text search
    └── lint.py            # Orphan/contradiction checker
```

## Key Content Areas

### Microeconomics of AI

| Source | Description |
|--------|-------------|
| [MIT Microeconomics of AI](wiki/sources/mit-microeconomics-ai.md) | Joshua Gans (2025) — open-access single-author treatment |
| [Prediction Machines](wiki/sources/prediction-machines-book.md) | Agrawal/Gans/Goldfarb (2018) — business primer |
| [Economics of AI: An Agenda](wiki/sources/economics-of-ai-agenda-book.md) | NBER volume — multi-author research agenda |
| [AI Agent Market Structure](wiki/questions/ai-agent-market-structure.md) | Will harnesses consolidate or fragment? |

### Deep Learning Education

| Source | Description |
|--------|-------------|
| [Andrej Karpathy](wiki/sources/andrej-karpathy-channel.md) | nanoGPT, Zero to Hero, from-scratch transformers |
| [3Blue1Brown](wiki/sources/3blue1brown-channel.md) | Geometric intuition for neural nets and transformers |
| [StatQuest](wiki/sources/statquest-channel.md) | Step-by-step statistical ML |
| [Sentdex](wiki/sources/sentdex-channel.md) | Practical NumPy/PyTorch implementations |
| [Two Minute Papers](wiki/sources/two-minute-papers-channel.md) | Research summaries: NeRF, diffusion, LLMs |

### Concept Stubs

- Transformers, self-attention, tokenization, language models
- Backpropagation, reinforcement learning (RLHF)
- Neural radiance fields, diffusion models
- Economics of AI: prediction, complements, market structure

## How This Was Built

This wiki was created and maintained by an LLM agent with human curation. Sources were selected based on perceived quality and cross-referenced automatically. Every page includes YAML frontmatter for structured querying. The wiki is designed to be opened as an [Obsidian](https://obsidian.md/) vault.

## Stats

- **32** sources ingested (books, YouTube channels, research summaries)
- **30** entities cataloged (researchers, creators, organizations)
- **18** concepts with dedicated pages
- **1** open question tracked
- **1** generated output (resource guide)

## License

MIT — use it, fork it, make it yours.

---

*Maintained with an LLM agent. Last lint: 85 pages, 0 issues.*
