# Example: Toolbar icons look uneven as a set

## Context
24×24 toolbar: Home, Search, Send, More—same viewBox, geometric centering.

## Finding

**What was observed:** Search/Send look smaller or off-axis vs Home though boxes match.

**Evidence:** Full-set review at 24px light/dark.

**Related concept:** Icon-set visual size; keylines.

**How:** Keylines by shape; per-glyph optical weight; bake padding for asymmetric marks; keep frames even.

**Severity:** 2 for primary chrome  
**Confidence:** High for need of set pass  
**Outcome:** Implement after set sheet  
**Validation:** Side-by-side set; 1×/2×  
**Hand-off:** Named exceptions; no universal offset  
