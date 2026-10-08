"""Week 2 · Part 1.1: temperature, the chapter's sweep.

Run it twice:  uv run temperature.py
"""
from genai import ask

prompt = ("Write a creative opening for a story that starts "
          "like: 'If I could start over, who would I be?'")
for temp in [0.0, 0.7, 1.5]:
    print(f"temp={temp}: {ask(prompt, options={'temperature': temp})}\n")
