---
title: Honcho (Plastic Labs)
created: 2026-05-25
updated: 2026-05-25
category: entity
tags: [product, memory, ai-agent, personalization]
status: active
---

# Honcho (Plastic Labs)

**Type:** Product / Service  
**Developer:** Plastic Labs  
**URL:** [honcho.dev](https://honcho.dev/)  
**Related:** [[hermes-agent]], [[persistent-memory]], [[nous-research]]

## TL;DR

Honcho is a peer memory service that integrates with AI agents (especially Hermes) to build rich, long-term user profiles called "peer cards." It reasons over conversation history to infer personality traits, preferences, and habits, then injects the most relevant context into the agent's system prompt in real time.

## How It Works

1. Receives every user message sent to the agent
2. Builds a dynamic "peer card" — a structured profile of the user
3. When the agent needs to respond, Honcho selects the most relevant peer-card insights
4. Injects those insights into the system prompt so the agent has personalized context

## Appears In

- [[networkchuck-hermes-agent]] — NetworkChuck demonstrates Honcho integration with his agent James.

## Connections

- [[persistent-memory]] — Honcho is a specific implementation of long-term agent memory.
- [[nous-research]] — Hermes has first-class integration with Honcho.

## Agent Notes

- Example insight generated: "high friction, technical procrastination gravitates towards tool building wiring to avoid high stakes communication or soul work."
- Can also be plugged into OpenClaw, though integration is less seamless.
