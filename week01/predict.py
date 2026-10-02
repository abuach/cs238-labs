"""Week 1 · Part 2.1: one obvious answer, one long shot.

Run from this folder:  uv run predict.py
Close each chart window to let the script continue.
"""
from pathlib import Path
from genai import ask, next_token_distribution
from genai.viz import plot_next_token, plot_two_step

HERE = Path(__file__).parent
MODEL = "llama3.2:latest"
prompt = "The capital of the USA is"

# 1. The model's forecast for the first word of its answer
dist = next_token_distribution(prompt, model=MODEL, top_k=6)
plot_next_token(prompt, dist, HERE / "washington.png")

# 2. Commit to the long shot: start the model's own answer with "New"
step2 = next_token_distribution(prompt, model=MODEL, top_k=6,
                                reply_start="New")
plot_two_step(prompt, "New", dist, step2, HERE / "new_york.png")

# 3. The same words, sent as a message of our own instead
print(ask("The capital of the USA is New", model=MODEL,
          options={"temperature": 0}))
