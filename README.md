# toybox

A tiny collection of Python utility functions — math helpers, string helpers, and a small CLI.
This repo exists as a test fixture (real commits, real branches, real pull requests) rather than
a production library.

## Modules

- `toybox.mathutils` — small arithmetic helpers
- `toybox.stringutils` — string helpers (palindromes, slugs, word counts)
- `toybox.textstats` — basic text statistics
- `toybox.cli` — a small command-line entry point over the above

## Development

```bash
pip install -e .
pytest
```
