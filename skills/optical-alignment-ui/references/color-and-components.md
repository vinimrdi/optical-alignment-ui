# Color weight and layout components

## Color is not the first lever

When a filled icon looks “heavier” than text or an outline icon:

1. **Geometry** — area, silhouette, alignment
2. **Stroke vs fill** — outline mass vs solid mass
3. **Contrast against background**
4. **Only then** chroma / lightness tweaks

Do not default to “lower the lightness” as the primary optical fix.

## What drives perceived weight

- Filled area
- Stroke thickness
- Contrast with background
- Saturation
- Surrounding spacing and density
- Component chrome (borders, elevation)

Same hex can still read differently at different sizes and on different surfaces.

## If you change color

- Re-check WCAG-relevant contrast ([accessibility-and-constraints.md](accessibility-and-constraints.md)).
- Verify light and dark themes.
- Prefer design tokens over one-off hex edits when a system exists.

## Containers and vertical bias

Elements can feel low or high inside cards/modals because of **negative space and neighbor weight**, not only box centering.

Treat “vertical gravity” as a **contextual perceptual heuristic**, not a global rule to shift all modals or illustrations by a fixed amount.

## System exceptions

Document named exceptions (`icon-play`, `icon-send`) rather than scattering unexplained `translate` values. Prefer pad-in-asset so geometric layout stays boring and correct.
