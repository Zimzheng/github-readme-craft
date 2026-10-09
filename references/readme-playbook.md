# GitHub README playbook

Use this reference after the user has chosen the README languages and the
repository has been inspected.

## 1. Information architecture

A README is a landing page and an operational starting point. Choose sections
based on evidence in the repository instead of mechanically filling a template.

| Reader question | Suitable README element |
|---|---|
| What is this? | Name and concrete one-sentence description |
| Why would I use it? | Three to five outcome-oriented capabilities |
| What does it look like? | Screenshot, GIF, terminal recording, diagram, or labeled mockup |
| Can I try it now? | Shortest verified install and run commands |
| How does it fit my work? | Brief usage example, architecture note, or linked demo |
| Where do I go next? | Documentation, examples, issue tracker, contribution and license links |

Put the first three answers above the fold. Use a table of contents only when
the document is long enough to make scanning difficult.

## 2. Visual demo patterns

### Static product or report preview

Store a stable asset under `assets/`, `docs/assets/`, or `screenshots/`. Use
descriptive alt text and a relative path:

```md
[![Report preview](assets/report-preview.svg)](https://example.github.io/project/demo.html)
```

The image is clickable; the destination should be a live demo, a verified HTML
preview, or a source-file page clearly labeled as such. GitHub Markdown does
not safely embed arbitrary interactive HTML, so do not promise inline
interactivity inside a README.

### Interaction explanation

Use a secondary diagram or caption to explain a behavior a static screenshot
cannot show: anchors, filtering, responsive layout, print rules, or an
authorization flow. Keep it subordinate to the primary product preview.

### Example safety

Prefer a synthetic scenario. Mark it “示例”, “演示”, or “fictional” wherever a
reader could interpret it as a real customer, metric, source, or deployment.

## 3. Installation and usage

Give the shortest working command first. Show each command in its own runnable
block and include path creation when the destination may not exist:

```bash
mkdir -p ~/.example/skills
git clone https://github.com/owner/project.git ~/.example/skills/project
```

Do not use `<repository-url>`, invented versions, or generic placeholders when
the user wants copyable installation instructions. For several hosts, present a
small table followed by host-specific complete commands. Distinguish “install”
from “clone source to contribute”.

## 4. Language variants

Ask for this before drafting. Use the requested primary language in `README.md`.
When optional variants are requested, make each a maintained peer document:

```md
[简体中文](README.md) | [English](README.en.md)
```

Do not create an unrequested translation or add a language switcher that points
to nonexistent files.

## 5. Release checklist

- Claims, commands, links, package names, and asset paths match the repository.
- Previews have useful alt text and their links have a verified destination.
- Sample content has no customer data, local paths, account identifiers, tokens,
  private research, or screenshots with sensitive text.
- The README separates facts, examples, and future plans.
- The staging diff contains only intended documentation and asset files.
- Remote publishing, hosted demos, repository creation, and Pages settings have
  direct user authorization.

## Sources informing these conventions

- GitHub Docs, “Basic writing and formatting syntax”: relative links and image
  paths remain portable across repository branches and clones.
- banesullivan/README: use concise demos and simple installation as a landing
  page, with deeper material moved into documentation.
- usman-idris/readme-examples: screenshots, GIFs, clear descriptions, demos and
  short installation paths are recurring characteristics of effective READMEs.
