# 🍌 GPT Image 2 Prompt Library (standalone page)

A self-contained, browsable HTML library of the prompts in this repo's
`README.md`. Live search, category filtering, one-click copy, image previews,
and "Try it" links — no build tooling or server required.

## Open it

```bash
# from the repo root
python3 prompt-library/build.py      # (re)generate prompts.js from README.md
```

Then open `prompt-library/index.html` in any browser (double-click works —
data is bundled as `prompts.js`, so no web server is needed).

## Files

| File | Purpose |
|------|---------|
| `index.html` | The library UI (search, filter, copy, lightbox). |
| `prompts.js` | Auto-generated data (`window.PROMPTS`). **Do not edit by hand.** |
| `build.py` | Parses `README.md` → `prompts.js`. Pass a filename to use a localized README, e.g. `python3 prompt-library/build.py README_zh.md`. |

## Refreshing

`README.md` is regenerated from the CMS (`pnpm generate`). After it changes,
re-run `python3 prompt-library/build.py` to update the library.
