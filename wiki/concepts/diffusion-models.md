---
title: Diffusion Models
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [generative-ai, computer-vision, deep-learning, text-to-image, generative-models]
status: active
---

# Diffusion Models

**AKA:** denoising diffusion probabilistic models (DDPM), score-based generative models  
**Related:** [[text-to-image]], [[generative-ai]], [[neural-networks]], [[stable-diffusion]]

## TL;DR

Diffusion models are generative models that learn to reverse a gradual noise-corruption process. During training, noise is progressively added to images until they become pure noise; a neural network learns to predict and remove that noise. At inference, the model starts from random noise and iteratively denoises it into a coherent image, guided by text embeddings or other conditioning. They are the engine behind modern text-to-image systems like DALL-E, Stable Diffusion, and Midjourney.

## Explanation

Forward process (fixed): progressively add Gaussian noise to an image over T timesteps.

Reverse process (learned): train a neural network to predict the noise at each step, then subtract it to recover the original image.

Training objective: minimize the mean squared error between predicted noise and actual noise.

Inference: start from pure noise, repeatedly apply the learned denoising network, optionally conditioned on a text prompt via cross-attention.

Key variants:
- **DDPM** (Ho et al., 2020) — The foundational formulation.
- **Latent Diffusion (Stable Diffusion)** — Operates in a compressed latent space rather than pixel space, enabling fast generation on consumer GPUs.
- **Classifier-Free Guidance** — A technique to make outputs more closely match the prompt (higher guidance = higher prompt adherence but less diversity).

## Sources

- [[two-minute-papers-text-to-image]] — Evolution of text-to-image generation via diffusion

## Connections

- [[text-to-image]] — Diffusion models are the dominant approach for generating images from text.
- [[neural-networks]] — The denoising network is typically a U-Net with attention layers.
- [[language-models]] — Text encoders (e.g., CLIP) provide the conditioning signal for text-to-image generation.

## Open Questions

- Can diffusion models be accelerated to real-time generation for video and interactive applications?
- Will diffusion be superseded by faster generative approaches (e.g., consistency models, flow matching)?
