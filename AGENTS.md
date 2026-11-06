# AGENTS.md — Optical Alignment UI

This repository is an **Agent Skill** for optical alignment (precision vs perception) in digital UI.

## Load order

1. Read `skills/optical-alignment-ui/SKILL.md` (required).
2. Open files under `skills/optical-alignment-ui/references/` only as needed.
3. For install paths and Lovable attach workflow, see `docs/compatibility-and-integrations.md`.

## Non-negotiables

- Do not invent universal pixel offsets or fake sources.
- Prefer pad-in-asset for design-system hand-off.
- Preserve touch targets; re-check WCAG contrast after color lightness changes.
- Explain while applying, in plain language.
- Skip this skill for physical optics or accessibility-only tasks.

## Invoke

- Slash: `/optical-alignment-ui` when supported.
- Or user language: off-center icon, play button, optical centering, visual weight, overshoot.
