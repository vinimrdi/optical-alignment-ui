# Geometry and centroids

## Why this file exists

Agents often treat “center the centroid” as optical truth. **Centroid is a diagnostic geometry tool.** Perceptual center still depends on stroke, contrast, background, size, and neighbors.

## Four centers (distinguish them)

| Center | Represents | Typical use |
|--------|------------|-------------|
| **Bounding-box center** | Center of the axis-aligned rect that contains the object | Layout systems, flex/grid centering |
| **Geometric centroid** | Center of mass of filled area (uniform density) | Simple filled polygons |
| **Alpha-weighted centroid** | Center weighted by opacity samples | Raster icons, soft edges, anti-aliased SVG renders |
| **Perceptual center** | Where the composition *looks* balanced | Final judgment after geometry aids |

For uniform filled region *A*:

\[
C_x = \frac{\iint_A x\,dA}{A}, \quad
C_y = \frac{\iint_A y\,dA}{A}
\]

For discrete opacity weights αᵢ:

\[
C_x = \frac{\sum_i x_i \alpha_i}{\sum_i \alpha_i}, \quad
C_y = \frac{\sum_i y_i \alpha_i}{\sum_i \alpha_i}
\]

These estimate **mass centers**, not guaranteed perceptual centers.

## Decision matrix

| Situation | Prefer |
|-----------|--------|
| Axis-symmetric filled rect | Bounding box |
| Equilateral play triangle in a circle | Geometric centroid as check; verify by eye; pad-in-asset preferred for hand-off |
| Outline-only icon | Do not use fill centroid alone; judge stroke mass and negative space |
| Mixed stroke weights | Perceptual assessment primary |
| PNG/WebP with transparency | Alpha-weighted bounds if tooling allows |
| Different libraries’ SVGs in one set | Inspect each `viewBox` and real ink bounds |

## Circle vs square scaling — name the intent

Equal **bounding box** does not imply equal perception.

| Intent | Meaning | Aid |
|--------|---------|-----|
| **Equal area** | Same filled area | \( d = s\sqrt{4/\pi} \approx 1.1284\,s \) |
| **Equal visual size** | Similar apparent size | Often less than full area factor; judge at target size |
| **Equal visual weight** | Similar mass including stroke/contrast | No single formula |
| **Equal frame occupancy** | Similar live area in a keyline system | Material-style keylines |
| **Equal prominence** | Similar attention in context | Contextual; not pure geometry |

**Do not** apply +12.8% to every circle by default. State the intent. Snap to pixels when crispness matters.

## SVG inspection checklist

When available, inspect:

- `viewBox`, width, height
- `stroke-width`, `stroke-linecap`, `stroke-linejoin`
- Transforms on groups/paths
- Real ink bounds vs empty padding
- Transparency / empty regions

Mis-set `viewBox` is a common cause of “optical” bugs that are actually asset bugs—fix the asset metadata first.

## Stroke geometry and negative space

- Outline icons distribute mass differently from filled icons at the same outer size.
- Internal counters and external negative space change perceived size.
- Keylines define **visual occupancy**, not an invariant scale law.

## Platform notes (attribution discipline)

- **Material Design** icon guidance: keyline grids and live areas by shape family—use for set consistency.
- **Apple HIG**: guidance on icons and composition varies by surface (e.g. app icons vs interface icons). Only attribute a specific recommendation to Apple when the cited HIG page supports that claim. Prefer describing the **pad-in-asset** pattern as a durable engineering practice aligned with optical centering, not as a blanket Apple mandate if the exact page is not verified in-session.

## Limits

- No universal pixel offset.
- Geometric equality ≠ perceptual equality.
- Automation helps; native-size judgment closes the loop.
