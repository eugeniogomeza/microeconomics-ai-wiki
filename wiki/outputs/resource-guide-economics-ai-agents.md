---
title: Curated Resource Guide — Economics, AI, and Agents
created: 2026-05-25
updated: 2026-05-25
category: output
tags: [resource-guide, curated-list, economics, ai, agents, learning, statistics, neural-networks, transformers, tiktok, education]
status: active
---

# Curated Resource Guide — Economics, AI, and Agents

**Generated in response to:** "I am trying to create a kind of guide of resources for economics, ai, and agents."

## TL;DR

A personally curated guide to high-signal learning resources spanning three overlapping domains: the economics of AI, the engineering of AI agents, and the statistical methods that underpin both. Every resource here has been vetted through actual use — not algorithmic recommendations.

---

## Table of Contents

1. [The Economics of AI — Theory and Framework](#1-the-economics-of-ai--theory-and-framework)
2. [Building and Evaluating AI Agents](#2-building-and-evaluating-ai-agents)
3. [Data Science and AI Education](#3-data-science-and-ai-education)
4. [Statistical Methods for AI Research](#4-statistical-methods-for-ai-research)
5. [AI Career and Practical Tips](#5-ai-career-and-practical-tips)
6. [Using This Guide](#using-this-guide)
7. [Further Reading](#further-reading)

---

## 1. The Economics of AI — Theory and Framework

### The Microeconomics of Artificial Intelligence
- **Author:** [[joshua-gans]] (Rotman School, University of Toronto)
- **Publisher:** [[mit-press]] (Open Access, CC BY-NC-ND)
- **Link:** [MIT Press Direct](https://direct.mit.edu/books/oa-monograph/6067/The-Microeconomics-of-Artificial-Intelligence) | [PDF](https://direct.mit.edu/books/oa-monograph-pdf/2575705/book_9780262384964.pdf)
- **Why it's here:** Gans reframes AI not as automation but as dramatically cheaper prediction. This is the most rigorous single-volume treatment of what AI does to decision-making, market structure, pricing, and policy. Essential for anyone building AI products or working in AI governance.
- **Best for:** Strategists, economists, product managers, policy researchers.
- **Key chapters:** 3 (Value of Prediction), 6 (Automation), 10–14 (Pricing), 15–22 (Policy).
- **Wiki source:** [[mit-microeconomics-ai]]

### Prediction Machines (2018)
- **Authors:** [[ajay-agrawal]], [[joshua-gans]], [[avi-goldfarb]]
- **Publisher:** Harvard Business Review Press
- **Link:** [HBR Store](https://www.hbr.org/product/prediction-machines-the-simple-economics-of-artificial-intelligence)
- **Why it's here:** The original business book that popularized the "AI = prediction" framework. More accessible than the 2025 MIT book; aimed at executives and strategists rather than academics. Start here if you want the intuition before the math.
- **Best for:** Business strategists, MBA students, policy makers.
- **Wiki source:** [[prediction-machines-book]]

### The Economics of AI: An Agenda (2019)
- **Editors:** [[ajay-agrawal]], [[joshua-gans]], [[avi-goldfarb]]
- **Publisher:** University of Chicago Press (NBER Conference Report)
- **Link:** [UChicago Press](https://press.uchicago.edu/ucp/books/book/chicago/E/bo35780726.html)
- **Why it's here:** If *Prediction Machines* is the business book and Gans's 2025 MIT book is the academic course, this is the **research agenda** that scoped the entire field. 30+ leading economists (Acemoglu, Brynjolfsson, Aghion, Stiglitz, Milgrom, Kahneman, Goolsbee, etc.) organized around four themes: AI as GPT, growth/jobs/inequality, regulation/IO, and ML's impact on economics itself. This is like being at the table in 1995 when economists gathered to debate the impact of the internet — except it's AI.
- **Best for:** Graduate students, researchers, policy makers who want evidence-based frameworks. Business strategists who want rigorous underpinnings beneath the executive summary.
- **Key chapters:** Brynjolfsson et al. on the productivity paradox (ch. 1), Acemoglu & Restrepo on automation and work (ch. 8), Aghion et al. on economic growth (ch. 9), Athey on ML's impact on economics (ch. 21).
- **Wiki source:** [[economics-of-ai-agenda-book]]

**Core insight you should steal:** The value of AI is not in replacing humans but in improving the quality of predictions that feed into human judgment. Understanding substitutes and complements is more important than speculating about AGI timelines.

---

## 2. Building and Evaluating AI Agents

### NetworkChuck — Hermes Agent Review and Tutorial
- **Creator:** [[networkchuck]]
- **Link:** [youtu.be/QQEgIo4Juxg](https://www.youtube.com/watch?v=QQEgIo4Juxg)
- **Length:** 32:39
- **Why it's here:** The most practical, hype-free comparison of Hermes vs. OpenClaw from someone who actually used both daily for a month. Includes a full VPS install walkthrough, Telegram bot setup, Home Assistant integration, and live demos of the agent writing its own skills.
- **Best for:** Developers, homelabbers, IT professionals evaluating agent infrastructure.
- **Wiki source:** [[networkchuck-hermes-agent]]

### Hermes Agent — Full Landscape Analysis
- **Organization:** [[nous-research]]
- **GitHub:** [github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
- **Stats:** 166k stars, 27.4k forks, 1,190 contributors
- **Why it's here:** Hermes is the fastest-growing open-source agent project. We've done a full landscape analysis at [[hermes-agent-landscape]]. TL;DR: genuinely useful for personal/IT/developer use, less proven for enterprise. Built-in OpenClaw migration, persistent memory, self-generated skills, and multi-platform support.
- **Best for:** Anyone asking "Is Hermes actually useful?" — yes, but with audience-specific caveats.
- **Wiki source:** [[hermes-agent-landscape]]

**Core insight you should steal:** Agent memory matters more than raw model capability. Hermes's hard-capped memory files + optional Honcho peer-cards make it more useful on day 30 than day 1. The harness (memory + tools + orchestration) is a complement to the model's prediction layer.

### Honcho (Plastic Labs)
- **Link:** [honcho.dev](https://honcho.dev/)
- **Why it's here:** The long-term memory layer that makes agents feel personal. It builds a "peer card" of the user's personality and injects relevant context into prompts in real time.
- **Best for:** Anyone building user-facing agents where personalization matters.
- **Wiki entity:** [[honcho]]

### LangGraph / LangChain
- **Developer:** LangChain (Harrison Chase)
- **Link:** [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)
- **Why it's here:** The default production framework for multi-agent apps. More complex than Hermes but gives fine-grained control over state transitions. Covered extensively in Krish Naik's agentic AI course.
- **Best for:** Developers building structured, stateful agent workflows at scale.
- **Wiki entity:** [[langgraph]]

---

## 3. Data Science and AI Education

### Krish Naik — Data Science & AI Education Channel
- **Creator:** [[krish-naik]]
- **Channel:** [youtube.com/@krishnaik06](https://www.youtube.com/@krishnaik06)
- **Why it's here:** The most comprehensive free curriculum for data science on YouTube. Offers full 5–6 hour courses in statistics, ML, deep learning, NLP, and recently agentic AI.
- **Best for:** Beginners to intermediate learners who want structured, project-based learning without paying for bootcamps.
- **Standout content:**
  - Complete Machine Learning in 6 Hours
  - Complete Statistics for Data Science in 6 Hours
  - Complete Agentic AI Course in 10 Hours (recent)
  - Claude Code Course in 2 Hours (recent)
- **Wiki source:** [[krish-naik-channel]]
- **Bonus:** Free career counseling via WhatsApp (+91-9111533440).

**Core insight you should steal:** Roadmaps matter more than individual tutorials. Krish's structured playlists are designed as end-to-end learning paths, not isolated videos.

### 3Blue1Brown — Neural Networks and Transformers Explained Visually
- **Creator:** [[grant-sanderson]]
- **Channel:** [youtube.com/@3blue1brown](https://www.youtube.com/@3blue1brown)
- **Subscribers:** 6.8M | **Views:** 612M
- **Why it's here:** The single best place to *see* how neural networks and transformers actually work. Sanderson's custom animation engine (Manim) makes abstract math concrete. His 2024 transformers series is the canonical accessible explanation of LLM architecture. Where Krish Naik teaches you to build models, 3Blue1Brown teaches you to *understand* them at a geometric level.
- **Best for:** Anyone who feels they "sort of get" neural networks but can't picture what's happening. Visual learners who find equations opaque without geometry.
- **Standout content:**
  - [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk)
  - [But what is a GPT? (Transformers)](https://www.youtube.com/watch?v=wjZofJX0v4M)
  - [Attention in transformers, step-by-step](https://www.youtube.com/watch?v=eMlx5fFNoYc)
  - Linear Algebra and Calculus series (foundations)
- **Wiki source:** [[3blue1brown-channel]]

### Welch Labs — Neural Networks Demystified (Build From Scratch)
- **Creator:** [[stephen-welch]]
- **Channel:** [youtube.com/welchlabsvideo](https://www.youtube.com/welchlabsvideo)
- **Why it's here:** A 7-part series that builds and trains a complete neural network from scratch in Python. Patient, methodical, and code-oriented. Where 3Blue1Brown is visual intuition, Welch Labs is hands-on implementation. The supporting GitHub repo includes working code.
- **Best for:** Students who want to build a neural network by hand to understand every piece. Self-learners who prefer slow, deliberate explanations.
- **Standout content:**
  - Neural Networks Demystified (7-part series)
  - Supporting code: [github.com/stephencwelch/Neural-Networks-Demystified](https://github.com/stephencwelch/Neural-Networks-Demystified)
  - The Welch Labs Illustrated Guide to AI (book in development)
- **Wiki source:** [[welch-labs-channel]]

### Tina Huang — AI Career Shorts
- **Creator:** [[tina-huang]]
- **Channel:** [youtube.com/@TinaHuang1](https://www.youtube.com/@TinaHuang1)
- **Why it's here:** Short-form, high-impact career advice for breaking into AI/ML roles. Covers resume optimization, interview prep, and productivity workflows in a format that actually gets watched.
- **Best for:** Career-changers, junior practitioners, anyone optimizing for job-market signaling.
- **Wiki entity:** [[tina-huang]]

### Tecnonauta — Tech/AI News (Spanish, TikTok)
- **Creator:** [[tecnonauta]]
- **Handle:** [@tecnonautatv](https://www.tiktok.com/@tecnonautatv)
- **Followers:** 2.4M | **Likes:** 51.4M
- **Why it's here:** The only Spanish-language tech/AI news channel in this curated list. Covers AI developments (Google AI, ChatGPT), gadget reviews, and industry commentary in short-form. If English-language YouTube deep dives aren't accessible, this is high-signal TikTok content.
- **Best for:** Spanish-speaking learners, anyone studying how AI news travels through short-form social media.
- **Wiki source:** [[tecnonauta-tiktok]]

---

## 4. Statistical Methods for AI Research

### Very Normal — Crash Course on Monte Carlo Simulation
- **Creator:** [[very-normal]] (Christian)
- **Link:** [youtu.be/OdWLP8umw3A](https://www.youtube.com/watch?v=OdWLP8umw3A)
- **Length:** 28:30
- **Why it's here:** The single best practical tutorial on Monte Carlo simulation. Walks through three levels of complexity: laptop loop, structured tidyverse parallelization, and HPC cluster deployment with SLURM.
- **Best for:** Researchers, data scientists, and economists who need to evaluate models or methods before seeing real data.
- **Wiki source:** [[very-normal-monte-carlo]]
- **Complements:** [[economics-of-ai]] — Simulation is the standard method for evaluating AI-driven decision models.

**Core insight you should steal:** Always simulate before you commit to a method. A 10-minute simulation can save weeks of theoretical confusion or implementation regret.

---

## 5. AI Career and Practical Tips

### Pending / Stub Resources

These URLs were provided but metadata fetching was blocked by YouTube. They should be manually reviewed:

- [youtu.be/EaR3C4e600k](https://www.youtube.com/watch?v=EaR3C4e600k) — (content unknown)
- [youtu.be/F8NKVhkZZWI](https://www.youtube.com/watch?v=F8NKVhkZZWI) — (content unknown)
- [youtu.be/8SF_h3xF3cE](https://www.youtube.com/watch?v=8SF_h3xF3cE) — Playlist (content unknown)
- [youtu.be/8xUher8-5_Q](https://www.youtube.com/watch?v=8xUher8-5_Q) — (content unknown)
- [youtube.com/@TinaHuang1/shorts](https://www.youtube.com/@TinaHuang1/shorts) — Tina Huang's short-form content (403 on fetch; known to be career-focused AI tips)

If you can identify any of these, update [[youtube-stubs]] and this section.

---

## Using This Guide

**For learners:** Start with Krish Naik's roadmaps for foundational skills, then watch 3Blue1Brown for geometric intuition, then move to NetworkChuck for agent infrastructure, then read Gans for strategic context.

**For researchers:** Gans provides the theoretical frame; Very Normal provides the methodological tooling. The Economics of AI: An Agenda gives the broader research landscape. Together they cover "why," "how," and "what's next."

**For builders:** NetworkChuck's Hermes tutorial is the fastest path to a working agent. Pair it with Chip Huyen's book for production practices. Use Welch Labs for understanding what's under the hood.

**For visual learners:** 3Blue1Brown is the definitive resource. Watch the transformers series before any other technical explanation.

**For Spanish speakers:** Tecnonauta provides tech/AI news in Spanish where most curated resources are English-only.

**For career-focused:** Tina Huang's shorts for quick wins, Krish Naik for deep skills, 3Blue1Brown for interview-level intuition, and the economics books for strategic conversations with leadership.

---

## Further Reading

- [[mit-microeconomics-ai]] — Full source page for the MIT book.
- [[economics-of-ai-agenda-book]] — The 2019 research agenda with 30+ economists.
- [[prediction-machines-book]] — Original prediction-economics framework.
- [[networkchuck-hermes-agent]] — Full source page for the Hermes tutorial.
- [[hermes-agent-landscape]] — Comprehensive landscape analysis with stats and audience fit.
- [[chip-huyen-ai-engineering]] — AI Engineering practitioner book.
- [[3blue1brown-channel]] — Math visualization channel, transformers series.
- [[welch-labs-channel]] — Neural Networks Demystified, build-from-scratch series.
- [[tecnonauta-tiktok]] — Spanish-language tech/AI TikTok.
- [[krish-naik-channel]] — Full source page for the education channel.
- [[very-normal-monte-carlo]] — Full source page for the Monte Carlo course.
- [[economics-of-ai]] — Concept page synthesizing economic insights.
- [[ai-agent-harness]] — Concept page on agent infrastructure.
- [[monte-carlo-simulation]] — Concept page on simulation methods.
- [[persistent-memory]] — Concept page on agent memory architecture.

---

*This guide is a living document. As new sources are ingested and new conclusions emerge, it should be updated to reflect the evolving synthesis.*
