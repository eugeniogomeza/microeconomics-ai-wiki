---
title: Factory.ai — Agent-Native Software Development
created: 2026-05-26
updated: 2026-05-26
category: source
tags: [ai-agent, enterprise, devtool, platform, droid]
author: Factory
publisher: Factory
url: https://factory.ai/
status: active
---

# Factory.ai — Agent-Native Software Development

**Author:** [[factory]]
**Published:** 2026 (ongoing)
**URL:** [https://factory.ai/](https://factory.ai/)
**CLI Install:** `curl -fsSL https://app.factory.ai/cli | sh`

## TL;DR

Factory is an enterprise agent-native software development platform powered by "Droid." It provides a CLI, Desktop, Web/Mobile, Slack, and Jira/Linear integrations. Factory's key differentiator is cost optimization: it claims to be the only platform incentivized to reduce token spend rather than grow consumption. Features include Agent Readiness scoring, Mission Control for orchestrating fleets of agents, and Droid Computers for persistent remote agent machines.

## Key Claims

1. **Agent-Native Platform** — Droid ships from desktop, browser, mobile, terminal, and CI pipeline.
2. **Cost Intelligence** — Factory Analytics breaks down consumption by model and by engineer to find inefficiencies.
3. **Agent Readiness** — Evaluates every repository across 100+ signals (docs, tests, CI health, modularity, dependencies) and prescribes fixes.
4. **Mission Control** — Orchestrates fleets of parallel Droids for complex, multi-day autonomous work.
5. **Droid Computers** — Persistent cloud machines that keep state across sessions.
6. **Model Agnostic** — Routes each step to the right model for speed, cost, and reliability.
7. **Enterprise-Ready** — SAML/IDP, air-gapped deployment, OTEL native, per-team cost controls.

## Trusted Customers

- Groq, Adyen, Chainguard, Podium (and others)

## Use Cases

- Triage customer signals from support tickets, Slack, CRM
- Ticket-to-code: auto-pickup and implement backlog tickets
- Code review: every PR reviewed in minutes
- QA: continuous test generation and regression catching
- Incident response: AI-powered root cause analysis reducing MTTR
- Documentation: self-writing docs that never go stale

## Recent News

- **Deferred Context Engine** — Keeps tool schemas reachable without loading everything every turn, saving input tokens.
- **Which Model Reviews Code Best?** — Benchmarked 13 models for code-review price-performance.
- **Automated QA** — End-to-end visual QA with evidence posted directly to PRs.
- **Factory raises $150M Series C** (Mar 2026) at $1.5B valuation from Khosla, Sequoia, Blackstone, Insight, Evantic, 20VC, NEA, Mantis VC.

## Entities Mentioned

- [[factory]] — Company behind Droid and the Factory platform
- [[groq]] — Customer and partner (fast inference)
- [[chainguard]] — Customer; Josh Wolf praised Droid's two-week session persistence
- [[anthropic]] — Model provider (Claude family)
- [[openai]] — Model provider (GPT family)

## Concepts Discussed

- [[ai-agent-harness]] — Enterprise-grade agent orchestration
- [[agent-readiness]] — Repository evaluation scoring for autonomous development
- [[cost-optimization]] — Reducing LLM token spend via analytics and routing
- [[mission-control]] — UI for orchestrating parallel agent fleets

## Connections to Other Sources

- [[anthropic-learn]] — Complements with Claude training and API development
- [[hermes-agent-website]] — Both in the agent harness space; Factory targets enterprise teams, Hermes targets individual power users

## Agent Notes

- Factory's Series C at $1.5B valuation signals serious market validation for enterprise agent-native development.
- The "Agent Readiness" concept is novel: treating codebase health as a prerequisite for autonomous agents, analogous to "road quality" before deploying self-driving cars.
- Deferred Context Engine is a production optimization worth tracking for other agent frameworks.
