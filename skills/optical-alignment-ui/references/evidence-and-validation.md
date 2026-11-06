# Evidence and validation

## Evidence-Based Optical Diagnosis

### Required

1. **Native size** — use size, not only zoomed artboards  
2. **Isolated and in context** — glyph alone and in the real control/row  
3. **Geometric vs visual** — box center vs mass center vs perceived center  
4. **Artifact check** — DPR, hinting, compression vs composition  
5. **Before state** — baseline description or screenshot before change  

### Optional

Blur test; side-by-side candidates; both themes.

### Evidence vs hypothesis

| Evidence | Hypothesis |
|----------|------------|
| “At 24px in the toolbar, send mass sits low-left vs neighbors.” | “Users will abandon the flow.” |

Do not present impact hypotheses as confirmed without data.

## Outcomes

| Outcome | Gate |
|---------|------|
| **Implement** | Confidence ≥ Medium; severity justifies work; a11y OK |
| **Propose** | Weaker confidence or high product risk |
| **Abstain** | Unverified/Low with weak severity, or no real issue |

## Optical QA protocol

1. Before/after at use size  
2. DPR 1× when relevant; 2×/3× if shipped  
3. Component size variants sharing the asset  
4. Clipping, overflow, `transform-origin`  
5. Light/dark  
6. Full set / neighbors  
7. Hit target dimensions unchanged  
8. Contrast if color changed  

## Design-system regression gates

Before marking Implement on a system icon:

- [ ] Exception named  
- [ ] Scope stated (which components)  
- [ ] “Do not copy to unrelated glyphs” noted  
- [ ] Set sheet reviewed  
- [ ] No target shrink  

## What not to claim

No user-test proof from inspection alone. No “Apple requires X” without verified page. No equal-area as mandatory visual weight.
