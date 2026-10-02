"""Week 3 · Task 1: your own strings (the chapter's Exercise 1).

Put your own name, a long technical term from your major, a common English
word, and an emoji on the marked lines. Guess first, then run:
    uv run my_tokens.py
"""
from genai import count_tokens, tokenize

mine = [
    "Chiké",                       # ← your name
    "photosynthesis",              # ← a long term from your major
    "house",                       # ← a common English word
    "🎸",                          # ← an emoji
]
for s in mine:
    print(f"{s:30} {count_tokens(s):2} tokens -> {tokenize(s)}")
