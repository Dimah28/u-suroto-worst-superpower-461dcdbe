"""Worst Superpower -- make.fun bounty u-suroto-worst-superpower-461dcdbe.

Writes one line (107 characters, inside the 140-character gate)
inventing the most useless superpower to /output/entry.txt.

The power: teleport any sock in the world -- but only the left one,
and only into the dryer it already came from. Teleportation is a great
power made perfectly pointless: the sock ends up exactly where it
started, so the power achieves net zero. One vivid picture (a sock
vanishing, then reappearing in its own dryer), three concrete details
(left sock, dryer, already came from), no familiar gag (no slow
flight, no invisibility-when-unwatched).

Rejected drafts:
- B (98 chars): hear pigeons' thoughts, Tuesdays only, pigeons think
  only of crumbs. Weaker: mind-reading is a real power, only the
  target is dumb; the "Tuesdays" limiter is arbitrary, not earned.
- C (96 chars): turn traffic lights green three seconds after
  crossing. Strong picture, but the "too late" trope is familiar and
  the light turning green still quietly helps whoever is behind you.
- D (90 chars): know any cloud's exact weight in kilograms. Useless,
  but no picture of the power in use -- no joke lands.
"""

import os
import sys

ENTRY = (
    "I can teleport any sock in the world \u2014 but only the left one, "
    "and only into the dryer it already came from."
)

MAX_CHARS = 140


def validate_entry(text: str) -> str:
    """Gate check (competition rules): UTF-8, 1-140 chars, one line."""
    assert isinstance(text, str) and text, "entry must be a non-empty string"
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        "entry is %d chars, gate is 1-%d" % (len(text), MAX_CHARS)
    )
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")  # gate: must be valid UTF-8
    return text


def summarize(text: str) -> str:
    """One-line summary of the entry for the run log (stdout stays clean)."""
    return "entry: %d chars, %d bytes, %d words, 1 line" % (
        len(text),
        len(text.encode("utf-8")),
        len(text.split()),
    )


def main() -> int:
    text = validate_entry(ENTRY)
    print(summarize(text), file=sys.stderr)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
