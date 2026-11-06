# Example: Play button looks left-heavy

## Context
Circular media control, 48×48 hit area, filled LTR play triangle, flex-centered SVG.

## Finding

**What was observed:** Triangle appears shifted toward the base (left) though path box is centered.

**Evidence:** Native 48px; isolated + in-button; optional blur shows base-heavy mass.

**Related concept:** Visual weight; geometric centroid as diagnostic.

**Compensation intent:** Optical centering of glyph (not equal-area scale).

**How:** Prefer **pad-in-asset** so file center ≈ optical center; else documented nudge toward tip. **Hit area unchanged.**

**Severity:** 2–3  
**Confidence:** High for direction; Medium for exact padding until viewed at size  
**Outcome:** Implement if Confidence ≥ Medium after pad trial; else Propose  
**Validation:** Before/after 48px; light/dark; no clip; target 48×48  
**Hand-off:** `icon-play`; do not copy to symmetric icons  
