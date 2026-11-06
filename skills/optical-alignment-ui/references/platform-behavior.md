# Platform and rendering behavior

Optical “bugs” are sometimes **rasterization or metric** issues, not composition errors.

## Device pixel ratio (DPR)

| Observation | Interpretation |
|-------------|----------------|
| Looks fine at 2× in design tool, soft or shifted at 1× | Pixel snapping / fractional coordinates |
| Fine on retina preview, off on 1× screenshot QA | Validate at shipping DPRs |

**Agent action:** Prefer integer stroke positions when the system requires crisp 1×. Re-check after `transform` (can create subpixel positions).

## SVG vs CSS layout

- Flex/grid centers the **border box**, not ink.  
- `line-height` and baseline alignment move **line boxes**, not glyph ink.  
- `transform` on the icon does not move the hit target unless the target is the same element—prefer nested structure: large hit area, inner glyph nudge or padded asset.

## Font stack shifts

Fallback fonts change cap-height and sidebearings. Icon+label pairs that were tuned for one face can look wrong after fallback—re-validate critical stacks.

## Theme surfaces

Light and dark change contrast and thus **perceived weight**. A balance that works on white may look heavy on black (or vice versa). Optical QA includes both themes when both ship.

## Design tool vs browser

Figma/Sketch previews may round differently than Safari/Chrome at 100% zoom. Prefer browser or device screenshots for final Confidence High on Implement.

## Limits

This file does not replace browser bug trackers or full cross-browser QA matrices. It flags rendering confounds so agents do not over-correct composition.
