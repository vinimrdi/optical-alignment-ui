# Scripts — Optical Alignment UI

Diagnostic tools. **Centroid output is not perceptual truth** — use with native-size judgment per the skill.

## `centroid.py` (raster PNG / WebP)

Alpha-weighted centroid + ink bbox from an image with transparency.

```bash
pip install pillow
python scripts/centroid.py icon.png --verbose
python scripts/centroid.py icon.png --json --threshold 8
```

## `svg_centroid.py` (SVG → raster at UI size → same metrics)

Renders the SVG into a square pixel grid (default 24×24) with **cairosvg**, then runs the same analysis as `centroid.py`. Also reports `viewBox` when present.

```bash
pip install pillow cairosvg

# Typical icon sizes
python scripts/svg_centroid.py icons/play.svg --size 24 -v
python scripts/svg_centroid.py icons/play.svg --size 48 --json

# Save the raster used for measurement
python scripts/svg_centroid.py icons/play.svg --size 24 --write-png /tmp/play-24.png
```

**System note:** `cairosvg` needs Cairo libraries on the machine (e.g. `cairo` on macOS via Homebrew, `libcairo2` on Debian/Ubuntu).

### Why rasterize SVG?

Path-only math struggles with strokes, linecaps, fills, groups, and transforms. Rasterizing at **target UI size** matches what users see (including anti-aliasing mass) and stays consistent with the alpha-centroid definition in the skill.

### How to read results

| Output | Meaning |
|--------|---------|
| `canvas_center` | Center of the raster square |
| `alpha_centroid` | Opacity-weighted mass center |
| `ink_bbox` / `ink_bbox_center` | Bounds of pixels above threshold |
| `offset_from_canvas` | Mass vs full box (large → often viewBox/padding) |
| `offset_from_ink_bbox` | Mass vs ink box (asymmetric marks often ≠ 0) |
| `viewBox` | Parsed from SVG when available |
| `likely_viewbox_or_padding_issue` | Heuristic flag when offset &gt; ~8% of size |

**Workflow with the skill**

1. Measure at the size the control uses (`--size 24` or `48`).
2. If offset vs canvas is large → fix viewBox/export first ([examples/svg-bad-viewbox.md](../examples/svg-bad-viewbox.md)).
3. If mass is asymmetric but expected (play triangle) → pad-in-asset; judge by eye.
4. Never treat the number as mandatory CSS `translate` for every icon.

## Shared disclaimer

These scripts support **Evidence-Based Optical Diagnosis**. Severity, confidence, and **Implement / Propose / Abstain** still come from the skill method—not from a single coordinate.
