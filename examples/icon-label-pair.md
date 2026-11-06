# Example: Icon + label feel uneven

## Context

Pill button: leading chevron-right + label “Continue”. Same gap token as other buttons. Icon and text vertically centered on the flex line box.

## Finding

**What was observed:** Chevron appears slightly low (or high) relative to the label’s cap-height; the pair feels “not on one line.”

**Evidence:** Visual inspection at UI size; comparison of icon silhouette to caps of the label (not only the SVG viewBox).

**Related concept:** Icon–label optical alignment.

**What:** Mismatch between glyph silhouette and type metrics.  
**Why:** ViewBox center ≠ ink center; x-height/cap-height and stroke weight change perceived midline.  
**Who:** Everyone reading the control; worse when mixed icon styles (outline vs filled).  
**Where:** Button content layout or the chevron asset.  
**When:** Icon+text pairs; less critical for icon-only.  
**How:** Nudge glyph with small `translateY` **or** adjust padding inside the SVG; prefer fixing the asset if many instances share it. Do not change the gap token only to “hide” a bad glyph.

**Impact:** Secondary polish; repeated across the product it accumulates as “cheap UI.”  
**Severity:** 1–2.  
**Trade-off:** Asset exception vs per-instance CSS.  
**Validation:** Compare against a square bullet or SF Symbol–style mark known to align; check bold label weight.  
**Confidence:** Probable until checked at final type size/weight.
