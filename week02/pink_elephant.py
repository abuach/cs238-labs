"""Week 2 · Part 3: the pink elephant.

A ban has to name the thing it forbids, and naming it makes the model more
likely to say it. Run from this folder:  uv run pink_elephant.py
"""
from genai.prompting import show_models, show_bans

question = ("What is the largest land animal on Earth? "
            "Answer in one short sentence, "
            "but do not use the word 'elephant'.")
show_models(question, ["gemma4:latest", "llama3.2:latest"],
            options={"temperature": 0})

print()
show_bans([
    ("no 'water'",
     "Describe the ocean in one sentence. "
     "Do not use the word 'water'."),
])
