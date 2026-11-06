# Example: Local optical fix breaks the toolbar set

## Context
Agent applied `translateX(2px)` only to Send. Home, Search, More left geometric.

## Finding

**What was observed:** Send looks better alone; in the full toolbar the row feels uneven and “drifted.”

**Evidence:** Isolated before/after improved; set sheet shows Send out of rhythm with neighbors.

**Related concept:** Icon-set consistency; anti-pattern “optical fix ignores the set.”

**How:** Revert one-off; run set-level diagnosis; pad-in-asset per glyph that needs it; keep frames aligned.

**Severity:** 2  
**Confidence:** High  
**Outcome:** Implement revert + set pass; do not ship isolated nudge  
**Validation:** Full toolbar sheet light/dark; named exceptions only  
**Hand-off:** Document why Send may differ; forbid copying `2px` to all icons  
