---
title: Kubernetes
created: 2026-05-26
updated: 2026-05-26
category: entity
tags: [product, platform, container-orchestration, cloud-native, cncf]
status: active
---

# Kubernetes

**Type:** Product / Open-Source Platform
**Also known as:** K8s
**URL:** [https://kubernetes.io/](https://kubernetes.io/)
**Maintainer:** Cloud Native Computing Foundation (CNCF), graduated project

## TL;DR

Kubernetes is the dominant open-source platform for automating deployment, scaling, and management of containerized applications. Built on 15+ years of Google production experience, it is now a graduated CNCF project and the unchallenged standard for container orchestration at scale.

## Core Capabilities

- **Automated Deployment** — Declarative desired-state configuration
- **Auto-Scaling** — Horizontal pod autoscaling
- **Self-Healing** — Restarts, replicates, and reschedules failed containers
- **Service Discovery & Load Balancing** — Built-in DNS and traffic distribution
- **Storage Orchestration** — Automatic mounting of local, cloud, or network storage
- **Runs Anywhere** — On-premises, hybrid, public cloud; workload portability

## Ecosystem Stats

- Graduate project of [[cncf]]
- Used by enterprises worldwide including Financial Times (150+ microservices migrated)
- Native support for Helm charts (including Docker Hardened Images)

## Relationships

- [[docker]] — Kubernetes orchestrates Docker containers
- [[cncf]] — Parent foundation
- [[google]] — Original creator and major contributor
- [[factory]] — Factory deploys on Kubernetes with Helm charts
- [[hermes-agent]] — Can be deployed on Kubernetes clusters for scaling

## Appears In

- [[kubernetes-website]] — Official Spanish-language site
- [[docker-website]] — Docker images consumed by Kubernetes
- [[factory-ai-website]] — Factory uses Kubernetes for agent workload orchestration

## Agent Notes

- No meaningful competitor has displaced Kubernetes for container orchestration.
- The combination of Docker + Kubernetes + MCP (via Docker) + agent frameworks (Hermes/Factory) forms a modern AI infrastructure stack.
- Spanish-language site ingestion reflects global/multilingual tech resource coverage.
