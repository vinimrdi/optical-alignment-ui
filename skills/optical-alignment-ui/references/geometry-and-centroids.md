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

## Decision matrix

| Situation | Prefer |
|-----------|--------|
| Axis-symmetric filled rect | Bounding box |
| Equilateral play in circle | Centroid as check; eye; pad-in-asset for hand-off |
| Outline-only icon | Not fill centroid alone |
| Mixed stroke weights | Perceptual primary |
| PNG with transparency | Alpha-weighted if tooling allows |
| Wrong or loose viewBox | **Fix metadata before optical nudge** |
| Mixed SVG libraries in one set | Per-file ink bounds + keylines |

## Circle vs square — name the intent

| Intent | Meaning | Aid |
|--------|---------|-----|
| **Equal area** | Same filled area | \( d = s\sqrt{4/\pi} \approx 1.1284\,s \) |
| **Equal visual size** | Similar apparent size | Often &lt; full area factor; judge at size |
| **Equal visual weight** | Similar mass incl. stroke/contrast | No single formula |
| **Equal frame occupancy** | Keyline live area | Material-style keylines |
| **Equal prominence** | Similar attention in context | Contextual |

Do not default every circle to +12.8%.

## SVG inspection (measurable checklist)

Record when available:

| Field | Why |
|-------|-----|
| `viewBox` | Maps path space to layout box |
| width / height | Presentation size |
| `stroke-width`, linecap, linejoin | Mass and raster |
| Group/path `transform` | Hidden offsets |
| Ink bounds vs empty padding | True optical box |
| Fill vs stroke-only | Centroid applicability |

### Quick ink-bounds idea (for tooling authors)

1. Rasterize glyph at known size on transparent canvas.  
2. Threshold alpha (e.g. α &gt; 0).  
3. Compute bounding box of nonzero pixels and optional alpha centroid.  
4. Compare to geometric viewBox center.  
5. Still judge perceptually at UI size—this only quantifies mass.

No script is required to use this skill; the checklist prevents inventing offsets when metadata is the bug.

## Stroke and negative space

Outline vs fill at the same outer size read differently. Counters and external empty space change perceived size. After stroke-token changes, re-check sets.

## Attribution discipline

Material keylines: use for set consistency. Apple HIG: cite a **specific** page when attributing a requirement. **Pad-in-asset** is a durable engineering pattern for optical hand-off—not a claim that every HIG page mandates it.

## Limits

No universal pixel offset. Geometric equality ≠ perceptual equality. Automation helps; native-size judgment closes the loop.
