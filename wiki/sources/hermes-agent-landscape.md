---
title: Hermes Agent — GitHub Repository and Landscape
created: 2026-05-25
updated: 2026-05-25
category: source
tags: [github, ai-agent, hermes, open-source, nous-research, data]
author: Nous Research
publisher: GitHub
url: https://github.com/nousresearch/hermes-agent
status: active
---

# Hermes Agent — GitHub Repository and Landscape

**Organization:** Nous Research  
**GitHub:** [github.com/nousresearch/hermes-agent](https://github.com/nousresearch/hermes-agent)  
**Website:** [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/)  
**License:** MIT  
**Data fetched:** 2026-05-25

## TL;DR

Hermes is the most popular open-source AI agent on GitHub with 166k stars and 27.4k forks. It is an autonomous agent that runs on your server, learns from interactions, generates its own skills, and connects to multiple messaging platforms. Built by Nous Research, it emphasizes lightweight reliability, curated memory, and getting out of the model's way.

## Key Metrics

- **166k GitHub stars** — Making it the most starred AI agent project
- **27.4k forks**
- **1,190 contributors**
- **9,464 commits** as of May 2026
- **Latest release:** v0.14.0 (2026-05-16)
- **License:** MIT (open source)

## Features (from official website and GitHub)

### Multi-Platform
Lives where you do: Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI, and growing.

### Persistent Memory & Self-Improving Skills
- Auto-generates skills from interactions
- Never forgets how it solved a problem
- Procedural memory system

### Scheduled Automations
Natural language cron scheduling for reports, backups, and briefings running unattended.

### Delegation & Parallelization
- Isolated subagents with their own conversations
- Python RPC scripts for zero-context-cost pipelines
- Parallel task execution

### Sandboxing
Five backends: local, Docker, SSH, Singularity, Modal — with container hardening and namespace isolation.

### Full Web & Browser Control
Web search, browser automation, vision, image generation, text-to-speech, and multi-model reasoning.

### Built-in OpenClaw Migration
- `hermes claw migrate` — auto-detects and imports settings, memories, skills, and API keys from OpenClaw
- `--dry-run` preview mode
- Supports selective migration (user-data only, skip secrets, etc.)

### MCP Integration
Connect any MCP (Model Context Protocol) server for extended capabilities.

### Context Files
Project context shapes every conversation across sessions.

## Architecture Highlights (from code)

- **Python 88.7%** / TypeScript 8.4% — Python-first with web dashboard in TS
- **Plugin-based platform adapters** — Modular architecture for Telegram, Discord, Slack, Mattermost, IRC, LINE, Google Chat, SimpleX, ntfy
- **S6 supervision** — Container lifecycle management with proper unprivileged user support
- **Kanban system** — Task board for agent workflows
- **Dashboard** — Web UI for skills, plugins, agent profiles, auxiliary models

## Comparison to OpenClaw

| Feature | Hermes | OpenClaw |
|---------|--------|---------|
| GitHub stars | 166k | Unknown but less |
| Memory | Hard-capped, auto-curated | Auto-growing, bloat risk |
| Skills | Self-generated | Marketplace/download |
| Migration | Built-in from OpenClaw | N/A |
| Platforms | Telegram, Discord, Slack, etc. | Wider platform support |
| Sandboxing | 5 backends (Docker, SSH, etc.) | Standard containerization |
| Philosophy | Opinionated, get out of the way | Configurable, everything |
| Stability | Reported more reliable | Degrades over time |

## Release History

- v2026.5.16 (v0.14.0) — Latest as of May 2026
- v0.13.0 — Major release with skills hub and expanded platform support
- Earlier releases tracked on GitHub

## Who Is It For?

| Profile | Hermes Fit |
|---------|-----------|
| Homelabbers | Excellent — self-hosted, lightweight, fun vibe |
| IT admins | Strong — NetworkChuck's Ron Weasley example is emblematic |
| Developers | Good — Python codebase, plugin architecture, CLI-first |
| Enterprise | Possibly via Docker/Modal backends; less enterprise-focused than Kore.ai or Sierra |
| Casual users | Good via Telegram bot; easy setup on $5 VPS |

## Is Hermes *Useful*?

**Yes, with caveats:**

1. **For personal/IT use** — Very useful. The persistent memory, self-improving skills, and multi-platform reach make it genuinely better over time. NetworkChuck's month-long real-world test is the strongest endorsement.

2. **For developers** — Useful as a reference implementation. The plugin architecture, S6 lifecycle management, and migration tooling are well-engineered. Studying the codebase teaches good patterns.

3. **For enterprises** — Less proven. While it has Docker/Modal backends and security features, enterprise buyers typically prefer backed vendors (Kore.ai, Moveworks, Sierra) with SLAs and compliance certifications.

4. **For experimentation** — Extremely useful. The open-source MIT license, lightweight install, and OpenClaw migration path lower the barrier to trying something new.

5. **Relative to OpenClaw** — Subjectively better for users who value stability and curation over raw configurability. The hard memory cap, skill generation, and reliability reports are meaningful differentiators.

## Limitations

- **Young ecosystem** — Smaller plugin marketplace than OpenClaw
- **Niche audience** — Leans toward technical users; less no-code than Lindy or CrewAI
- **Self-hosted burden** — Requires managing your own server/VPS unless using Modal
- **Documentation** — Improving but not as comprehensive as commercial platforms

## Ecosystem

- **Skills Hub:** [agentskills.io](https://agentskills.io/)
- **Community WeChat bridge:** HermesClaw (run both on same WeChat account)
- **Linux desktop MCP:** [computer-use-linux](https://github.com/avifenesh/computer-use-linux)

## Connections to Wiki

- [[networkchuck-hermes-agent]] — Practical review and install tutorial
- [[nous-research]] — Organization behind Hermes
- [[ai-agent-harness]] — Concept page on harness architecture
- [[persistent-memory]] — Hermes's curated memory approach
- [[openclaw]] — Primary comparison point

## Agent Notes

- The 166k stars metric is remarkable for a project that started as an internal Discord tool.
- The built-in OpenClaw migration is a savvy competitive move that reduces switching friction.
- The S6 container lifecycle work (visible in recent commits) shows real systems engineering depth.
- Watch for enterprise features in upcoming releases — the Modal/Docker backends suggest that direction.
