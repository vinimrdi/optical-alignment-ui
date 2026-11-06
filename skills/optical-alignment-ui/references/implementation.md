# Implementation — design systems and front-end

## Preferred: pad the asset

Bake optical correction into the asset so geometric centering of the **file** yields optical centering of the **glyph**.

## Measure before you nudge

```bash
# Raster icon
python scripts/centroid.py path/to/icon.png --verbose

# SVG at real UI size
pip install pillow cairosvg
python scripts/svg_centroid.py path/to/icon.svg --size 24 -v
```

Large offset vs canvas → fix `viewBox`/export first. See [geometry-and-centroids.md](geometry-and-centroids.md) and [scripts/README.md](../../../scripts/README.md).

## Acceptable: runtime nudge

When assets cannot change:

```css
/* Example only — values are case-specific */
.icon-play {
  transform: translateX(0.06em);
}
```

Document the exception. Mind `transform-origin` and overflow.

## Design-system checklist

1. Frame + keylines.
2. Draw for visual weight.
3. Optically center; pad-in-asset when possible.
4. Optional: `svg_centroid.py --size <px>` on export.
5. Name exceptions.
6. Review set at 1×/2×, light/dark.
7. Re-check after stroke/radius token changes.

## Limits

Script numbers do not replace perceptual judgment or a11y constraints.
