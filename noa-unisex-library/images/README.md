# Noa preview images

Drop the generated card previews here. Each card looks for an exact filename —
see `../IMAGES.md` (human-readable checklist + per-image prompts) or
`../image-manifest.json` (machine-readable) for the full mapping.

- **18 images**, one per card.
- Filenames are fixed, e.g. `01-ghost-mannequin-invisible-apparel.webp`.
- Preferred format: **`.webp`** (smaller). To use `.png`/`.jpg` instead, change
  `IMG_EXT` in `../build.py` and re-run it, or just rename your files to `.webp`.
- Respect each card's **aspect ratio** (listed in the checklist) so previews
  aren't cropped.
- Until a file exists, the card shows a dashed "preview pending" placeholder —
  no broken images.
