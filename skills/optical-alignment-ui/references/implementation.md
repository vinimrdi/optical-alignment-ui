# Implementation — design systems and front-end

Optical alignment fails in production when design tools nudge once and code re-centers the raw path. Prefer patterns that survive hand-off.

## Preferred: pad the asset

**Apple HIG pattern:** Put optical correction into the asset as asymmetric padding (or empty viewBox margin) so the **file’s geometric center** matches the **glyph’s optical center**. Developers then center the asset mathematically and the result looks right.

Benefits: stable CSS, fewer one-off `translate` values, consistent Storybook/Figma previews.

## Acceptable: runtime nudge

When assets cannot change:

```css
/* Example only — values are case-specific, not standards */
.icon-play {
  transform: translateX(0.06em); /* toward tip for LTR play */
}
.icon-with-label {
  transform: translateY(-0.03em); /* example vertical optical tweak */
}
```

Prefer relative units (`em`) tied to the control’s type size when the icon scales with text. Document the exception on the component.

## Front-end / automation angle

For simple polygons, **barycentre (centroid)** alignment is a repeatable alternative to pure eyeballing (Grekov / Bumble series on optical alignment for frontend developers):

1. Identify the visible shape (not only the SVG canvas).
2. Compute or approximate its center of mass.
3. Align that center to the control’s center; keep the hit target fixed.

Libraries that estimate glyph optical bounds (e.g. canvas-based optical-properties experiments) can help tooling—but always verify at UI size.

## Design-system checklist

| Step | Action |
|------|--------|
| 1 | Define frame size and live area (keylines for circle / square / rect). |
| 2 | Draw glyph for visual weight, not max fill of the box. |
| 3 | Optically center; bake padding into export when possible. |
| 4 | Name exceptions (`icon-play`, `icon-send`) in the system. |
| 5 | Review full set at 1x and 2x on light and dark. |
| 6 | Re-check after stroke weight or corner-radius tokens change. |

## Platform APIs (when relevant)

- **CSS:** `font-optical-sizing: auto` and `font-variation-settings: "opsz" …` for faces that support optical size.
- **Windows XAML:** `OpticalMarginAlignment` on text blocks can trim side bearings so mixed-size type aligns by ink edge rather than advance width—use when multi-size type looks ragged at container edges (Microsoft UI XAML docs).

## Limits

- Do not scatter unexplained magic numbers across screens.
- Do not break minimum touch targets to hide a bad drawing.
- Automation helps; target-size judgment still wins for composite icons.
