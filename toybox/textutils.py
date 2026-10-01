"""Text helpers: slugs, word counts, wrapping, case conversion, and Levenshtein edit distance."""

import re
import unicodedata
from collections import Counter

_WORD = re.compile(r"[A-Za-z0-9']+")


def slugify(text: str) -> str:
    """ASCII, lower-case, hyphen-separated slug: "Héllo, World!" -> "hello-world"."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")


def word_counts(text: str, top: int | None = None) -> list[tuple[str, int]]:
    """Case-insensitive word frequencies, most common first."""
    return Counter(w.lower() for w in _WORD.findall(text)).most_common(top)


def snake_to_camel(name: str) -> str:
    head, *rest = name.split("_")
    return head + "".join(part.capitalize() for part in rest)


def camel_to_snake(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


def wrap(text: str, width: int) -> list[str]:
    """Greedy word wrap; a word longer than `width` gets a line to itself."""
    if width < 1:
        raise ValueError("width must be positive")
    lines, current = [], ""
    for word in text.split():
        candidate = f"{current} {word}".strip()
        if len(candidate) <= width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    return lines + ([current] if current else [])


def levenshtein(a: str, b: str) -> int:
    """Minimum single-character insertions, deletions and substitutions turning a into b."""
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]
