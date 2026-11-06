# Shapes, icons, and alignment

## Mathematical vs optical alignment

**Mathematical alignment** uses bounding boxes, centers, and equal margins.
**Optical alignment** shifts or scales so the *visible mass* feels balanced.

Start with geometry for layout systems; apply optical correction when the eye disagrees at the target size.

## Visual weight

Asymmetric shapes do not share mass evenly inside their box. A right-pointing play triangle carries more ink on the left (base) than on the tip. Centering the box makes the glyph look shifted toward the base.

**How:** Nudge the glyph **toward the lighter side / tip** until it feels centered. Keep the **hit area and outer frame** fixed when possible so spacing and targets stay predictable.

**Classic case — play icon:**
- Bounding-box center → often looks left-heavy.
- Optical center → triangle moved slightly toward the point (typically right for LTR play).
- Stronger method when automating: align **centroid** (or appropriate triangle center) to the circle center rather than the fitted box alone (see Bjango).

**Reference:** Luke Jones (Marvel); Marc Edwards / Bjango, *Formulas for optical adjustments*; widespread UI writing on play-button centering.

## Circle vs square scale

A circle and a square with the same width/height do not appear equal: the square has more area and more contact with the imaginary box.

**Formula aid (equal area):** scale circle diameter by √(4/π) ≈ **1.1284** (~+12.8%) relative to the square’s side when equal *area* is the intent.

**Practice:** At UI sizes, also snap to pixel boundaries when crispness matters more than exact area. Concave shapes may need convex-hull thinking rather than raw path area (Bjango).

**Limit:** Equal area is one intent among several (equal width, equal optical stroke, equal cap height). State the intent.

**Reference:** Bjango, *Formulas for optical adjustments*; common UI articles on circle/square pairing.

## Triangles and other irregular icons

- Prefer **centroid-based** centering for equilateral play marks inside circles when automating.
- Chevrons, carets, and arrows often need small optical shifts along their pointing axis.
- Rounded corners change how much of the shape “touches” the box; re-check after corner radius changes.

## Icon + label

1. Align using a stable text metric (line box or cap-height rule).
2. Compare the **visible** icon silhouette to the label—not only the icon’s square viewBox.
3. Adjust glyph offset inside the icon frame rather than breaking the component’s gap token when possible.

Mixed scripts, all-caps labels, and filled vs outline icons change the result; verify the real pair.

## Groups of icons

A row of icons with different silhouettes can look uneven even when boxes align. Optical correction is per-glyph; the **grid of frames** should stay even for scanability and targets.

## What not to do

- Do not change touch-target size ad hoc to “fix” a drawing.
- Do not apply the same +2px offset to every icon in a set without checking each silhouette.
- Do not confuse optical nudge with inconsistent padding tokens across the system.
