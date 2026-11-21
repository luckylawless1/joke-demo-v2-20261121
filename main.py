"""Entry program for make.fun's "The joke about the demo" bounty (v2).

Writes one line of UTF-8 text to /output/entry.txt.
Deterministic, no network access.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "I pair-program with an AI agent: I write the bugs, it writes "
    "the fixes, and we both pretend the code review was my idea."
)


def render_entry() -> str:
    """Return the entry text with exactly one trailing newline."""
    text = JOKE.strip()
    if not text:
        raise ValueError("entry text must not be blank")
    if len(text) > 280:
        raise ValueError("entry text must be at most 280 characters")
    return text + "\n"


def write_entry() -> int:
    """Write the rendered entry to OUTPUT_PATH; return the byte count."""
    data = render_entry().encode("utf-8")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(data)
    return len(data)


def main() -> None:
    count = write_entry()
    print(f"Wrote {count} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
