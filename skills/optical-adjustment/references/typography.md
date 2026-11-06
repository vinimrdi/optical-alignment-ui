# Typography: overshoot, optical margin, optical size

## Overshoot

**Category:** Type design mechanic (practice with long craft tradition).

**What:** Round or pointed letterforms (O, C, A, V, …) are drawn slightly beyond the baseline, x-height, or cap-height so they *appear* the same size as flat letters (H, X, E).

**Why:** Only a small part of a curve touches the guide line; most of the shape falls away. The eye reads the round form as smaller if heights are mathematically equal. Pointed forms need equal or greater compensation than rounds.

**Typical magnitude (guidance, not a law):** On the order of about 1–3% of cap- or x-height for O; pointed forms often more. Peter Karow’s *Digital Formats for Typefaces* is widely cited for roughly 3% (O) and 5% (A)—always judge on the specific face and size.

**Who / Where / When:** Every quality text face; relevant when judging vertical alignment of mixed shapes or when building geometric logotypes that must match type.

**How in UI work:**
- Do not “correct” a professional font by clipping overshoot.
- When drawing geometric marks next to type, allow slight overshoot for circles and peaks.
- At very small sizes, overshoot interaction with pixels matters; check rasterized result.

**Limit:** Percentages vary by designer, weight, and curvature. There is no single correct overshoot for all faces.

**Reference:**
- Tobias Frere-Jones, Typeface Mechanics (overshoot): eye wins over ruler; round and pointed forms need progressive compensation.
- Wikipedia, *Overshoot (typography)* — definition and typical ranges; cites Karow.
- Monotype Foundry Support, lack of overshoots — practical type production note.

## Optical margin alignment (hanging punctuation)

**Category:** Type / layout practice.

**What:** Punctuation and some diagonal capitals (e.g. A, V, W, Y) are allowed to hang slightly into the margin so the *text edge* looks straight.

**Why:** Quotes, periods, and diagonals take little vertical ink at the edge; strict indentation makes the column look ragged inward.

**Where / When:** Body text columns, block quotes; less critical for short UI labels.

**How:** In editorial tools, enable optical margin alignment. On the web, approximate only when the layout justifies the complexity (hanging punctuation is limited in pure CSS).

**Limit:** Font-dependent; not a substitute for good measure and leading. Wikipedia notes it is aimed at body text, not tables or display one-liners.

**Reference:** Wikipedia, *Optical margin alignment*.

## Optical size (`opsz`)

**Category:** Type design + CSS feature.

**What:** Letterforms optimized for the size at which they are set—sturdier, more open forms at small sizes; higher contrast and finer detail at large sizes.

**Why:** One master outline does not read equally well at 11px and 72px.

**How:**
```css
font-optical-sizing: auto; /* default when the face has opsz */
/* or explicit */
font-variation-settings: "opsz" 14;
```
Use variable fonts that expose the `opsz` axis. Prefer `auto` unless you intentionally override.

**Limit:** Only works when the font actually provides optical-size designs. Not a fix for poor hierarchy or weak contrast.

**Reference:**
- MDN, `font-optical-sizing`
- MDN, Variable fonts guide (`opsz`)
- Google Fonts Knowledge, Optical Size axis

## ALL CAPS next to mixed case

**Category:** UI heuristic.

**What:** Caps at the same computed size as sentence case often *look* larger and heavier.

**How:** If parity is the goal, reduce caps slightly (commonly on the order of 1–2px at UI sizes, or a modest relative scale). If emphasis is the goal, keep the size and accept prominence.

**Limit:** Depends on the face’s cap height and weight. Always check the real pair.

**Reference:** Luke Jones, *Optical Adjustment – Logic vs. Designers* (Marvel / Medium)—caps example used widely in UI writing.

## Button label vertical alignment

**Category:** UI heuristic.

**What:** Centering a text node by its line-box is not always the same as centering the visible cap-height or x-height mass. Descenders (g, y, p) pull perceived weight down; all-caps blocks sit differently than mixed case.

**How:** Prefer consistent system rules (e.g. align to cap-height for title-case actions). Small baseline nudges are acceptable for one-off icons+labels; document system-wide choices.

**Reference:** Slava Shestopalov, *Optical effects in user interfaces* (cap-height vs x-height approaches for button labels).
