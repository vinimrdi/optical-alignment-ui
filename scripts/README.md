# Scripts — Optical Alignment UI

Diagnostic tools. **Centroid output is not perceptual truth** — use it with native-size judgment per the skill.

## `centroid.py`

Compute **bounding-box center**, **alpha-weighted centroid**, and **ink bounding box** from a raster image (PNG/WebP/GIF with alpha preferred).

### Requirements

```bash
pip install pillow
```

### Usage

```bash
# From repo root
python scripts/centroid.py path/to/icon.png

# Custom alpha threshold (default: 1 = any non-zero alpha)
python scripts/centroid.py icon.png --threshold 8

# JSON only (for agents / CI)
python scripts/centroid.py icon.png --json

# Compare against geometric center of full canvas
python scripts/centroid.py icon.png --verbose
```

### How to use results

| Output | Meaning |
|--------|---------|
| `canvas_center` | Center of the full image rectangle |
| `ink_bbox_center` | Center of the axis-aligned box of opaque pixels |
| `alpha_centroid` | Opacity-weighted center of mass |
| `offset_from_canvas` | `alpha_centroid - canvas_center` (px) |
| `offset_from_ink_bbox` | `alpha_centroid - ink_bbox_center` (px) |

**Interpretation tips**

- Large `offset_from_canvas` with ink huddled in one corner → often a **viewBox / export padding** issue, not pure optical weight.
- `offset_from_ink_bbox` near zero but the icon still *looks* off in UI → perception/context; do not trust the number alone.
- For filled play triangles, non-zero offset from ink bbox center is expected; use as a **check**, then pad-in-asset and judge at UI size.

### Not supported (yet)

- Live SVG path geometry without rasterization (export PNG at target size first).
- True perceptual models (contrast, neighbors).

Export the glyph at **target UI size** (e.g. 24×24 or 48×48) on a transparent background for the most relevant numbers.
