"""Week 2 · Part 2.3: count the "random" numbers.

Predict what you'll see at temperature 2.0 before you run it:
    uv run count_numbers.py
"""
from collections import Counter
from genai import ask

def tally(prompt, temperature, n=6, **options):
    """Ask the same question n times and count the distinct answers."""
    answers = [ask(prompt, max_tokens=8,
                   options={"temperature": temperature, **options}).strip()
               for _ in range(n)]
    return dict(Counter(answers))

prompt = "Pick a random number between 1 and 10. Reply with only the number."
for temp in [0.0, 1.0, 2.0]:
    print(f"temperature {temp}: {tally(prompt, temp)}")
