"""Basic text statistics."""

import re


def char_count(text):
    return len(text)


def word_count(text):
    return len(text.split())


def sentence_count(text):
    return len(re.findall(r"[.!?]+", text))


def average_word_length(text):
    words = text.split()
    total_chars = sum(len(w) for w in words)
    return total_chars / len(words)
