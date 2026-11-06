# Example: Play button looks left-heavy

## Context
Circular media control, 48×48 hit area, filled LTR play triangle, flex-centered SVG.

## Finding

**What was observed:** Triangle appears shifted toward the base (left) though the path box is centered.

**Evidence:** Native 48px inspection; isolated glyph + in-button; optional blur still shows base-heavy mass. Geometric box center ≠ perceived center.

**Related concept:** Visual weight; geometric centroid as diagnostic.

**Compensation intent:** Optical centering of glyph (not equal-area scale).

**What / Why / Who / Where / When / How:** Asymmetric mass in a symmetric control; eye centers on mass not box; all users of primary media control; asset/component; when mark is triangular play; prefer **pad-in-asset** so file center matches optical center; alternative documented `translateX` toward tip only if assets locked. **Hit area unchanged.**

**Severity:** 2–3 (prominence-dependent)  
**Confidence:** High for direction; exact padding **Medium** until measured at size  
**Outcome:** Implement if Confidence ≥ Medium after pad trial; else Propose  
**Validation:** Before/after at 48px; light/dark; no clip; target still 48×48  
**Hand-off:** Exception name `icon-play`; do not copy offset to symmetric icons.
