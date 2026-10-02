"""Week 1 · Part 2.2: a door that opens onto anything.

Run from this folder:  uv run door.py
"""
from pathlib import Path
from genai import next_token_distribution
from genai.viz import plot_two_step

HERE = Path(__file__).parent
MODEL = "llama3.2:latest"
door = "She opened the door and saw a"

# 1. The forecast for the first word: many reasonable options
step1 = next_token_distribution(door, model=MODEL, top_k=6)

# 2. Lock in the favorite and forecast the word after it
top_word = step1[0][0]
step2 = next_token_distribution(door, model=MODEL, top_k=6,
                                reply_start=top_word)
plot_two_step(door, top_word, step1, step2, HERE / "door.png")
