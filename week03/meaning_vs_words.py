"""Week 3 · Part 2.2: meaning versus word overlap (the chapter's Exercise 1).

Predict each score before you run it:  uv run meaning_vs_words.py
"""
from genai import similarity

pairs = [
    ("She aced the exam", "He passed the test with flying colors"),
    ("I love this movie", "I don't love this movie"),
]
for a, b in pairs:
    print(f"{similarity(a, b):.3f}  {a!r} vs {b!r}")
