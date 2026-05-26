---
title: Hermes Agent
created: 2026-05-26
updated: 2026-05-26
category: entity
tags: [product, ai-agent, open-source, harness, nous-research]
status: active
---

# Hermes Agent

**Type:** Product / AI Agent Harness
**Developer:** [[nous-research]]
**URL:** [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)
**License:** Open Source / MIT

## TL;DR

Hermes Agent is an autonomous, self-improving AI agent harness from Nous Research. Unlike IDE-tethered copilots or chatbot wrappers, it runs persistently on a server, supports multi-platform communication (Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI), and auto-generates skills from interactions. It is positioned as a lighter, more stable alternative to OpenClaw.

## Key Features

- **Persistent Memory** — Remembers projects and past solutions; auto-curates skills.
- **Multi-Platform** — Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI.
- **Sandboxing** — Five backends: local, Docker, SSH, Singularity, Modal.
- **Subagent Delegation** — Isolated subagents with their own terminals and Python RPC.
- **Scheduled Automations** — Natural-language cron for reports, backups, briefings.
- **Full Web Control** — Search, browser automation, vision, image generation, TTS.

## Comparison to OpenClaw

| Dimension | Hermes | OpenClaw |
|-----------|--------|----------|
| Memory | Hard-capped, auto-curated | Auto-growing, can bloat |
| Skills | Self-generated from use | Marketplace/downloads |
| Stability | More stable | Degrades with updates |
| Philosophy | Opinionated, fewer options | Configurable everything |
| Vibe | Fun, aesthetic, product-like | Functional/utilitarian |

## Relationships

- [[nous-research]] — Developer
- [[jeff-quesnelle]] — Co-founder of Nous Research
- [[teknium]] — Co-founder & Head of Post-Training
- [[openclaw]] — Competing agent harness

## Appears In

- [[hermes-agent-website]] — Official product page
- [[networkchuck-hermes-agent]] — Video review by NetworkChuck
- [[skills-sh-directory]] — Nous Research listed as a supported agent

## Agent Notes

- One of the fastest-growing GitHub projects at the time of review; topped OpenClaw on OpenRouter token usage.
- The "get out of the model's way" philosophy is central: the harness provides hands and fingers, the model is the brain.
