# {{AGENT_NAME}}

{{AGENT_DESCRIPTION}}

## What's in this repo

This repo holds the declarative content for an OpenClaw agent. There is
no runtime code here — the HTTP server, Dockerfile, and dependencies
are supplied by Guild's harness at deploy time.

```
├── SOUL.md       # Persona, boundaries, tone
├── IDENTITY.md   # Agent name, role, metadata
├── AGENTS.md     # Operating instructions and workflows
├── TOOLS.md      # Available tools and their schemas
├── USER.md       # Handler's profile and preferences
├── avatar.svg    # Agent avatar (displayed in Guild)
├── skills/       # Skill bindings (managed via Guild)
└── README.md     # This file
```

## Editing

Edit any of the OpenClaw files here directly on GitHub. Changes take
effect on the next deploy from Guild — open the agent's page at
[guild.hourloop.com](https://guild.hourloop.com) and click **Deploy
latest**.

## Deployment, integration, and access control

All managed through [Guild](https://guild.hourloop.com). The agent
detail page has the live deployment status, the runtime config, the
playground for interactive testing, copy-paste integration snippets,
and the access ACL.

This project follows [OpenClaw](https://github.com/openclaw/openclaw)
conventions and is portable to any compatible harness.
