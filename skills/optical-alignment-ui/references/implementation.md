# Implementation — design systems and front-end

## Preferred: pad the asset

Put optical correction in the asset (asymmetric padding / viewBox) so geometric centering of the **file** yields optical centering of the **glyph**. Stable CSS; fewer one-offs.

## Acceptable: runtime nudge

When assets cannot change:

```css
/* Example only — values are case-specific */
.icon-play {
  transform: translateX(0.06em);
}
```

Prefer `em` when the icon scales with type. Document the component exception. Mind `transform-origin` and overflow clipping.

## Measuring before you nudge

```bash
python scripts/centroid.py path/to/icon.png --verbose
```

Use offsets as **diagnostic hints**. Large offset from canvas center often means fix export/`viewBox` first. See [geometry-and-centroids.md](geometry-and-centroids.md) and [scripts/README.md](../../../scripts/README.md).

## SVG / CSS / Canvas differences

| Surface | Watch for |
|---------|-----------|
| **SVG** | `viewBox` vs ink; stroke alignment; group transforms |
| **CSS** | flex/grid centers the box, not ink; `line-height` vs glyph bounds |
| **Canvas** | Manual metrics; DPI scaling |
| **Raster** | Alpha bounds; compression halos |

## Design-system checklist

1. Frame + keylines (circle / square / rect).
2. Draw for visual weight, not max fill.
3. Optically center; bake padding when possible.
4. Optional: run `centroid.py` on export at target size.
5. Name exceptions.
6. Review set at 1× and 2×, light and dark.
7. Re-check after stroke or radius token changes.
8. Record “do not copy this offset to unrelated icons.”

## Platform APIs (when relevant)

- CSS: `font-optical-sizing`, `font-variation-settings` / `opsz` when the face supports it (MDN).
- Windows XAML: `OpticalMarginAlignment` — verify applicability before recommending.

## Limits

No unexplained magic numbers across screens. No broken minimum targets. Numbers from `centroid.py` do not replace perceptual judgment.
