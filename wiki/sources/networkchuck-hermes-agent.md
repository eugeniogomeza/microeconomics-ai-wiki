---
title: NetworkChuck — Hermes Agent Review & Tutorial
created: 2026-05-25
updated: 2026-05-25
category: source
tags: [video, youtube, ai-agent, hermes, openclaw, tutorial, nous-research]
author: NetworkChuck
publisher: YouTube
url: https://www.youtube.com/watch?v=QQEgIo4Juxg
status: active
---

# NetworkChuck — Hermes Agent Review & Tutorial

**Author:** [[networkchuck]]  
**Channel:** NetworkChuck  
**Published:** 2026-05-20  
**URL:** [youtu.be/QQEgIo4Juxg](https://www.youtube.com/watch?v=QQEgIo4Juxg)  
**Length:** 32:39  
**Original file:** (none — fetched directly)

## TL;DR

NetworkChuck's review of Hermes, an open-source AI agent from Nous Research, after one month of daily use. He walks through installation on a $5 VPS, compares it to OpenClaw, and demonstrates why he switched: the "vibe," persistent memory architecture, the team behind it, self-improving skills, and reliability.

## Key Claims

1. **Hermes is an OpenClaw alternative** — Built by Nous Research, designed to be lightweight, stable, and genuinely self-improving rather than bloated with marketplace skills. It feels like a product rather than a project.
2. **Memory architecture is superior** — Hermes enforces hard size limits on its `USER.md` (~1,375 chars) and `MEMORY.md` (~2,200 chars), forcing the agent to curate what matters. This prevents the bloat OpenClaw experiences over time.
3. **Honcho integration for long-term memory** — A peer service called Honcho reasons over interactions and builds a "peer card" of the user's personality and preferences, injecting relevant context into the system prompt in real time.
4. **Self-improving skills** — Hermes can write its own skills based on user interactions. NetworkChuck demonstrates Ron (his IT agent persona) creating a Twingate client operations skill and a UniFi network operations skill after being given tasks.
5. **Reliability** — NetworkChuck reports using Hermes for a month without issues, something he couldn't say about OpenClaw, which degraded over time with updates breaking things.

## Entities Mentioned

- [[nous-research]] — Company behind Hermes; open-source AI research group, also develops the Hermes LLM series.
- [[jeff-quesnelle]] — Co-founder, Nous Research (interviewed in the video).
- [[teknium]] — Co-founder & Head of Post-Training, Nous Research.
- [[karan-malhotra]] — Co-founder & Head of Behavior, Nous Research.
- [[bowen-peng]] — Co-founder, YaRN co-author, Nous Research.
- [[honcho]] — Memory layer by Plastic Labs that integrates with Hermes for long-term personality/memory.
- [[ron-weasley]] — NetworkChuck's IT agent persona, an IT admin named after the Harry Potter character.

## Concepts Discussed

- [[ai-agent-harness]] — Hermes is an agent harness that connects to any LLM (OpenAI Codex, Grok, local models via LM Studio).
- [[persistent-memory]] — How AI agents maintain state across sessions; Hermes uses curated files + optional Honcho peer cards.
- [[self-improving-skills]] — Agents that generate reusable skill modules based on past interactions.
- [[it-automation]] — Using an AI agent for network inventory, Home Assistant control, UniFi management.
- [[agent-deployment]] — Installing on a VPS, systemd service, Telegram bot integration.

## Notable Quotes

> "Hermes is the fastest growing GitHub project. It just topped OpenClaw on the OpenRouter token usage."

> "The idea that the Hermes agent grows with you, that it's gonna be better on day 30 than day one."

> "Get out of the way with the models... the model is the brain. We just need to give it the hands, the feet, the fingers to touch the world."

> "Ron just made his own skill. That's the power of Hermes."

## Connections to Other Sources

- (none yet — first source)

## Agent Notes

- This source is a primary reference for anyone evaluating AI agent tools.
- Links to practical: VPS install, Telegram bot setup, systemd service.
- The self-improvement loop (Curator skill) is a concept worth deeper exploration.
- NetworkChuck's Ron Weasley persona is a great example of persona-engineering for agents.
