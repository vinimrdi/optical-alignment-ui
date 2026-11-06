# Shapes, icons, and alignment

## Mathematical vs optical alignment

**Mathematical alignment** uses bounding boxes, centers, and equal margins.
**Optical alignment** shifts or scales so the *visible mass* feels balanced.

Start with geometry for layout systems; apply optical correction when the eye disagrees at the target size.

**Platform note (Apple HIG — Icons):** Some icons—especially asymmetric ones—look unbalanced when centered geometrically. Prefer slightly adjusting position until optically centered. A durable pattern is to **bake padding into the asset** so geometric centering of the file yields optical centering of the glyph.

## Visual weight

Asymmetric shapes do not share mass evenly inside their box. A right-pointing play triangle carries more ink on the left (base) than on the tip. Centering the box makes the glyph look shifted toward the base. A download-style mark can look too low if its mass sits at the bottom.

**How:** Nudge the glyph **toward the lighter side / tip** until it feels centered. Keep the **hit area and outer frame** fixed when possible so spacing and targets stay predictable.

**Classic case — play icon:**
- Bounding-box center → often looks left-heavy.
- Optical center → triangle moved slightly toward the point (typically right for LTR play).
- Stronger method when automating: align **centroid** (or appropriate triangle center) to the circle center rather than the fitted box alone (see Bjango).
- Shestopalov tip: imagine a circle around the triangle and align *that* circle to the button, not the raw triangle box.

**Reference:** Apple HIG Icons (optical centering); Luke Jones (Marvel); Marc Edwards / Bjango; Slava Shestopalov (Design Bridges).

## Circle vs square scale

A circle and a square with the same width/height do not appear equal: the square has more area and more contact with the imaginary box.

**Formula aid (equal area):** scale circle diameter by √(4/π) ≈ **1.1284** (~+12.8%) relative to the square’s side when equal *area* is the intent.

**Practice:** At UI sizes, also snap to pixel boundaries when crispness matters more than exact area. Concave shapes may need convex-hull thinking rather than raw path area (Bjango).

**Keylines:** Material-style icon keyline grids formalize different “live” sizes for circle, square, and rect so optical mass matches across a set—not only equal outer frames.

**Limit:** Equal area is one intent among several (equal width, equal optical stroke, equal cap height). State the intent.

**Reference:** Bjango, *Formulas for optical adjustments*; Material icon keyline practice; common UI articles on circle/square pairing.

## Icon sets (visual size, not only box size)

Industry guidelines (Apple, Google, IBM—summarized in research on icon-set visual size/alignment) state that designers should adjust **size and position per icon** for visual consistency instead of only unifying bounding boxes.

- Equal box ≠ equal perceived size.
- Adjust dimensions or live-area padding by visual weight.
- Align optically across the row, not only by box centers.

Validate the full set side-by-side at target sizes (e.g. 20–24 px UI).

## Triangles and other irregular icons

- Prefer **centroid-based** centering for equilateral play marks inside circles when automating.
- Chevrons, carets, arrows, and paper-plane “send” marks often need small optical shifts along their pointing axis.
- Sharp-edged shapes often need to read slightly larger next to soft rectangles (Shestopalov).
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
