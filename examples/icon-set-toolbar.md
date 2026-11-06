# Example: Toolbar icons look uneven as a set

## Context

24×24 toolbar: Home (square-ish), Search (circle-heavy), Send (paper-plane), More (horizontal dots). All assets use the same viewBox and geometric centering.

## Finding

**What was observed:** Search and Send look smaller or off-axis compared with Home; the set feels inconsistent though boxes match.

**Evidence:** Full-set review at 24px on light and dark; Apple/Google-style guidance that visual weight needs per-icon adjustment.

**Related concept:** Icon-set visual size and optical alignment (platform guidance theme).

**What:** Uniform frames without optical equalization.  
**Why:** Silhouette area, stroke, and asymmetry differ; one centering rule does not fit all drawings.  
**Who:** Daily users of the chrome; trained eyes notice first, but inconsistency scales with frequency.  
**Where:** Icon production pipeline / design-system keylines.  
**When:** Building or refactoring a set; after changing stroke width tokens.  
**How:** Define keylines (circle / square / rect live areas); adjust each glyph for optical weight; bake padding for asymmetric marks (Send, carets); name exceptions. Re-export; keep hit areas identical.

**Impact:** Product chrome feels unfinished.  
**Severity:** 2 for primary toolbars.  
**Trade-off:** More design QA time vs long-term consistency.  
**Validation:** Side-by-side set sheet; 1× raster; compare to SF Symbols / Material reference density if matching a platform.  
**Confidence:** Confirmed need for set-level review; per-icon deltas remain judgment calls.
