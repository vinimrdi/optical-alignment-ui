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

## SVG / CSS / Canvas differences

| Surface | Watch for |
|---------|-----------|
| **SVG** | `viewBox` vs ink; stroke alignment; group transforms |
| **CSS** | flex/grid centers the box, not ink; `line-height` vs glyph bounds |
| **Canvas** | Manual metrics; DPI scaling |
| **Raster** | Alpha bounds; compression halos |

## Automation aid

Centroid/barycentre alignment can reduce pure eyeballing for simple polygons (frontend literature on optical alignment). Always verify at UI size.

## Design-system checklist

1. Frame + keylines (circle / square / rect).
2. Draw for visual weight, not max fill.
3. Optically center; bake padding when possible.
4. Name exceptions.
5. Review set at 1× and 2×, light and dark.
6. Re-check after stroke or radius token changes.
7. Record “do not copy this offset to unrelated icons.”

## Platform APIs (when relevant)

- CSS: `font-optical-sizing`, `font-variation-settings` / `opsz` when the face supports it (MDN).
- Windows XAML: `OpticalMarginAlignment` for text side bearings in some multi-size layouts (Microsoft UI docs)—verify applicability before recommending.

## Limits

No unexplained magic numbers across screens. No broken minimum targets. Automation assists; judgment remains.
