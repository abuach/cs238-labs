"""Week 2 · Part 1.3: count the answers.

Ask for an animal six times at each temperature and count what comes back.
Run from this folder:  uv run count_animals.py
"""
from collections import Counter
from genai import ask

def tally(prompt, temperature, n=6, **options):
    """Ask the same question n times and count the distinct answers."""
    answers = [ask(prompt, max_tokens=8,
                   options={"temperature": temperature, **options}).strip()
               for _ in range(n)]
    return dict(Counter(answers))

prompt = "Name one animal. Reply with one word."
for temp in [0.0, 1.0, 2.0]:
    print(f"temperature {temp}: {tally(prompt, temp)}")
print("temperature 2.0, top_k=1:", tally(prompt, 2.0, top_k=1))
