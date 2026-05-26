---
title: Hermes Agent Website — The Agent That Grows With You
created: 2026-05-26
updated: 2026-05-26
category: source
tags: [ai-agent, open-source, tool, nous-research]
author: Nous Research
publisher: Nous Research
url: https://hermes-agent.nousresearch.com/
status: active
---

# Hermes Agent Website — The Agent That Grows With You

**Author:** [[nous-research]]
**Published:** 2026 (ongoing)
**URL:** [https://hermes-agent.nousresearch.com/](https://hermes-agent.nousresearch.com/)
**License:** Open Source / MIT

## TL;DR

Hermes Agent is an autonomous, self-improving AI agent harness from Nous Research. Unlike IDE-tethered copilots or single-API chatbots, it runs persistently on a server, learns from interactions, auto-generates skills, and supports multi-platform communication (Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI).

## Key Claims

1. **Persistent Memory** — Remembers projects and past solutions across sessions; auto-curates skills as it learns.
2. **Multi-Platform** — Runs on Telegram, Discord, Slack, WhatsApp, Signal, Email, and CLI with a growing list of integrations.
3. **Sandboxing** — Five isolation backends: local, Docker, SSH, Singularity, and Modal, with container hardening.
4. **Subagent Delegation** — Spawns isolated subagents with independent conversations, terminals, and Python RPC scripts for parallel pipelines.
5. **Scheduled Automations** — Natural-language cron scheduling for reports, backups, and briefings.
6. **Full Browser & Web Control** — Web search, browser automation, vision, image generation, text-to-speech, and multi-model reasoning built in.

## Installation & Setup

- One-liner install: `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- Initial setup: `hermes setup`

## Entities Mentioned

- [[nous-research]] — Developer of Hermes Agent and Hermes LLM family
- [[jeff-quesnelle]] — Co-founder of Nous Research
- [[teknium]] — Co-founder & Head of Post-Training
- [[openclaw]] — Contrasting agent harness referenced in the landscape

## Concepts Discussed

- [[ai-agent-harness]] — Infrastructure layer for autonomous agents
- [[persistent-memory]] — Memory architecture that persists and auto-curates over time
- [[sandboxing]] — Isolated execution environments for agent operations
- [[subagent-delegation]] — Spawning helper agents for parallel task execution

## Connections to Other Sources

- [[networkchuck-hermes-agent]] — Video review and installation walkthrough
- [[openclaw]] — Competing agent harness; Hermes positioned as lighter and more stable

## Agent Notes

- The website emphasizes "grows with you" as a core differentiator — persistent learning and skill crystallization.
- The product positioning (not IDE-tethered, not single-API wrapper) directly targets the gap between coding copilots and consumer chatbots.
- The five sandboxing backends and container hardening suggest serious attention to security for autonomous execution.
