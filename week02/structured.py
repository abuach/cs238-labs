"""Week 2 · Part 3.1: pin down the shape.

Asks the same question three ways and shows a tiny `key: value` parser trying
to read each answer. Run from this folder:  uv run structured.py
"""
from genai.prompting import show_structured

show_structured(
    "Give me the sport, match length (minutes), and players "
    "per side for soccer.",
    keys=["sport", "match_minutes", "players_per_side"])
