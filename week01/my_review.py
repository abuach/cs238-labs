"""Week 1 · Task 1: a review that's hard to label.

Replace the review below with one you write yourself, then run:
    uv run my_review.py
"""
from genai import ask

review = "Oh great, another three-hour superhero movie."   # ← your review

label = ask("Classify as POSITIVE, NEGATIVE, or MIXED. "
            f"One word.\n{review}")
print(f"Review → {review}")
print(f"Label  → {label}")
