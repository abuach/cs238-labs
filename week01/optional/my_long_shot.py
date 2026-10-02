"""Week 1 · Optional: find your own long shot.

Put one of your Task 2 prompts in `prompt`, run it once to see the candidates,
then set `long_shot` to a word the model gave under 1% and run it again:
    uv run optional/my_long_shot.py
"""
from pathlib import Path
from genai import next_token_distribution
from genai.viz import plot_two_step

HERE = Path(__file__).parent
MODEL = "llama3.2:latest"

prompt = "My favorite thing to eat is"    # ← one of your prompts
long_shot = "spaghetti"                   # ← a candidate under 1%

step1 = next_token_distribution(prompt, model=MODEL, top_k=10)
for token, p in step1:
    print(f"{token!r:15} {p:6.1%}")

step2 = next_token_distribution(prompt, model=MODEL, top_k=6,
                                reply_start=long_shot)
plot_two_step(prompt, long_shot, step1, step2, HERE / "long_shot.png")
