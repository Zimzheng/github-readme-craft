---
name: github-readme-craft
description: Create or revise a high-quality GitHub README with language selection, verified installation steps, clickable visual demos, and privacy-aware publishing checks. Use for repository landing pages, README rewrites, and GitHub documentation polish.
---

# GitHub README Craft

Create a README that lets a new visitor understand the project, see a credible
example, install it, and take the next useful action without reading the code.

## Start with language selection

Before inspecting or editing the README, ask the user to choose:

1. the **primary language** for the README; and
2. any **optional languages** to publish alongside it, or “none”.

This selection is required even when the repository has an existing README.
Do not infer it from the repository, account locale, or prior files. After the
user selects, use the primary language in `README.md`; create language variants
only when the user requested them, and link variants visibly near the top.

## Discover the product before writing

- Inspect the repository structure, package manifests, executable entry points,
  existing docs, demos, and deployment configuration.
- Identify the audience, the one-sentence value proposition, the shortest
  successful install/run path, and what evidence can demonstrate the result.
- Verify installation commands against the repository's actual files and tools.
  Do not publish placeholder commands, untested package names, or guessed URLs.
- Preserve useful project-specific information. Keep the README as a landing
  page; move exhaustive API or implementation reference to linked documents.

Read [readme-playbook.md](references/readme-playbook.md) before drafting.

## Build the README

- Put the project name, a concrete one-sentence description, and the most
  useful action near the top. Use badges only when they convey maintained facts.
- Include a visual demonstration when it helps readers judge the product:
  screenshots, a short GIF, a terminal capture, a diagram, or an explicitly
  labeled illustrative mockup. Never present a mockup as a live result.
- Make preview images clickable when a richer destination exists. Use repository
  relative paths for image assets and internal documentation links.
- When a full HTML report, app, or interactive sample cannot render inside
  GitHub Markdown, link the preview image to a verified public demo page or
  clearly label the source-file destination.
- Give complete, copyable commands. Include prerequisites only when required.
  Separate ordinary user installation from contributor/development setup.
- Use concise sections chosen for the project: overview, demo, features, quick
  start, usage, architecture, configuration, examples, documentation,
  contributing, security, and license. Omit sections that add no value.

## Privacy and publishing

- Use fictional or sanitized examples for public demonstrations unless the user
  explicitly approves real project material. Explain that sample data is
  fictional when readers could mistake it for a finding or customer deployment.
- Before a public commit or push, scan staged content for local paths, tokens,
  credentials, personally identifying material, private research artifacts, and
  accidental output files. Remove only the findings relevant to public release.
- Do not create a repository, enable GitHub Pages, push, or alter a remote until
  the user authorizes that external action. If hosting is needed for a clickable
  HTML demo, prepare the files and configuration first; request authorization
  immediately before enabling or publishing the public site.

## Verify before handoff

Run `scripts/validate_readme.py README.md --repo-root .` when Python is
available. Resolve its errors and review warnings. Also render or inspect visual
assets when possible, test the shortest documented install path, and verify that
each clickable demo destination is reachable in the intended public context.
