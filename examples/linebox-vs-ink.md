# Example: Label centered on line box looks low

## Context
Primary button, title-case label with descenders (“Shipping”). Flex `align-items: center` on the line box.

## Finding

**What was observed:** Text mass feels slightly low in the pill; all-caps sibling buttons look better centered.

**Evidence:** Cap-height mass sits above geometric line-box center when descenders pull the box; comparison with all-caps variant.

**Related concept:** Line box vs ink / cap-height alignment.

**How:** Prefer system rule (e.g. optical pad or cap-height alignment for title-case actions). Avoid random `line-height` hacks that break multi-line buttons.

**Severity:** 1–2  
**Confidence:** Medium  
**Outcome:** Propose system rule; Abstain on one-off if only one button  
**Validation:** Title-case and all-caps variants; focus ring unchanged  
