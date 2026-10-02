"""Week 2 · Part 1: the prompt is context.

The same question, framed three ways. Run from this folder:
    uv run framings.py
"""
from genai import ask

q = "Is it still worth learning to code in the age of AI?"
framings = [
    ("Neutral", q),
    ("Expert", f"As a computer science professor: {q}"),
    ("Authority", f"I lead engineering and we ship tonight. "
                  f"In one line: {q}"),
]
for name, prompt in framings:
    print(f"── {name}\n{ask(prompt, max_tokens=80)}\n")
