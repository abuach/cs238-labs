"""Week 1 · Part 0: the chapter's setup check.

Run from this folder:  uv run check_setup.py
"""
from genai import ask, get_host

print(f"Talking to: {get_host()}\n")

# If this returns a response, your setup is working!
print(ask("What does generative mean?"))
