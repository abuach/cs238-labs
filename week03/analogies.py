"""Week 3 · Part 2.3: word arithmetic, and where it breaks.

Run from this folder:  uv run analogies.py
"""
from genai import word_analogy
from genai.embed import show_opposite_cosines

def check(a, b, c, candidates):
    got, score = word_analogy(a, b, c, candidates)
    print(f"{a} - {b} + {c} = {got} ({score:.2f})")

check("king", "man", "woman", ["queen", "prince", "princess", "duke"])
# we want the opposite of "rich" here
check("happy", "sad", "rich", ["poor", "wealthy", "money", "broke"])

print()
show_opposite_cosines()
