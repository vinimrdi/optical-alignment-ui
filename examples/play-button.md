# Example: Play button looks left-heavy

## Context

Circular media control, 48×48 hit area, filled equilateral play triangle (LTR), SVG centered with `margin: auto` / flex center on the viewBox.

## Finding

**What was observed:** Triangle appears shifted toward the left (base) even though the path’s bounding box is centered in the circle.

**Evidence:** Side-by-side comparison of geometric center vs perceived center at 1× and 2×; optional blur still shows mass bias to the base.

**Related concept:** Visual weight; centroid vs bounding-box center (UI heuristic + geometry aid).

**What:** Optical imbalance of an asymmetric glyph in a symmetric container.  
**Why:** More visible mass sits at the triangle base than at the tip; the eye’s “center” is not the box center.  
**Who:** All users; more obvious on large controls and sparse layouts.  
**Where:** Play icon asset and/or icon component used in the media button.  
**When:** When the mark is a right-pointing triangle (or similar); pure geometry may suffice for symmetric glyphs.  
**How:** Prefer **pad-in-asset** (empty margin on the base side so geometric center of the file ≈ optical center of the glyph). Alternative: small `translateX` toward the tip only if assets cannot change. Keep the 48×48 hit area unchanged.

**Impact:** Primary control feels less trustworthy/polished.  
**Severity:** 2–3 depending on prominence.  
**Trade-off:** One named exception (`icon-play`) in the system vs ad-hoc CSS on every screen.  
**Validation:** Side-by-side math vs optical at target size; check dark/light; confirm touch target still ≥ policy.  
**Confidence:** Confirmed for classic play marks; exact offset is **per drawing** (hypothesis until viewed at size).

### Explain while applying (sample)

> **Visual weight (UI heuristic):** The play triangle carries more mass on the left, so bounding-box centering looks left-heavy. We shift the glyph toward the tip (or bake that into the SVG padding) so it *looks* centered without changing the hit target. Confirm by eye at 48px; there is no universal pixel value for every triangle.
