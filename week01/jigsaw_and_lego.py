"""Week 1 · Part 1: the jigsaw and the LEGO.

Discriminative AI places a piece among options that already exist; generative
AI builds something new. A modern LLM can do both.

Run from this folder:  uv run jigsaw_and_lego.py
"""
from genai import ask

review = ("I felt like part one was more fast-paced and exciting, "
          "but the soundtrack in part two was more emotionally "
          "satisfying.")

# Discriminative: choose one of three labels that already exist
label = ask("Classify as POSITIVE, NEGATIVE, or MIXED. "
            f"One word.\n{review}")
print(f"Discriminate → {label}")

# Generative: make something that didn't exist before
new_review = ask("Write a one-sentence MIXED review of a movie sequel.")
print(f"Generate     → {new_review}")
