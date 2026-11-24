"""Funniest one-line bio for an AI on a dating app.

Writes a single bio line to /output/entry.txt.
Pure stdlib, deterministic, no network.

The bio: an AI with perfect memory that still cannot decode the
most dreaded dating text, "we need to talk". Power, then a narrow
specific limit, with the punch ("dinner or doom") landing last.
"""

from pathlib import Path

BIO = (
    "I can remember everything you've ever said, "
    "but I still can't tell if 'we need to talk' means dinner or doom."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the one bio line.
    output_path.write_text(BIO, encoding="utf-8")


if __name__ == "__main__":
    main()
