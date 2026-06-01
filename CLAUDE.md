# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not an application** — it is a **content pipeline** that renders a curated collection of GPT Image 2 prompts into localized README files. The source of truth lives in an **external Payload CMS** (not in this repo). The `README.md` and all `README_*.md` files are **generated artifacts** committed back to the repo by CI.

**Do not hand-edit `README*.md`** — those changes are overwritten by the scheduled `update-readme` workflow (runs twice daily). To change README content, change the data in the CMS (or the generator/i18n code), then regenerate.

## Commands

```bash
pnpm install                  # Node 20+, pnpm 9 (packageManager pinned)
pnpm run generate             # CMS → regenerate all README*.md  (scripts/generate-readme.ts)
pnpm run sync                 # Parse a GitHub issue → create/update a CMS prompt (local testing)
```

Both scripts run via `tsx` (no build step; `dist/` and the `tsc` config exist but CI runs sources directly with `npx tsx`). There is **no test suite and no linter** configured — don't look for `pnpm test`/`pnpm lint`.

Required env (via `.env`, auto-loaded by `dotenv/config`):
- `CMS_HOST`, `CMS_API_KEY` — needed by **both** scripts.
- `pnpm run sync` additionally needs `GITHUB_TOKEN`, `GITHUB_REPOSITORY`, `ISSUE_NUMBER`, `ISSUE_BODY` (in CI these come from the issue event; locally set them inline, e.g. `ISSUE_NUMBER=123 pnpm run sync`).

## Architecture

Two entrypoints in `scripts/`, sharing helpers in `scripts/utils/`:

**1. README generation (`generate-readme.ts`)** — for each of the 16 locales in `SUPPORTED_LANGUAGES` (`markdown-generator.ts`):
- `fetchPromptCategories(locale)` → categories (filtered to campaign `gpt-image-2-prompts`).
- `fetchAllPrompts(locale, categories)` → combines `fetchFeaturedPrompts` (featured, limit 30) with `fetchPromptsByCategory` for each `use-cases` child category (limit 20 each), **deduping by prompt id**. Category prompts get their title prefixed with the category title.
- `sortPrompts` splits featured/regular; `generateMarkdown` renders the localized file. Regular prompts shown are capped at `MAX_REGULAR_PROMPTS_TO_DISPLAY` (120).
- All CMS queries filter on `model == "gpt-image-2"`. Prompts with **no images** (`sourceMedia` empty after `processPromptImages`) are dropped.

**2. Issue → CMS sync (`sync-approved-to-cms.ts`)** — the contribution path:
- Triggered by `sync-approved-to-cms.yml` when an `approved` label is added to an issue that already has `prompt-submission`.
- `parseIssue` turns the issue-form body into fields by lowercasing `### ` headings and replacing spaces with `_`; `FIELD_NAME_MAP` reconciles the label-derived names (e.g. `generated_image_urls` → `image_urls`) and `LANGUAGE_MAP` maps display language → locale code.
- Images are re-hosted via `image-uploader.ts` (`uploadImageToCMS`), then `createPrompt`/`updatePrompt` writes to the CMS. **Idempotency** is by `sourceMeta.github_issue` (`findPromptByGitHubIssue`) — re-approving updates the same prompt rather than duplicating. The issue is then closed.

**The full loop:** contributor opens a *Submit a Prompt* issue (`.github/ISSUE_TEMPLATE/submit-prompt.yml`) → maintainer adds `approved` → sync workflow writes to CMS → the twice-daily `update-readme` cron regenerates and commits `README*.md` to `main` with `[skip ci]` (uses a rebase-retry loop to survive concurrent pushes).

### Key files
- `scripts/utils/cms-client.ts` — all CMS REST access, the `Prompt`/category types, fetch/sort/dedup logic.
- `scripts/utils/markdown-generator.ts` — `SUPPORTED_LANGUAGES`, per-locale README rendering, gallery URL building (`getLocalePrefix`).
- `scripts/utils/i18n.ts` — large translation table powering localized output (`t()`).
- `scripts/utils/image-uploader.ts` — uploads source image URLs into the CMS media library.

## Conventions & gotchas

- **TypeScript ESM**: `"type": "module"`, target ES2022. Source files import local modules with explicit **`.js` extensions** (e.g. `from './utils/cms-client.js'`) even though the files are `.ts` — keep this when adding imports.
- **Adding a language** requires both a new entry in `SUPPORTED_LANGUAGES` and matching translations in `i18n.ts`; the CMS fetch passes the locale through for translated content.
- CI pins **pnpm 9 / Node 20** and installs with `--frozen-lockfile`; keep `pnpm-lock.yaml` in sync.
- `CMS_HOST` must have **no trailing slash** (a common 401/404 cause).

## Auxiliary tooling (not part of the CMS pipeline)

These are standalone additions and do not feed the README generator:
- `.claude/skills/gpt-image-2-prompts/` — a Claude Code skill for discovering/remixing prompts from the generated READMEs (`scripts/search_prompts.py`).
- `prompt-library/` and `noa-unisex-library/` — self-contained static HTML prompt browsers, each with a Python `build.py` that emits a `*.js` data file. They are plain `python3 build.py` + open `index.html`; no Node involvement.
