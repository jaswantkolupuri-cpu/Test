"""Small string helpers."""

import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def word_count(text):
    return len(text.split())


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug
