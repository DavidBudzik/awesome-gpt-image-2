---
name: gpt-image-2-prompts
description: >-
  Discover, adapt, and author high-quality GPT Image 2 prompts from this repo's
  curated collection (5000+ prompts across categories like avatar, infographic,
  poster, product marketing, comic, app/web design). Use when the user wants an
  image-generation prompt, asks to find or remix an existing prompt, wants help
  writing a new GPT Image 2 prompt, or is preparing a prompt submission for this
  repository.
---

# GPT Image 2 Prompts

This repository (`awesome-gpt-image-2`) is a curated collection of prompts for
OpenAI's **GPT Image 2** model. The prompts live in the generated `README.md`
(English) and the localized `README_*.md` files. This skill helps you mine that
collection, remix prompts, and author new ones that match the project's
conventions.

## When to use this skill

- The user wants a prompt to generate a specific kind of image (avatar, poster,
  infographic, product shot, comic panel, YouTube thumbnail, app/web mockup…).
- The user wants to **find** an existing prompt by topic, style, or category.
- The user wants to **remix/adapt** an existing prompt for a new subject.
- The user wants help **authoring a new prompt** to submit to this repo.

## How prompts are stored

`README.md` is generated from a CMS — do not hand-edit it (run `pnpm generate`
to regenerate; see `scripts/generate-readme.ts`). Each prompt is a block:

```
### No. <N>: <Category> - <Title>

![Language-EN] ![Featured?] ![Raycast?]

#### 📖 Description
<one-line description>

#### 📝 Prompt
```​
<the prompt — often a JSON object>
```​

#### 🖼️ Generated Images
<image URLs>

#### 📌 Details
- **Author:** ...
- **Source:** ...
- **Languages:** ...
**[👉 Try it now →](https://youmind.com/gpt-image-2-prompts?id=<id>)**
```

Two sections exist: **🔥 Featured Prompts** (hand-picked) and **📋 All Prompts**
(everything, with the category embedded in the heading).

## Finding a prompt (do this first)

Don't scan the whole README — it's large. Use the helper script:

```bash
python3 .claude/skills/gpt-image-2-prompts/scripts/search_prompts.py "<query>"
```

- `<query>` matches against the title, category, and description (case-insensitive).
- `--category "Poster / Flyer"` restricts to a category.
- `--full` prints the complete prompt text for each match (default shows a preview).
- `--limit N` caps results (default 10).
- `--file README_zh.md` searches a localized file instead of `README.md`.

Example: `python3 .../search_prompts.py "infographic" --category "Infographic / Edu Visual" --full --limit 3`

## Prompt conventions to follow

GPT Image 2 prompts in this collection favor a **structured, declarative**
style. Two common shapes:

1. **JSON object** — explicit keys like `type`, `subject`, `style`,
   `background`, `layout`, `header`, `footer`, `callout_labels`, `color_palette`,
   `aspect_ratio`. This gives the model precise, repeatable control and is the
   dominant format for posters, infographics, and product diagrams.
2. **Rich natural-language paragraph** — a single descriptive paragraph for
   illustration/photography styles.

GPT Image 2's strengths to lean into when writing prompts:

- 🎯 Pixel-perfect multilingual **text rendering** (EN/CN/JP) — put exact copy in
  quotes; specify language when it matters.
- 🎨 **Cross-image consistency** — reuse the same subject/style description for a
  series (storyboards, IP characters, product lines).
- 📐 **Layout/typography control** — name regions (header, footer, callouts) and
  give counts.

### Raycast dynamic arguments

Prompts marked 🚀 *Raycast Friendly* use [Raycast Snippet](https://raycast.com/help/snippets)
argument syntax so values can be swapped at use time:

```
{argument name="product name" default="Meta Quest 3"}
```

When **authoring** a reusable prompt, parameterize the parts a user would change
(subject, brand, headline, colors) with this syntax. When **using** a prompt for
a concrete image, replace the `{argument ...}` placeholders with real values
before sending it to the model.

## Authoring / remixing workflow

1. Search for the 1–3 closest existing prompts and read them with `--full`.
2. Pick the format (JSON vs. paragraph) that matches the target use case.
3. Write the prompt: keep exact on-image text in quotes, name layout regions,
   specify style + background + aspect ratio, and parameterize variable parts
   with Raycast argument syntax if it should be reusable.
4. Present the prompt to the user in a copyable code block, and note which
   `{argument ...}` values they should customize.

## Generating an image (optional)

If an image-generation tool is available in the session (an MCP `generate_image`
tool), you may offer to generate a preview from the crafted prompt — replacing
any `{argument ...}` placeholders with concrete values first. Confirm with the
user before generating, since generation may incur cost.

## Submitting a prompt to this repo

New prompts are contributed via a GitHub issue, not by editing the README. Use
the **🍌 Submit a Prompt** issue template (`.github/ISSUE_TEMPLATE/submit-prompt.yml`):
it requires title, prompt text, description, generated image URLs, author,
source link, and language. Content is licensed CC BY 4.0. See
`docs/CONTRIBUTING.md` for the full flow.
