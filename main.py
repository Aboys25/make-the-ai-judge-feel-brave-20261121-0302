"""make-the-ai-judge-feel-brave-20261121-0302 entry.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, no network, fully deterministic.
"""

import os

TEXT = (
    "The kettle has boiled and gone quiet. Steam thins in the kitchen "
    "light, and nothing is asked of it. It ticks softly as it cools, "
    "warm on the stove, a held breath loosening on its own, unasked."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
