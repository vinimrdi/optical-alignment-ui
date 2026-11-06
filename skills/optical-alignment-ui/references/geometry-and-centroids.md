# Geometry and centroids

## Why this file exists

**Centroid is a diagnostic geometry tool**, not guaranteed perceptual center. Stroke, contrast, background, size, and neighbors still matter.

## Four centers

| Center | Represents | Typical use |
|--------|------------|-------------|
| **Bounding-box center** | Center of axis-aligned container rect | Layout, flex/grid |
| **Geometric centroid** | Center of mass of filled area (uniform density) | Simple filled polygons |
| **Alpha-weighted centroid** | Opacity-weighted center | Raster, soft edges, AA SVG renders |
| **Perceptual center** | Where the composition *looks* balanced | Final judgment |

Uniform filled region *A*:

\[
C_x = \frac{\iint_A x\,dA}{A}, \quad
C_y = \frac{\iint_A y\,dA}{A}
\]

Discrete opacity weights αᵢ:

\[
C_x = \frac{\sum_i x_i \alpha_i}{\sum_i \alpha_i}, \quad
C_y = \frac{\sum_i y_i \alpha_i}{\sum_i \alpha_i}
\]

## Tooling in this repo

| Script | Input | Notes |
|--------|--------|--------|
| [`scripts/centroid.py`](../../../scripts/centroid.py) | PNG/WebP + alpha | Direct raster analysis |
| [`scripts/svg_centroid.py`](../../../scripts/svg_centroid.py) | SVG | Rasterizes at `--size` (UI px), then same metrics + `viewBox` |

```bash
pip install pillow cairosvg
python scripts/svg_centroid.py icon.svg --size 24 --verbose
python scripts/svg_centroid.py icon.svg --size 48 --json
python scripts/svg_centroid.py icon.svg --size 24 --write-png /tmp/icon-24.png
```

SVG is measured **as rendered at target size** (strokes, AA, transforms included)—more faithful for UI icons than path math alone. See [`scripts/README.md`](../../../scripts/README.md).

## Decision matrix

| Situation | Prefer |
|-----------|--------|
| Axis-symmetric filled rect | Bounding box |
| Equilateral play in circle | Centroid as check; eye; pad-in-asset |
| Outline-only icon | Not fill centroid alone; raster helps |
| PNG with transparency | `centroid.py` |
| SVG icons | `svg_centroid.py --size <ui-px>` |
| Wrong or loose viewBox | **Fix metadata before optical nudge** |
| Mixed SVG libraries | Per-file measure + keylines |

## Circle vs square — name the intent

| Intent | Meaning | Aid |
|--------|---------|-----|
| **Equal area** | Same filled area | \( d = s\sqrt{4/\pi} \approx 1.1284\,s \) |
| **Equal visual size** | Similar apparent size | Judge at size |
| **Equal visual weight** | Mass incl. stroke/contrast | No single formula |
| **Equal frame occupancy** | Keyline live area | Material-style keylines |
| **Equal prominence** | Attention in context | Contextual |

## SVG inspection checklist

| Field | Why |
|-------|-----|
| `viewBox` | Maps path space to layout box |
| width / height attrs | Presentation size |
| stroke / transforms | Mass and position |
| Ink vs empty padding | True optical box |

`svg_centroid.py` surfaces viewBox + `likely_viewbox_or_padding_issue` when offset vs canvas is large.

## Limits

No universal pixel offset. Geometric equality ≠ perceptual equality. `cairosvg` must be installed for SVG rasterization.
