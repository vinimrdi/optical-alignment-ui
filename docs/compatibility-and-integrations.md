# Compatibility and integrations

**Optical Alignment UI** follows the open **Agent Skills** layout: a folder named `optical-alignment-ui` containing `SKILL.md` (YAML `name` + `description` + markdown body) and optional `references/`.

`name` must match the folder name: `optical-alignment-ui`.

## Install paths by agent

| Agent | Personal (all projects) | Project (this repo) |
|-------|-------------------------|---------------------|
| **Claude Code** | `~/.claude/skills/optical-alignment-ui/` | `.claude/skills/optical-alignment-ui/` |
| **Cursor** | `~/.cursor/skills/` or `~/.agents/skills/` | `.cursor/skills/` or `.agents/skills/` (also loads `.claude/skills/`) |
| **Codex** | `~/.agents/skills/` or `~/.codex/skills/` | `.agents/skills/` or `.codex/skills/` |
| **Gemini CLI** | `~/.agents/skills/` or `~/.gemini/skills/` | `.agents/skills/` |
| **OpenCode** | agent skills dir per product docs | `.agents/skills/` |
| **GitHub Copilot (skills)** | `~/.copilot/skills/` when supported | `.agents/skills/` |

### Manual install (any agent)

```bash
git clone https://github.com/vinimrdi/optical-adjustment.git
# After GitHub rename, prefer: vinimrdi/optical-alignment-ui

mkdir -p ~/.claude/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui

# Cursor example
mkdir -p ~/.cursor/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.cursor/skills/optical-alignment-ui

# Shared agents path
mkdir -p ~/.agents/skills
cp -R optical-adjustment/skills/optical-alignment-ui ~/.agents/skills/optical-alignment-ui
```

**Critical:** `SKILL.md` must sit at `…/optical-alignment-ui/SKILL.md` — not nested an extra level.

### CLI (when available)

```bash
npx skills add vinimrdi/optical-adjustment --skill optical-alignment-ui
# or after rename:
npx skills add vinimrdi/optical-alignment-ui
```

Use `--agent cursor` / product flags if your CLI supports targeting one client.

## Claude Code

- Auto-activates when the user request matches the skill **description**.
- Explicit: `/optical-alignment-ui`
- Prefer project install + commit for team consistency.
- Start a **new session** after install.

## Cursor

- `/optical-alignment-ui` or `@` attach the skill.
- Skills load from `.cursor/skills/`, `.agents/skills/`, and Claude-compatible paths.
- New Agent chat after install.

## Lovable and chat-only UIs

Lovable and similar products may not scan `~/.claude/skills`. Use **context attach**:

1. Open `skills/optical-alignment-ui/SKILL.md`.
2. Attach needed files under `references/` (shapes, implementation, typography).
3. Prompt: review-only first, then implement with explain-while-applying.

### Implementation prompt after approval

```text
Using the Optical Alignment UI skill, implement only the approved findings.
For each change, explain the problem fixed, the UX/optical concept applied,
and why it fits — in plain language the user can learn from.
Do not change touch targets or invent universal pixel offsets.
Re-check contrast if any color lightness changes.
```

## Codex / other coding agents

Place the same folder under `.agents/skills/optical-alignment-ui/`. Invoke by name or describe the optical imbalance; the description field drives matching.

## Pairing with other skills

| Skill | Role |
|-------|------|
| **ux-laws-principles** (or similar) | Task friction, heuristics, accessibility |
| **optical-alignment-ui** | Perception vs precision, icon/type craft |

Run usability/a11y first when both apply; optical polish second.

## Verification checklist

- [ ] Folder name = `optical-alignment-ui`
- [ ] `SKILL.md` present with `name: optical-alignment-ui`
- [ ] `references/` optional files resolve relatively from SKILL.md
- [ ] New agent session started
- [ ] Test prompt: “Play icon looks off-center—use optical alignment UI skill”
