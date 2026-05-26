---
title: Docker — Accelerated Container Application Development
created: 2026-05-26
updated: 2026-05-26
category: source
tags: [devops, container, security, mcp, platform]
author: Docker Inc.
publisher: Docker Inc.
url: https://www.docker.com/
status: active
---

# Docker — Accelerated Container Application Development

**Author:** [[docker]]
**Published:** 2026 (ongoing)
**URL:** [https://www.docker.com/](https://www.docker.com/)

## TL;DR

Docker is the dominant container platform for building, shipping, and running applications. In 2026, Docker has expanded aggressively into AI/Agent infrastructure: free hardened images (Apache 2.0), Docker MCP (200+ verified MCP servers containerized), and agentic-stack orchestration via Docker Compose. The platform serves 24M+ users with 14M+ images and 11B+ monthly downloads.

## Key Claims

1. **Docker Hardened Images (DHI)** — Now free and Apache 2.0 licensed. Near-zero CVE images with complete SBOMs and SLSA Level 3 provenance.
2. **Docker MCP** — 200+ verified MCP servers (Stripe, Notion, GitHub, Browserbase, etc.) run as signed, isolated containers with Rug Pull and Tool Poisoning protection.
3. **Agentic Stack Orchestration** — Define and run agents, models, and tools with Docker Compose in a single file.
4. **Enterprise Security** — SAML/IDP, air-gapped deployment, OTEL native, per-team cost controls, centralized org config.
5. **Extended Lifecycle Support** — Multi-year CVE patches for EOL images.

## Ecosystem Stats

- 14M+ images on Docker Hub
- 11B+ monthly downloads
- 24M+ users
- 200+ verified MCP servers
- 1000+ hardened images and Helm charts

## Security Pillars

- Minimal / distroless images (97% attack-surface reduction)
- Signed provenance
- Complete SBOMs
- VEX insights
- Transparent verification

## Entities Mentioned

- [[docker]] — The company and platform
- [[github]] — Partner (MCP servers, sponsorship)
- [[nvidia]] — GPU-related container images and partnerships
- [[cloudflare]] — Testimonial from senior engineer on Docker's utility
- [[adobe]] — Testimonial on hardened images alignment with security posture

## Concepts Discussed

- [[containerization]] — OS-level virtualization for application deployment
- [[mcp-server]] — Model Context Protocol servers packaged as containers
- [[supply-chain-security]] — SBOMs, SLSA, signed builds, and CVE management
- [[hardened-images]] — Minimal, continuously rebuilt security-focused base images

## Connections to Other Sources

- [[hermes-agent-website]] — Hermes supports Docker as a sandboxing backend
- [[skills-sh-directory]] — Docker skills exist in the skills ecosystem
- [[kubernetes-website]] — Kubernetes is the standard container orchestrator that consumes Docker images

## Agent Notes

- Docker's pivot into MCP and agent orchestration is significant: it positions containers as the default packaging format for AI tools, not just traditional applications.
- The "Rug Pull" and "Tool Poisoning" protections for MCP servers suggest Docker sees agent security as a major emerging concern.
- Hardened images being free (Apache 2.0) is a competitive response to Chainguard and other security-focused image providers.
