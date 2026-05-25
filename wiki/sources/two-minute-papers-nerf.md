---
title: "Two Minute Papers: Neural Radiance Fields (NeRF)"
url: "https://www.youtube.com/watch?v=JuH79a8wO-0"
category: source
tags: [nerf, computer-vision, 3d-reconstruction, neural-networks, neural-rendering, video, two-minute-papers]
author: Károly Zsolnai-Fehér
publisher: YouTube
speaker: Károly Zsolnai-Fehér
created: 2026-05-25
updated: 2026-05-25
---

# Two Minute Papers: Neural Radiance Fields (NeRF)

## Source Details

- **URL:** [https://www.youtube.com/watch?v=JuH79a8wO-0](https://www.youtube.com/watch?v=JuH79a8wO-0)
- **Channel:** [Two Minute Papers](https://www.youtube.com/@TwoMinutePapers)
- **Presenter:** [[karoly-zsolnai-feher]]
- **Published:** 2020
- **Duration:** ~2 minutes
- **Views:** 1M+
- **Status:** Summarizes the foundational NeRF paper

## Summary

Zsolnai-Fehér summarizes the Mildenhall et al. (2020) paper "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis." The key innovation: instead of storing a 3D scene as a mesh or voxel grid, NeRF represents it as a continuous function — a neural network that maps a 5D coordinate (3D position + 2D viewing direction) to color and density. Given a handful of 2D images, the network learns to render photorealistic novel views from any angle.

## Key Claims

- **NeRF replaces explicit 3D representations with implicit neural ones** — a scene is encoded in the weights of a neural network, not in a mesh or point cloud.
- **5D input coordinate** — (x, y, z, θ, φ): spatial position plus viewing direction. This enables view-dependent effects like specular reflections.
- **Volume rendering integral** — the network predicts density (-opacity) and RGB color at each point along a ray; ray marching composites these into a final pixel.
- **Positional encoding is critical** — mapping coordinates into higher-dimensional Fourier features allows the MLP to learn high-frequency detail.
- **Photorealistic results from sparse views** — NeRF produces results that rival photogrammetry methods but from far fewer images.

## Entities Mentioned

- [[karoly-zsolnai-feher]] — Presenter, Two Minute Papers

## Concepts Discussed

- [[neural-radiance-fields]] — Representing 3D scenes as neural functions
- [[volume-rendering]] — Accumulating color along viewing rays through a medium
- [[implicit-representation]] — Encoding geometry/function in neural network weights rather than explicit data structures
- [[positional-encoding]] — Mapping low-dimensional inputs to higher frequencies to help MLPs learn fine detail

## Source References

- [Two Minute Papers: NeRF](https://www.youtube.com/watch?v=JuH79a8wO-0) — Summary video
- Original paper: Mildenhall et al., "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis" (ECCV 2020)
