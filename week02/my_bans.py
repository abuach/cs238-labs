"""Week 2 · Task 4: set your own pink-elephant traps (the chapter's Exercise 4).

Write two negative instructions of your own on the marked lines, each forbidding
a word strongly tied to its topic. Then rewrite one as a positive instruction
that gives the model somewhere to go. Run from this folder:
    uv run my_bans.py
"""
from genai.prompting import show_bans

show_bans([
    ("trap 1",                                                  # ← your trap
     "Describe a birthday party in one sentence. "
     "Do not use the word 'cake'."),
    ("trap 2",                                                  # ← your trap
     "Describe a library in one sentence. "
     "Do not use the word 'books'."),
    ("positive",                                                # ← your rewrite
     "Describe a birthday party in one sentence, and call the "
     "dessert 'the sweet centerpiece'."),
])
