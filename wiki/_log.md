---
title: Wiki Log
created: 2026-05-25
updated: 2026-05-25
category: meta
tags: [log, meta]
status: active
---

# Wiki Log

Chronological record of all operations performed on this wiki.

## [2026-05-25 16:30] ingest | Two Minute Papers + Sentdex — research awareness + practical coding channels

- Created source pages:
  - [[two-minute-papers-channel]] — Channel overview for Two Minute Papers (1.7M+ subs)
  - [[two-minute-papers-nerf]] — Neural Radiance Fields paper summary
  - [[two-minute-papers-text-to-image]] — Text-to-image diffusion model summaries
  - [[sentdex-channel]] — Channel overview for Sentdex (1.3M+ subs)
  - [[sentdex-neural-networks-scratch]] — Neural networks from scratch in NumPy
  - [[sentdex-reinforcement-learning]] — Q-learning and DQN with OpenAI Gym
- Created entity pages:
  - [[karoly-zsolnai-feher]] — Creator of Two Minute Papers, AI research summarizer
  - [[harrison-kinsley]] — Creator of Sentdex, Python/ML educator
- Created concept pages:
  - [[neural-radiance-fields]] — 3D scene representation via neural networks
  - [[diffusion-models]] — Generative models via iterative denoising
  - [[reinforcement-learning]] — Learning by trial and error with environmental rewards
- Updated [[_index]], [[00-overview]], [[_log]]
- Pages touched: 6 sources, 2 entities, 3 concepts
- Notes: Following the user's request to inject more channels. These two complete the set of practical channels alongside StatQuest and Karpathy: Two Minute Papers for research awareness, Sentdex for code-level implementation.

## [2026-05-25 15:45] ingest | Andrej Karpathy — deep learning from scratch, GPT training pipeline

- Created source pages:
  - [[andrej-karpathy-channel]] — Channel overview for Andrej Karpathy
  - [[karpathy-neural-networks-zero-to-hero]] — Neural Networks: Zero to Hero (makemore series)
  - [[karpathy-build-gpt]] — Let's Build GPT: transformer from scratch in PyTorch
  - [[karpathy-state-of-gpt]] — The State of GPT: pre-training, SFT, reward modeling, RLHF
- Created entity page: [[andrej-karpathy]] — Former OpenAI/Tesla researcher, deep learning educator
- Created concept pages:
  - [[transformers]] — Attention-based sequence modeling architecture
  - [[language-models]] — Probabilistic models of text
  - [[tokenization]] — Text-to-token mapping for language models
  - [[autoregressive-models]] — Left-to-right sequence generation
  - [[self-attention]] — Core mechanism inside transformers
  - [[rlhf]] — Reinforcement Learning from Human Feedback for LLM alignment
- Updated [[_index]], [[00-overview]], [[_log]]
- Pages touched: 4 sources, 1 entity, 6 concepts
- Notes: User selected Karpathy as the second channel to inject after StatQuest. YouTube fetches remain blocked by anti-bot measures (403); content built from well-established public knowledge. Karpathy's nanoGPT (300-line PyTorch transformer) is the canonical reference implementation for transformers. The Zero to Hero series is the highest-leverage free deep learning curriculum for from-scratch understanding.

## [2026-05-25 15:00] ingest | StatQuest with Josh Starmer — channel overview + key video series

- Created source pages:
  - [[statquest-channel]] — Channel overview for StatQuest (1.2M+ subs)
  - [[statquest-pca]] — Principal Component Analysis (10M+ views, canonical PCA explainer)
  - [[statquest-neural-networks]] — Neural Networks series (forward propagation + backpropagation)
  - [[statquest-linear-regression]] — Linear Regression (5M+ views)
  - [[statquest-logistic-regression]] — Logistic Regression (3M+ views)
- Created entity page: [[josh-starmer]] — StatQuest creator, statistics and ML educator
- Created concept pages:
  - [[neural-networks]] — Biologically inspired computational models
  - [[principal-component-analysis]] — Linear dimensionality reduction technique
  - [[linear-regression]] — Foundational supervised learning method
  - [[logistic-regression]] — Binary classification via sigmoid link
  - [[backpropagation]] — Gradient computation algorithm enabling deep learning
- Updated [[_index]], [[00-overview]], [[_log]]
- Pages touched: 5 sources, 1 entity, 5 concepts
- Notes: User selected StatQuest from research into channels similar to 3Blue1Brown and Welch Labs. YouTube page fetches remain blocked by anti-bot measures (403); content built from established public knowledge and channel metadata. Channel-level + individual video pages created per user preference.

## [2026-05-25 12:15] ingest | Curated YouTube and book resources for economics/AI/agents

- Processed URLs provided by user:
  - https://www.youtube.com/watch?v=QQEgIo4Juxg (NetworkChuck — Hermes)
  - https://www.youtube.com/watch?v=OdWLP8umw3A (Very Normal — Monte Carlo)
  - https://www.youtube.com/@krishnaik06 (Krish Naik channel)
  - https://direct.mit.edu/books/oa-monograph/6067/The-Microeconomics-of-Artificial-Intelligence (MIT book)
- Stubbed failed fetches for EaR3C4e600k, F8NKVhkZZWI, 8SF_h3xF3cE, 8xUher8-5_Q, @TinaHuang1
- Created source pages: [[networkchuck-hermes-agent]], [[very-normal-monte-carlo]], [[krish-naik-channel]], [[mit-microeconomics-ai]], [[youtube-stubs]]
- Created entity pages: [[networkchuck]], [[krish-naik]], [[joshua-gans]], [[very-normal]], [[tina-huang]], [[nous-research]], [[jeff-quesnelle]], [[honcho]], [[openclaw]], [[mit-press]], [[krish-naik-academy]]
- Created concept pages: [[economics-of-ai]], [[ai-agent-harness]], [[monte-carlo-simulation]], [[persistent-memory]]
- Created output: [[resource-guide-economics-ai-agents]]
- Updated [[_index]], [[00-overview]], [[_log]]
- Pages touched: 5 sources, 11 entities, 4 concepts, 1 output
- Notes: First real ingest. YouTube anti-bot measures blocked some fetches; flagged in stubs. Guide intentionally ties economics, engineering, and methods together.

## [2026-05-25 14:15] ingest | Retry of failed YouTube fetches — 4 new sources ingested

- Successfully fetched and ingested:
  - https://www.youtube.com/watch?v=EaR3C4e600k (ritvikmath — Monte Carlo Simulations)
  - https://www.youtube.com/watch?v=F8NKVhkZZWI (IBM Technology / Maya Murad — What are AI Agents?)
  - https://www.youtube.com/watch?v=8SF_h3xF3cE (Jeremy Howard — Practical Deep Learning Lesson 1)
  - https://www.youtube.com/watch?v=8xUher8-5_Q (Tech With Tim — Learn ML/AI FAST)
- Still blocked: https://www.youtube.com/@TinaHuang1/shorts (403 Forbidden) — retained in [[youtube-stubs]]
- TikTok URLs still blocked by anti-bot measures — retained in [[tiktok-stubs]]
- Created source pages: [[ritvikmath-monte-carlo-simulations]], [[ibm-what-are-ai-agents]], [[jeremy-howard-practical-deep-learning]], [[tech-with-tim-learn-ml-ai-fast]]
- Created entity pages: [[ritvikmath]], [[maya-murad]], [[ibm-technology]], [[jeremy-howard]], [[fastai]], [[tech-with-tim]]
- Updated [[_index]], [[00-overview]], [[_log]], [[youtube-stubs]]
- Pages touched: 4 sources, 6 entities
- Notes: Retry succeeded for four previously failed YouTube URLs. Original error was likely transient anti-bot/block. TikTok remains fully inaccessible via direct fetch.

## [2026-05-25 12:45] ingest | Additional resources: AI Engineering book, Prediction Machines, Hermes landscape

- Created sources:
  - [[chip-huyen-ai-engineering]] — Chip Huyen's AI Engineering (O'Reilly 2024/25)
  - [[prediction-machines-book]] — Agrawal/Gans/Goldfarb, Prediction Machines (2018)
  - [[hermes-agent-landscape]] — GitHub data + architecture analysis for Hermes
- Created entities:
  - [[chip-huyen]], [[ajay-agrawal]], [[avi-goldfarb]], [[oreilly-media]], [[langgraph]]
- Created concept stub: LangGraph framework
- Updated [[resource-guide-economics-ai-agents]] with new books and agent framework landscape
- Updated [[_index]] with new sources/entities
- Notes: User asked about Hermes/OpenClaw usefulness. Filed comprehensive landscape analysis with star counts, feature breakdown, and target audience fit. Prediction Machines added as precursor to Gans's 2025 book. Landscape analysis confirms Hermes is genuinely useful for personal/IT/developer use, less proven for enterprise.

## [2026-05-25 11:40] create | Initialize LLM Wiki

- Created directory structure: `raw/`, `raw/assets/`, `wiki/`, `tools/`
- Created schema: `AGENTS.md`
- Created index: `wiki/_index.md`
- Created log: `wiki/_log.md`
- Created overview: `wiki/00-overview.md`
- Created templates: `wiki/_templates.md`
- Created README: `README.md`
- Created tool stubs: `tools/search.py`, `tools/lint.py`
- Pages touched: [[_index]], [[_log]], [[00-overview]], [[_templates]]
- Notes: Wiki initialized. Ready for first ingest.
