"""Week 1 · Optional: bigger isn't always better (the chapter's Warm-Up 2).

Run from the week01 folder:  uv run optional/smaller_model.py
"""
from genai import ask

question = "What does generative mean?"
for model in ["gemma4:latest", "llama3.2:1b"]:
    print(f"── {model}\n{ask(question, model=model)}\n")
