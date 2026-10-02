"""Week 3 · Part 1.1: what's a token?

A token is a chunk, not a word. Watch where the splits fall.
Run from this folder:  uv run tokens.py
"""
from genai import count_tokens, tokenize

for s in ["cat", "tokenization", "antidisestablishmentarianism",
          "🍓", "café"]:
    print(f"{s:30} {count_tokens(s):2} tokens -> {tokenize(s)}")
