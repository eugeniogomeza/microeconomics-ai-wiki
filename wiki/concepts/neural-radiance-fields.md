---
title: Neural Radiance Fields
created: 2026-05-25
updated: 2026-05-25
category: concept
tags: [computer-vision, 3d-reconstruction, neural-networks, neural-rendering, implicit-representations]
status: active
---

# Neural Radiance Fields

**AKA:** NeRF, neural scene representation  
**Related:** [[implicit-representations]], [[volume-rendering]], [[computer-vision]], [[neural-networks]]

## TL;DR

NeRF is a method for representing 3D scenes as continuous neural functions rather than explicit meshes or voxel grids. A neural network maps a 5D coordinate (3D spatial position + 2D viewing direction) to color and density. Given a handful of 2D images of a scene, NeRF can render photorealistic novel views from any camera angle. It sparked a revolution in neural rendering and implicit 3D representations.

## Explanation

Traditional 3D representations use meshes, point clouds, or voxel grids — discrete data structures that scale poorly. NeRF instead encodes the scene in the weights of a fully connected neural network.

The process:
1. For each pixel in a target view, cast a ray through the scene.
2. Sample points along that ray.
3. For each point, query the NeRF network: input (x, y, z, θ, φ) → output (R, G, B, density).
4. Composite colors and densities along the ray using classical volume rendering to produce the final pixel color.
5. Minimize the difference between rendered pixels and ground-truth images.

Key innovations:
- **Positional encoding** — maps low-dimensional coordinates into high-frequency Fourier features, allowing the MLP to represent fine geometric detail.
- **View-dependent color** — the network outputs different colors for the same 3D point depending on viewing angle, enabling specular reflections and view-dependent effects.

## Sources

- [[two-minute-papers-nerf]] — 2-minute summary of the original paper
- [[3blue1brown-channel]] — Linear algebra and neural network foundations underlying NeRF

## Connections

- [[neural-networks]] — NeRF is an MLP; the scene is encoded in its weights.
- [[volume-rendering]] — The classical graphics technique that composites NeRF's density/color predictions into images.
- [[implicit-representations]] — NeRF is the flagship example of representing geometry implicitly via neural networks.

## Open Questions

- Can NeRF replace traditional 3D pipelines for film, games, and VR?
- How do we scale NeRF to large, dynamic, or outdoor scenes?
- Will 3D Gaussian splatting or other explicit representations overtake NeRF?
