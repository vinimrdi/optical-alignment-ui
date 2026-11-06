# Example: Outline vs filled at the same box size

## Context
Toolbar: filled “Home,” outline “Search,” both 24×24 viewBoxes, same stroke token on outline.

## Finding

**What was observed:** Search reads smaller/lighter than Home though boxes match.

**Evidence:** Side-by-side at 24px; outline has less filled area; blur test shows weaker mass on Search.

**Related concept:** Visual weight; stroke vs fill; keylines.

**Compensation intent:** Equal **visual weight** (not equal area of path data).

**How:** Slightly increase outline live size or stroke within keyline rules; or accept hierarchy if Search is secondary. Do not only dim Home (color-last rule).

**Severity:** 2  
**Confidence:** High for direction; Medium for exact stroke delta  
**Outcome:** Propose token/keyline change for system; Implement only after set sheet  
**Validation:** Full toolbar light/dark; no target change  
