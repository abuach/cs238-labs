"""Week 3 · Part 2.1: words as locations.

Run from this folder:  uv run semantics.py
"""
from genai import embed, similarity

v = embed("cat")
print(f"cat -> [{v[0]:+.2f}, {v[1]:+.2f}, {v[2]:+.2f}, ...] "
      f"({len(v)} numbers long)")

for word in ["kitten", "dog", "car"]:
    print(f"cat-{word}: {similarity('cat', word):.3f}")
