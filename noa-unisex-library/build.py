#!/usr/bin/env python3
"""Build noa-prompts.js for the Noa Unisex prompt library.

These prompts are hand-authored for the Noa Unisex brand, adapting the proven
techniques mined from this repo's collection (structured-JSON art direction,
layered lighting/material descriptors, {argument} templating, and negative
steering for cross-image consistency). All copy is English; no CJK text.

Brand kit baked into every default:
  palette   : terracotta, sun-faded ochre, olive, clay, warm sand, cream, oat,
              charcoal accents
  materials : organic cotton, washed linen, raw-edge denim, chunky knit,
              brushed canvas, natural leather
  mood      : warm, sunlit, organic, calm, inclusive, unisex, sustainable
  wordmark  : lowercase "noa", modern humanist sans, generous letter-spacing
  surfaces  : lime-plaster walls, travertine, raw clay, linen sweeps,
              Mediterranean daylight
"""
import json
import os

OUT = os.path.join(os.path.dirname(__file__), "noa-prompts.js")

# Shared brand tokens used inside prompt defaults.
PALETTE = "terracotta, sun-faded ochre, olive, warm sand, oat cream, clay"
NEG = ("strictly avoid: cool blue tones, neon colors, glossy plastic look, "
       "busy backgrounds, logos other than noa, distorted hands, warped text")

PROMPTS = [
    # ───────────────────────── E-commerce product ─────────────────────────
    {
        "category": "E-commerce Product",
        "title": "Ghost-Mannequin Invisible Apparel",
        "technique": "Structured JSON · catalog control",
        "description": "Clean invisible-mannequin PDP shot that shows garment shape with no model — the e-commerce main-image standard.",
        "aspect": "4:5",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "ghost mannequin (invisible mannequin) e-commerce product photo",
            "garment": "{argument name=\"garment\" default=\"oversized organic-cotton crewneck tee\"}",
            "color": "{argument name=\"garment color\" default=\"warm sand\"}",
            "presentation": "garment shaped as if worn by an invisible body, hollow neckline and cuffs visible, symmetrical, gently three-dimensional, no mannequin, no person",
            "background": "seamless oat-cream studio backdrop, soft floor gradient",
            "photography": {
                "composition": "centered, full garment in frame, generous negative space, straight-on eye level",
                "lighting": "large soft frontal softbox with subtle fill, gentle natural shadow under hem",
                "lens": "85mm look, true-to-life proportions, no distortion",
                "quality": "ultra-sharp fabric weave, accurate warm-neutral color, catalog-grade"
            },
            "brand": "discreet woven 'noa' label at inner collar",
            "negatives": NEG
        },
    },
    {
        "category": "E-commerce Product",
        "title": "Folded Flat-Lay on Washed Linen",
        "technique": "Structured JSON · top-down flat-lay",
        "description": "Top-down folded-garment flat-lay on natural linen for catalog grids and lookbook detail pages.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "top-down folded apparel flat-lay product photo",
            "subject": "{argument name=\"garment\" default=\"washed-linen overshirt\"}, crisply folded into a neat rectangle",
            "color": "{argument name=\"garment color\" default=\"terracotta\"}",
            "surface": "textured natural linen sweep in oat cream with soft visible weave",
            "props": "one sprig of dried olive branch, a folded care card, kept minimal at the corner",
            "photography": {
                "composition": "perfect 90° overhead, garment centered, balanced margins",
                "lighting": "soft directional daylight from upper-left, long gentle shadows, warm tone",
                "quality": "high detail on fabric texture and fold edges, true color"
            },
            "negatives": NEG
        },
    },
    {
        "category": "E-commerce Product",
        "title": "On-Model PDP — Neutral Studio",
        "technique": "Descriptor paragraph · on-model PDP",
        "description": "Full-length unisex on-model product shot, front-facing, for the primary PDP image.",
        "aspect": "4:5",
        "model": "nano_banana_pro",
        "prompt": "Full-length e-commerce product photograph of an androgynous unisex model standing relaxed and straight-on, wearing a {argument name=\"garment\" default=\"boxy organic-cotton shirt and wide-leg trousers\"} in {argument name=\"garment color\" default=\"olive and oat cream\"}. Calm neutral expression, hands at sides, natural unposed stance, diverse casting, minimal styling. Seamless warm oat-cream studio backdrop, soft even daylight-balanced lighting with a gentle floor shadow, true-to-life warm-neutral color. Sharp focus on garment fit, fabric drape and texture clearly visible, 85mm proportions with no distortion, catalog-grade clarity. Small woven 'noa' label visible at the chest. Strictly avoid: cool blue cast, heavy retouching, plastic skin, busy background, exaggerated poses.",
    },
    {
        "category": "E-commerce Product",
        "title": "Accessory Macro on Clay Pedestal",
        "technique": "Structured JSON · hero macro",
        "description": "Close hero shot of a small accessory on a sculptural clay riser — for accessory PDP and homepage tiles.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "macro hero product photo of a fashion accessory",
            "subject": "{argument name=\"accessory\" default=\"natural-leather card holder\"} in {argument name=\"color\" default=\"tan clay\"}",
            "staging": "resting on a small raw-clay pedestal, single subject, sculptural",
            "background": "lime-plaster wall in warm sand, soft gradient",
            "photography": {
                "composition": "tight three-quarter angle, subject fills two-thirds of frame, shallow depth of field",
                "lighting": "warm directional sunlight with soft hard-edged shadow, golden undertone",
                "quality": "macro detail on grain and stitching, tactile, true color"
            },
            "negatives": NEG
        },
    },
    {
        "category": "E-commerce Product",
        "title": "Knitwear Stack Hero",
        "technique": "Structured JSON · color-story stack",
        "description": "Neatly stacked folded knitwear in the brand palette — ideal for a category banner or color-story hero.",
        "aspect": "3:2",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "stacked folded knitwear product hero photo",
            "subject": "a tidy vertical stack of {argument name=\"count\" default=\"5\"} folded chunky-knit sweaters",
            "color story": "{argument name=\"color story\" default=\"terracotta, ochre, olive, oat, clay\"} from bottom to top",
            "surface": "travertine ledge, warm sand plaster wall behind",
            "photography": {
                "composition": "slight three-quarter angle on the stack, off-center with negative space for text",
                "lighting": "warm window daylight from the right, soft shadows, cozy",
                "quality": "rich knit texture, accurate warm palette, high resolution"
            },
            "negatives": NEG
        },
    },
    # ───────────────────────── Lookbook / editorial ───────────────────────
    {
        "category": "Lookbook / Editorial",
        "title": "Sunlit Warm-Earth Portrait",
        "technique": "Descriptor paragraph · campaign portrait",
        "description": "Signature campaign portrait — warm low sun, plaster wall, the hero editorial image of a drop.",
        "aspect": "4:5",
        "model": "soul_2",
        "prompt": "Editorial fashion campaign portrait of a unisex model with natural features and an effortless presence, photographed from the waist up against a warm lime-plaster wall in sun-faded terracotta. They wear a {argument name=\"outfit\" default=\"relaxed linen overshirt layered over a ribbed tank\"} in {argument name=\"palette\" default=\"olive and oat cream\"}. Late-afternoon golden sunlight rakes across the wall casting a soft long shadow, warm amber tones, gentle film grain, shallow depth of field, 50mm. Calm, confident, candid expression; natural skin texture; inclusive casting. Quiet-luxury earthy mood, organic and sustainable feel. Strictly avoid: cool tones, studio flash look, heavy makeup, plastic retouching, cluttered background.",
    },
    {
        "category": "Lookbook / Editorial",
        "title": "Unisex Duo Pairing",
        "technique": "Descriptor paragraph · multi-subject consistency",
        "description": "Two models styled as a coordinated unisex pair — shows range and the inclusive ethos in one frame.",
        "aspect": "3:2",
        "model": "nano_banana_pro",
        "prompt": "Editorial lookbook photograph of two diverse unisex models standing close together in coordinated but non-matching looks: one in a {argument name=\"look a\" default=\"boxy ochre canvas chore jacket and wide trousers\"}, the other in a {argument name=\"look b\" default=\"oversized oat knit and raw-edge denim\"}. Warm Mediterranean daylight, travertine courtyard with a plaster wall in warm sand, dried grasses in the corner. Natural relaxed poses, easy body language, candid connection. Warm golden color grade, soft shadows, 35mm wide editorial framing, film-like texture. Inclusive casting, calm confident mood. Strictly avoid: cool blue cast, harsh flash, stiff catalog poses, busy props, text.",
    },
    {
        "category": "Lookbook / Editorial",
        "title": "Mediterranean Outdoor Editorial",
        "technique": "Structured JSON · environment editorial",
        "description": "Full-scene outdoor editorial placing the garment in a sunlit earthy landscape — seasonal campaign key art.",
        "aspect": "3:2",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "outdoor fashion editorial environmental shot",
            "subject": "a unisex model walking unhurried through the scene wearing {argument name=\"outfit\" default=\"a flowing linen set in warm sand\"}",
            "environment": "{argument name=\"location\" default=\"sun-baked terracotta steps beside an olive grove\"}, dry warm landscape",
            "palette": PALETTE,
            "photography": {
                "composition": "wide environmental framing, model small-to-mid in frame, lots of warm negative space",
                "lighting": "golden-hour sun, long shadows, hazy warm atmosphere",
                "lens": "35mm, natural perspective",
                "quality": "editorial film look, fine grain, rich earthy color"
            },
            "negatives": NEG
        },
    },
    {
        "category": "Lookbook / Editorial",
        "title": "Movement & Drape Study",
        "technique": "Descriptor paragraph · motion",
        "description": "Captures fabric in motion to sell drape and flow — great for hero video stills and PDP secondary shots.",
        "aspect": "4:5",
        "model": "nano_banana_pro",
        "prompt": "Dynamic editorial photograph of a unisex model mid-movement, turning so the {argument name=\"garment\" default=\"wide linen trousers and unbuttoned overshirt\"} in {argument name=\"color\" default=\"terracotta and oat\"} catch the air and reveal their drape and flow. Warm sand studio sweep, single warm key light from the side creating a soft directional shadow, subtle motion blur on the fabric edges while the body stays sharp, golden tone, 70mm. Energetic yet calm, organic. Strictly avoid: frozen stiff pose, cool tones, harsh contrast, cluttered set.",
    },
    {
        "category": "Lookbook / Editorial",
        "title": "Fabric & Texture Macro",
        "technique": "Structured JSON · material storytelling",
        "description": "Extreme close-up celebrating natural fibers and craftsmanship — the sustainability/material story tile.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "extreme macro material detail photo",
            "subject": "the weave and seam of {argument name=\"material\" default=\"washed organic linen\"} in {argument name=\"color\" default=\"sun-faded ochre\"}, showing slub texture, topstitch, and a corozo button",
            "background": "out-of-focus same fabric, warm tone",
            "photography": {
                "composition": "tight macro, diagonal seam line, shallow depth of field",
                "lighting": "warm raking sidelight emphasizing texture relief",
                "quality": "tactile fiber detail, true natural color, premium craft feel"
            },
            "negatives": NEG
        },
    },
    # ──────────────────────────── Social media ────────────────────────────
    {
        "category": "Social Media",
        "title": "Drop Announcement Card",
        "technique": "Structured JSON · on-image typography",
        "description": "Square feed post announcing a new drop, with pixel-accurate headline typography in the brand voice.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "social media announcement post for a fashion brand",
            "layout": {
                "background": "warm sand lime-plaster texture, generous space",
                "hero": "a single {argument name=\"product\" default=\"folded terracotta linen set\"} placed lower-right with a soft shadow",
                "wordmark": "lowercase 'noa' top-left, modern humanist sans, wide letter-spacing",
                "headline": "{argument name=\"headline\" default=\"new arrivals\"}",
                "subhead": "{argument name=\"subhead\" default=\"the warm-earth edit · made to share\"}",
                "cta_chip": "{argument name=\"cta\" default=\"shop the drop\"}"
            },
            "typography": "clean modern sans, charcoal text on warm sand, crisp and perfectly legible, no spelling errors",
            "palette": PALETTE,
            "mood": "calm, premium, organic",
            "negatives": NEG
        },
    },
    {
        "category": "Social Media",
        "title": "Carousel Cover Tile",
        "technique": "Structured JSON · scroll-stopping cover",
        "description": "Slide-1 carousel cover that invites a swipe — bold but warm, with a clear hook.",
        "aspect": "4:5",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "instagram carousel cover slide",
            "layout": {
                "background": "split warm-earth color blocks in olive and oat",
                "headline": "{argument name=\"hook\" default=\"5 ways to wear one shirt\"}",
                "visual": "a unisex model in {argument name=\"garment\" default=\"an oat overshirt\"}, cut-out style on the color block",
                "swipe_cue": "small arrow + 'swipe' bottom-right",
                "wordmark": "'noa' small, bottom-left"
            },
            "typography": "large confident sans headline, charcoal, perfectly legible",
            "negatives": NEG
        },
    },
    {
        "category": "Social Media",
        "title": "Story / Reel Template (9:16)",
        "technique": "Structured JSON · vertical promo",
        "description": "Vertical story template for a sale or restock, with a tappable-feeling CTA and countdown space.",
        "aspect": "9:16",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "vertical instagram story promo template",
            "layout": {
                "background": "full-bleed warm terracotta gradient with subtle plaster grain",
                "top": "lowercase 'noa' wordmark, centered",
                "center_hero": "{argument name=\"product\" default=\"clay leather tote\"} floating with a soft shadow",
                "headline": "{argument name=\"headline\" default=\"the restock is here\"}",
                "detail_line": "{argument name=\"detail\" default=\"limited run · warm-earth essentials\"}",
                "cta_button": "rounded button reading '{argument name=\"cta\" default=\"tap to shop\"}' in oat cream"
            },
            "typography": "clean sans, high legibility, charcoal and cream, no typos",
            "negatives": NEG
        },
    },
    {
        "category": "Social Media",
        "title": "Product Trio Flat-Lay Post",
        "technique": "Structured JSON · grid-friendly flat-lay",
        "description": "Top-down trio styled for the feed with a short caption headline — keeps the grid cohesive.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "styled top-down flat-lay social post",
            "subject": "three coordinated items: {argument name=\"items\" default=\"a folded oat tee, tan leather card holder, ochre cap\"}",
            "surface": "warm linen and travertine, dried olive sprig accent",
            "text_overlay": "small headline '{argument name=\"headline\" default=\"everyday earth tones\"}' in charcoal sans, lower third",
            "photography": {
                "composition": "90° overhead, balanced triangular arrangement, space for text",
                "lighting": "soft warm daylight, gentle shadows",
                "quality": "crisp, tactile, true warm color"
            },
            "negatives": NEG
        },
    },
    # ──────────────────────────── Brand & packaging ───────────────────────
    {
        "category": "Brand & Packaging",
        "title": "Wordmark Lockup on Plaster",
        "technique": "Structured JSON · logo lockup",
        "description": "Hero brand wordmark composition for headers, about pages, and profile banners.",
        "aspect": "3:2",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "minimal brand wordmark hero composition",
            "wordmark": "lowercase 'noa' set large and centered in a modern humanist sans with wide tracking",
            "treatment": "{argument name=\"treatment\" default=\"debossed into warm sand lime-plaster\"}, subtle dimensional shadow",
            "tagline": "{argument name=\"tagline\" default=\"unisex essentials in warm earth\"}, small, below the wordmark",
            "background": "warm plaster texture, golden directional light",
            "palette": PALETTE,
            "typography": "perfectly clean letterforms, accurate spacing, no artifacts",
            "negatives": NEG
        },
    },
    {
        "category": "Brand & Packaging",
        "title": "Hang Tag & Care Label",
        "technique": "Structured JSON · physical collateral",
        "description": "Recycled-card hang tag plus woven care label mockup — the touchpoints that signal craft and sustainability.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "product collateral mockup — hang tag and care label",
            "items": {
                "hang_tag": "rectangular recycled kraft card with lowercase 'noa' wordmark, '{argument name=\"tagline\" default=\"made warm, made to last\"}', and a small olive-branch icon, jute string threaded through a brass eyelet",
                "care_label": "woven cotton care label in oat with charcoal text reading '100% organic cotton'"
            },
            "staging": "resting on washed linen in warm sand, top-down, soft daylight",
            "photography": {"composition": "overhead, two items balanced, negative space", "quality": "tactile paper and weave detail, true color"},
            "typography": "crisp legible sans, no spelling errors",
            "negatives": NEG
        },
    },
    {
        "category": "Brand & Packaging",
        "title": "Mailer Box & Tissue Mockup",
        "technique": "Structured JSON · unboxing mockup",
        "description": "Sustainable mailer and tissue unboxing scene — the shareable first-impression moment.",
        "aspect": "4:5",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "sustainable packaging unboxing mockup",
            "subject": "an open recycled-cardboard mailer box in warm kraft tone, lowercase 'noa' printed on the lid, garment wrapped in oat tissue with a terracotta paper sticker reading '{argument name=\"sticker\" default=\"hello, noa\"}'",
            "contents": "a glimpse of {argument name=\"garment\" default=\"folded ochre linen\"} inside",
            "staging": "on a travertine surface, dried grass sprig beside it, warm daylight",
            "photography": {"composition": "three-quarter top angle, inviting, negative space upper area", "lighting": "soft warm window light", "quality": "premium tactile detail, true earthy color"},
            "negatives": NEG
        },
    },
    {
        "category": "Brand & Packaging",
        "title": "Brand Avatar Mark",
        "technique": "Structured JSON · profile mark",
        "description": "Clean circular profile/avatar mark for social and app — instantly recognizable at small sizes.",
        "aspect": "1:1",
        "model": "nano_banana_pro",
        "prompt": {
            "type": "circular brand avatar / profile mark",
            "design": "lowercase 'noa' monogram centered, modern humanist sans, on a {argument name=\"bg\" default=\"warm terracotta\"} circle",
            "accent": "a tiny minimalist olive-leaf glyph above the wordmark",
            "treatment": "flat, high-contrast for legibility at 64px, subtle warm grain",
            "typography": "perfect letterforms, balanced spacing",
            "negatives": NEG
        },
    },
]


def main():
    records = []
    for i, p in enumerate(PROMPTS):
        prompt = p["prompt"]
        prompt_str = (json.dumps(prompt, ensure_ascii=False, indent=2)
                      if isinstance(prompt, dict) else prompt)
        # collect {argument name="X" default="Y"} placeholders for the UI.
        # JSON serialization escapes inner quotes, so unescape before matching.
        import re
        search_src = prompt_str.replace('\\"', '"')
        args = re.findall(r'\{argument name="([^"]+)" default="([^"]*)"\}', search_src)
        records.append({
            "id": i,
            "category": p["category"],
            "title": p["title"],
            "technique": p["technique"],
            "description": p["description"],
            "aspect": p["aspect"],
            "model": p["model"],
            "prompt": prompt_str,
            "args": [{"name": a, "default": d} for a, d in args],
        })

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by build.py — hand-authored Noa Unisex prompts.\n")
        f.write("window.NOA_PROMPTS = " + json.dumps(records, ensure_ascii=False, indent=1) + ";\n")
    print(f"Wrote {len(records)} Noa prompts to {OUT}")
    cats = {}
    for r in records:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    for c, n in cats.items():
        print(f"  {c}: {n}")


if __name__ == "__main__":
    main()
