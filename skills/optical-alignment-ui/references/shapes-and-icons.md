# Shapes, icons, and alignment

## Mathematical vs optical

**Mathematical** alignment uses boxes and equal margins.  
**Optical** alignment shifts or scales so visible mass feels balanced.

Start with geometry for systems; correct when the eye disagrees **at use size**.

**Pad-in-asset (preferred hand-off):** bake optical correction into empty margin/`viewBox` padding so **file geometric center ≈ glyph optical center**. Developers keep simple centering; fewer magic `translate` values. Treat this as an engineering pattern for systems—not a claim that every platform HIG page mandates it unless you verify that page.

## Visual weight

Asymmetric marks (play, send, chevron, download) do not share mass evenly in the box. Nudge **toward the lighter side / tip**. Keep **hit area and outer frame** fixed.

**Play icon:** box center often looks left-heavy; optical center moves toward the tip. Centroid alignment is a useful **check**, not automatic truth. Shestopalov: imagine a circle around the triangle and align that to the button.

## Circle vs square

Same width ≠ same perceived size. If equal **area** is the intent, diameter ≈ side × √(4/π) ≈ ×1.128. Often **equal visual weight** needs a smaller adjustment—**state the intent**. Snap to pixels when needed. Material-style **keylines** formalize different live areas by shape.

## Icon sets

Equal box ≠ equal perceived size. Adjust per glyph for visual weight; keep **frames** even for scanability and targets. Review the full set at target size on light and dark.

## Stroke, fill, negative space

Outline vs filled icons at the same outer size read differently. Internal counters and external empty space change perceived size. After stroke-width token changes, re-check the set.

## Icon + label

Align to a stable text metric; compare **silhouette** to label ink, not only viewBox. Prefer fixing the asset when many instances share it.

## Pixel alignment

At 16–24px, fractional strokes and off-pixel anchors create false “optical” problems. Align strokes for consistent rasterization when the design system requires it.

## What not to do

- Do not change touch targets to hide a bad drawing.
- Do not apply one +2px offset to every icon.
- Do not confuse optical nudge with inconsistent padding tokens.
