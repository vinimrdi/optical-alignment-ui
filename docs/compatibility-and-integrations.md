# Compatibility and integrations

**Optical Alignment UI** uses the Agent Skills layout: folder `optical-alignment-ui` with `SKILL.md` (`name` must match folder) and optional `references/`.

Three different claims—do not merge them:

1. **Format** — understandable as a SKILL.md skill  
2. **Discovery** — agent auto-loads from a known path  
3. **Execution** — model can follow instructions and open reference files  

## Install paths (verify on your agent version)

| Platform | Format | Auto-discovery | Notes |
|----------|--------|----------------|-------|
| **Claude Code** | Agent Skills | Personal `~/.claude/skills/`; project `.claude/skills/` | Test personal vs project; new session after install |
| **Cursor** | Agent Skills | `.cursor/skills/`, `.agents/skills/`, also Claude-compatible paths | Distinguish local vs Cloud Agents per Cursor docs |
| **Codex** | Agent Skills | `.agents/skills/`, product-specific paths | Skills ≠ persistent `AGENTS.md` instructions |
| **GitHub Copilot** | Varies by surface | Do not assume | Check VS Code / CLI / app separately |
| **Lovable** | Project context | **Do not assume** local skill scan | Attach `SKILL.md` + references explicitly |
| **Other agents** | Conditional | Do not assume | Require an install test |

### Manual install

```bash
git clone https://github.com/vinimrdi/optical-alignment-ui.git
mkdir -p ~/.claude/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.claude/skills/optical-alignment-ui

mkdir -p ~/.cursor/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.cursor/skills/optical-alignment-ui

mkdir -p ~/.agents/skills
cp -R optical-alignment-ui/skills/optical-alignment-ui ~/.agents/skills/optical-alignment-ui
```

**Critical:** `SKILL.md` at `…/optical-alignment-ui/SKILL.md` — no extra nesting.

### CLI (if available)

```bash
npx skills add vinimrdi/optical-alignment-ui --skill optical-alignment-ui
```

## Lovable / chat

1. Attach `skills/optical-alignment-ui/SKILL.md`.
2. Attach needed `references/*.md`.
3. Prefer read-only diagnosis first.

### Implementation prompt after approval

```text
Using the Optical Alignment UI skill, implement only approved findings.
For each change: problem, concept, why it fits — plain language.
Outcome was Implement only. Do not shrink touch targets.
Re-check contrast if color changes. Prefer pad-in-asset when possible.
```

## Verification checklist

- [ ] Folder name = `optical-alignment-ui`
- [ ] Frontmatter `name: optical-alignment-ui`
- [ ] New agent session
- [ ] Test: “Play icon looks off-center—use optical-alignment-ui”
- [ ] Agent can open at least one `references/` file when asked
