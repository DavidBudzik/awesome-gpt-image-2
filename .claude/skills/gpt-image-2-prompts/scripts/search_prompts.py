#!/usr/bin/env python3
"""Search the awesome-gpt-image-2 prompt collection.

Parses a generated README (default: README.md) into prompt blocks and filters
them by a free-text query and/or category. Prints title, category, description,
the "Try it now" link, and (with --full) the complete prompt text.

Usage:
    search_prompts.py "<query>" [--category NAME] [--full] [--limit N] [--file README.md]

Examples:
    search_prompts.py "infographic"
    search_prompts.py "poster" --category "Poster / Flyer" --full --limit 3
    search_prompts.py "" --category "Profile / Avatar" --limit 5
"""
import argparse
import os
import re
import sys

# A prompt block starts at "### No. N: ..." and runs until the next one.
BLOCK_RE = re.compile(r"^### No\. \d+: (.+?)\s*$", re.MULTILINE)


def repo_root():
    # scripts/ -> skill dir -> skills -> .claude -> repo root
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(here, "..", "..", "..", ".."))


def parse_blocks(text):
    """Yield dicts for each prompt block in the README text."""
    matches = list(BLOCK_RE.finditer(text))
    for i, m in enumerate(matches):
        heading = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]

        # Heading is "Category - Title" in All Prompts; just a title in Featured.
        if " - " in heading:
            category, title = heading.split(" - ", 1)
        else:
            category, title = "", heading

        desc = _section(body, "📖 Description")
        prompt = _code_block_after(body, "📝 Prompt")
        link_m = re.search(r"\((https://youmind\.com/[^)]+)\)", body)
        link = link_m.group(1) if link_m else ""

        yield {
            "category": category.strip(),
            "title": title.strip(),
            "description": (desc or "").strip(),
            "prompt": (prompt or "").strip(),
            "link": link,
        }


def _section(body, header):
    m = re.search(
        r"####\s*" + re.escape(header) + r"\s*\n(.*?)(?:\n#### |\Z)",
        body,
        re.DOTALL,
    )
    return m.group(1).strip() if m else ""


def _code_block_after(body, header):
    sec = re.search(
        r"####\s*" + re.escape(header) + r"\s*\n(.*?)(?:\n#### |\Z)",
        body,
        re.DOTALL,
    )
    if not sec:
        return ""
    fence = re.search(r"```[a-zA-Z]*\n(.*?)```", sec.group(1), re.DOTALL)
    return fence.group(1) if fence else sec.group(1)


def main():
    ap = argparse.ArgumentParser(description="Search GPT Image 2 prompts.")
    ap.add_argument("query", nargs="?", default="",
                    help="text matched against title/category/description")
    ap.add_argument("--category", default="", help="restrict to a category")
    ap.add_argument("--full", action="store_true",
                    help="print the complete prompt text")
    ap.add_argument("--limit", type=int, default=10, help="max results")
    ap.add_argument("--file", default="README.md", help="README file to search")
    args = ap.parse_args()

    path = args.file if os.path.isabs(args.file) else os.path.join(repo_root(), args.file)
    if not os.path.exists(path):
        sys.exit(f"File not found: {path}")

    with open(path, encoding="utf-8") as f:
        text = f.read()

    q = args.query.lower()
    cat = args.category.lower()
    results = []
    for b in parse_blocks(text):
        hay = f"{b['title']} {b['category']} {b['description']}".lower()
        if q and q not in hay:
            continue
        if cat and cat not in b["category"].lower():
            continue
        results.append(b)

    total = len(results)
    shown = results[: args.limit]
    if not shown:
        print("No matching prompts found.")
        return

    for b in shown:
        cat_str = f"[{b['category']}] " if b["category"] else ""
        print(f"\n### {cat_str}{b['title']}")
        if b["description"]:
            print(f"  {b['description']}")
        if b["link"]:
            print(f"  Try it: {b['link']}")
        if args.full and b["prompt"]:
            print("  --- prompt ---")
            for line in b["prompt"].splitlines():
                print(f"  {line}")
        elif b["prompt"]:
            preview = b["prompt"].replace("\n", " ")[:160]
            print(f"  prompt: {preview}{'…' if len(b['prompt']) > 160 else ''}")

    print(f"\nShowing {len(shown)} of {total} match(es).")


if __name__ == "__main__":
    main()
