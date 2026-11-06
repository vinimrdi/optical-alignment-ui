# Color weight and layout components

## Color and perceived weight

**What:** The same hex on a solid icon and on thin text often does not *look* the same. Filled shapes read heavier/darker.

**How:** Adjust **lightness** (L in HSL or B in HSB) slightly—lighten the heavy filled shape or darken the thin text—while keeping hue stable when the goal is one family color.

**Mandatory:** Re-check **WCAG contrast** for text and meaningful icons after any lightness change.

**Limit:** Do not build fragile per-component color exceptions that fragment the palette. Sometimes a heavier type style is cleaner than a second color token (Bjango’s caution).

**Reference:** Luke Jones, optical adjustment (colour); UI articles echoing HSB/HSL nudges; always pair with accessibility checks.

## Vertical “gravity” in containers

Perfect vertical centering can look slightly low for some compositions (especially larger masses). A small upward shift may improve perceived balance in modals, tiles, or illustration frames.

**Limit:** Hypothesis-level; verify per layout. Do not break scroll or safe-area rules.

**Reference:** Discussed in component-level optical adjustment writing (e.g. Prototypr / Lovchikov-style component notes).

## Spacing between different sizes

Equal mathematical gaps between a large title and a small row can look tighter than equal gaps between two small rows. Optical spacing often gives **more** space after larger elements.

Related to grouping: elements that belong together should be closer to each other than to neighbors (Gestalt proximity)—optical judgment refines the scale of those gaps.

## Rounded rectangles and padding

Large corner radii reduce contact with the outer box; content may need slightly different padding to *feel* even, especially for short labels in highly rounded pills.

## Design-system guidance

Document **named exceptions**:
- `icon-play` optical offset inside `icon-button`
- circle avatar vs rounded-square thumbnail scale
- caps style size token when used beside sentence case

Exceptions should be intentional, few, and tested—not ad hoc magic numbers in every screen.
