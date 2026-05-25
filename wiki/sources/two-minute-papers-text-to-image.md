---
title: "Two Minute Papers: Text-to-Image Generation (Stable Diffusion, DALL-E, Imagen)"
url: "https://www.youtube.com/@TwoMinutePapers"
category: source
tags: [stable-diffusion, dall-e, text-to-image, diffusion-models, generative-ai, computer-vision, video, two-minute-papers]
author: Károly Zsolnai-Fehér
publisher: YouTube
speaker: Károly Zsolnai-Fehér
created: 2026-05-25
updated: 2026-05-25
---

# Two Minute Papers: Text-to-Image Generation

## Source Details

- **URL:** Multiple videos on the [Two Minute Papers channel](https://www.youtube.com/@TwoMinutePapers)
- **Channel:** [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers)
- **Presenter:** [[karoly-zsolnai-feher]]
- **Published:** 2021–2024 (multiple episodes)
- **Duration:** ~2 minutes per paper
- **Status:** Series of summaries tracking the text-to-image breakthrough era

## Summary

A collection of Two Minute Papers episodes covering the rapid evolution of text-to-image generation, from DALL-E (2021) to DALL-E 2, Stable Diffusion, Midjourney, and Imagen. Zsolnai-Fehér explains the core mechanism — diffusion models that progressively denoise random latent noise into coherent images conditioned on text embeddings — and demonstrates the rapidly improving visual quality across papers and systems.

## Key Claims

- **Diffusion models beat GANs for text-to-image** — by 2022, diffusion-based approaches (DALL-E 2, Stable Diffusion) produced higher quality, more diverse, and more controllable outputs than GAN-based predecessors.
- **Text encoding matters as much as image generation** — CLIP embeddings (from OpenAI) enable the text-image alignment that makes prompt-conditioned generation work.
- **Latent diffusion is the efficiency breakthrough** — Stable Diffusion operates in a compressed latent space rather than full pixel space, making it feasible to run on consumer GPUs.
- **Guidance scale controls fidelity vs. diversity** — higher classifier-free guidance produces outputs that more closely match the prompt but look less natural.
- **The progression was shockingly fast** — from blurry 256px DALL-E outputs in 2021 to photorealistic 1024px images from Midjourney and DALL-E 3 by 2023.

## Notable Papers Covered

- **DALL-E** (2021) — GPT-style transformer generating images from text, 256x256 resolution.
- **DALL-E 2** (2022) — Diffusion model with CLIP embeddings, much higher quality and resolution.
- **Stable Diffusion** (2022) — Latent diffusion model that runs efficiently on consumer hardware; open-sourced by Stability AI.
- **Imagen** (2022) — Google's text-to-image model using frozen LLM text encoders and cascaded diffusion.
- **Midjourney** — Not a paper but a product; Two Minute Papers covered its capabilities as they evolved.

## Entities Mentioned

- [[karoly-zsolnai-feher]] — Presenter, Two Minute Papers
- OpenAI — DALL-E, DALL-E 2, CLIP
- Stability AI — Stable Diffusion
- Google Research — Imagen

## Concepts Discussed

- [[diffusion-models]] — Generative models that learn to reverse a noise-corruption process
- [[text-to-image]] — Generating images from natural language descriptions
- [[classifier-free-guidance]] — Controlling prompt adherence vs. output diversity in diffusion models
- [[latent-space]] — Compressed representation space where diffusion operates efficiently

## Connections to Other Sources

- [[andrej-karpathy-channel]] — Karpathy's nanoGPT and LLM work underlie the text understanding in text-to-image systems.
- [[3blue1brown-channel]] — 3Blue1Brown has visualized diffusion and CLIP concepts.

## Source References

- [Two Minute Papers: Stable Diffusion](https://www.youtube.com/watch?v=4LZJ9ws4P3E) — One representative episode
- [Two Minute Papers channel](https://www.youtube.com/@TwoMinutePapers) — Full collection of text-to-image episodes
