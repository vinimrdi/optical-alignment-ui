# AGENTS.md — Optical Alignment UI

This repository is an **Agent Skill** for optical alignment (precision vs perception) in digital UI.

**Current skill version:** 1.5.3 (`skills/optical-alignment-ui/SKILL.md`).

## Load order

1. Read `skills/optical-alignment-ui/SKILL.md` (required).
2. Open `skills/optical-alignment-ui/references/` only as needed (geometry, evidence, a11y, anti-patterns, …).
3. Optional tools: `scripts/centroid.py`, `scripts/svg_centroid.py` — **diagnostic only**.
4. Worked patterns: `examples/`. Smoke assets: `fixtures/`.
5. Install / Lovable: `docs/compatibility-and-integrations.md`.

## Non-negotiables

- Do not invent universal pixel offsets or fake sources.
- Prefer **pad-in-asset** for design-system hand-off.
- Preserve touch targets; re-check contrast after color changes.
- Centroid / script output ≠ perceptual center — still judge at native UI size.
- Report **severity** and **confidence** independently.
- End with **Implement**, **Propose**, or **Abstain**.
- Check `references/anti-patterns.md` before popular “fixes.”
- Explain while applying, in plain language.
- Skip this skill for physical optics or accessibility-only tasks (use companion UX skill for task friction).

## Invoke

- Slash: `/optical-alignment-ui` when supported.
- Or user language: off-center icon, play button, optical centering, visual weight, overshoot, icon set uneven.
