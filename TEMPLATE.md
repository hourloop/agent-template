# Hour Loop AI Agent Template

This is a [GitHub template repository](https://docs.github.com/repositories/creating-and-managing-repositories/creating-a-template-repository) for bootstrapping a new AI agent managed by [Guild](https://guild.hourloop.com).

## How to use

Click the green **Use this template** button (or run `gh repo create <owner>/<new-agent> --template hourloop/agent-template --private --description "What this agent does"`).

When you create a new repo from this template, a one-shot GitHub Action (`.github/workflows/init.yml`) runs on the first push and:

1. Substitutes `{{AGENT_NAME}}` / `{{AGENT_DESCRIPTION}}` placeholders in `SOUL.md`, `IDENTITY.md`, `AGENTS.md`, `TOOLS.md`, `README.md` from the new repo's name + description.
2. Removes the sentinel (`.scaffold-init`), this self-explainer (`TEMPLATE.md`), and the init workflow itself.
3. Pushes the cleanup commit.

After ~30s your new agent's repo will be indistinguishable from one scaffolded through Guild's web UI.

## Source of truth

The contents of this template repo are mirrored from `scaffolds/agent-template/` in [hourloop/guild](https://github.com/hourloop/guild) on every push to `main`. **Don't edit files here directly** — they'll be overwritten on the next mirror sync. To improve the template, edit the markdown files under `scaffolds/agent-template/` in the Guild repo.
