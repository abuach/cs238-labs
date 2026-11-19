"""Week 8 · Part 4: a real error to screenshot.

This crashes on purpose with a KeyError. Run from this folder:
    uv run broken.py
"""
import collections

def process_data(rows):
    counts = collections.Counter(row["fn"] for row in rows)
    return counts

process_data([{"name": "ada"}, {"name": "grace"}])
