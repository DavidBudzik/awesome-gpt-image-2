# noa — Unisex Prompt Library

A custom, tailor-made GPT Image 2 prompt library for the **Noa Unisex** brand.
All copy is **English** (no CJK text), tuned to a **warm-earth** aesthetic, and
covers the brand's four image use cases. Open `index.html` in any browser — the
data is bundled in `noa-prompts.js`, so no server is needed.

## Brand kit (baked into every prompt default)

| Token | Values |
|-------|--------|
| Palette | terracotta · sun-faded ochre · olive · clay · warm sand · oat cream |
| Materials | organic cotton · washed linen · raw-edge denim · chunky knit · brushed canvas · natural leather |
| Mood | warm, sunlit, organic, calm, inclusive, unisex, sustainable |
| Wordmark | lowercase **noa**, modern humanist sans, wide letter-spacing |
| Surfaces | lime-plaster, travertine, raw clay, linen, Mediterranean daylight |

## What I analyzed (techniques from the source collection)

Reviewing the repo's top Product Marketing, E-commerce, Social and editorial
prompts surfaced five reusable techniques, each applied here:

1. **Structured-JSON art direction** — explicit `type / scene / subject /
   photography{composition,lens,lighting,quality} / background` keys give
   repeatable, controllable results. Used for all product, packaging, and
   social-layout prompts.
2. **Layered descriptor paragraphs** — dense lighting + material + mood language
   for editorial/on-model shots where natural phrasing reads better than JSON.
3. **`{argument name="…" default="…"}` templating** — every prompt is a reusable
   template; swap product, color, headline, etc. without rewriting.
4. **Negative steering** — a shared "strictly avoid…" clause locks the look
   (kills cool tones, plastic sheen, busy sets) so a whole drop stays on-brand.
5. **Quoted on-image copy** — exact headline/label text in quotes leverages GPT
   Image 2's pixel-accurate text rendering for social cards and packaging.

## Library contents (18 prompts)

- **E-commerce Product (5):** ghost-mannequin, linen flat-lay, on-model PDP,
  accessory macro, knitwear color-stack.
- **Lookbook / Editorial (5):** sunlit portrait, unisex duo, Mediterranean
  environment, movement/drape study, fabric texture macro.
- **Social Media (4):** drop card, carousel cover, story/reel template,
  product-trio flat-lay.
- **Brand & Packaging (4):** wordmark lockup, hang tag + care label, mailer
  unboxing, avatar mark.

## Using the page

- **Customize variables** — each card exposes its `{argument}` fields as inputs;
  edit them and the prompt preview updates live.
- **Copy resolved prompt** — copies the prompt with your values filled in (paste
  straight into GPT Image 2 / Nano Banana Pro).
- **Copy with {args}** — copies the template form (placeholders intact) for
  reuse in Raycast or another templating flow.
- Each card notes a suggested **aspect ratio** and **model** (`nano_banana_pro`
  for product/text/packaging, `soul_2` for on-model editorial).

## Files

| File | Purpose |
|------|---------|
| `index.html` | The warm-earth library UI. |
| `noa-prompts.js` | Auto-generated data (`window.NOA_PROMPTS`). Do not edit by hand. |
| `build.py` | Holds the hand-authored prompts and emits `noa-prompts.js`. Edit here to add/adjust prompts, then re-run it. |
