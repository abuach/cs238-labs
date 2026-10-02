"""Week 1 · Task 2: predict, then peek.

Replace the two sentences below with your own, then run:
    uv run my_prompts.py
"""
from pathlib import Path
from genai import next_token_distribution
from genai.viz import plot_next_token

HERE = Path(__file__).parent
MODEL = "llama3.2:latest"

sure = "Twinkle, twinkle, little"            # ← your "very sure" sentence
anything = "My favorite thing to eat is"     # ← your "almost anything" sentence

for name, prompt in [("sure", sure), ("anything", anything)]:
    dist = next_token_distribution(prompt, model=MODEL, top_k=6)
    plot_next_token(prompt, dist, HERE / f"{name}.png")
