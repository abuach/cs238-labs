"""Week 2 · Task 1: a framing of your own.

Write your own framing of the question on the marked line (a worried parent,
a skeptical journalist, a ten-year-old...), then run:
    uv run my_framing.py
"""
from genai import ask

q = "Is it still worth learning to code in the age of AI?"
mine = f"I'm a worried parent of a high-school senior. {q}"   # ← your framing

print(f"── Neutral\n{ask(q, max_tokens=80)}\n")
print(f"── Yours\n{ask(mine, max_tokens=80)}")
