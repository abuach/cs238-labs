"""Week 3 · Part 1.2: letters the model can't see.

Run from this folder:  uv run letters.py
"""
from genai import ask, tokenize

for word, letter in [("strawberry", "r"), ("mississippi", "s"),
                     ("parallel", "l")]:
    reply = ask(f"How many times does the letter '{letter}' appear in "
                f"'{word}'? Reply with only the number.", max_tokens=10)
    print(f"{word:12} {tokenize(word)!s:30} model says {reply}")

print(ask("Spell the word 'tokenization' backward.", max_tokens=30))
