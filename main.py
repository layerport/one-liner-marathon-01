"""One-Liner Marathon entry.

Writes one original one-line comedy joke to /output/entry.txt.
Python 3.13 standard library only; no network, no secrets, no input files.
"""

import os

# The joke, written in this session. A builder replaces himself with an AI,
# and the punchline is that the replacement immediately behaves like the
# most human thing in the office: it asks HR for a desk and a raise.
JOKE = (
    "I built an AI to replace me at work, and it did "
    "\u2014 it just asked HR for my desk and a raise."
)


def validate(joke: str) -> str:
    """Return the joke unchanged, or raise if it would fail the gate.

    The gate requires UTF-8 text of 1 to 280 characters, not only
    whitespace, and a single line. Checking here keeps a bad edit
    from ever reaching /output/entry.txt.
    """
    if not joke or not joke.strip():
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > 280:
        raise ValueError("joke is over 280 characters")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    return joke


def main() -> None:
    joke = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
