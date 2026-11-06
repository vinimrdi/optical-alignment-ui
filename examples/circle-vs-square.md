# Example: Circle looks smaller than square

## Context
Grid of media thumbs: circular avatars and rounded-square covers, both width/height 40px.

## Finding

**What was observed:** Circles read smaller/lighter than rounded squares in the same row.

**Evidence:** Same CSS box; blur test; known area difference.

**Related concept:** Area vs visual weight; keylines.

**Compensation intent:** State explicitly—e.g. **equal visual weight** or **equal frame occupancy**, not assumed equal area.

**How:** Slightly larger circle live area or keyline rule; if equal **area** is intended, diameter ≈ ×1.128 then snap pixels. Document intent.

**Severity:** 2 in dense pickers; 1 if sparse  
**Confidence:** High for direction; Medium for exact scale  
**Outcome:** Propose token/keyline; Implement after grid QA  
**Validation:** Mixed row at 1×; no clipping  
