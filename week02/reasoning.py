"""Week 2 · Part 4: the reasoning ladder.

Misguided attention, chain of thought, and step-back prompting.
Run from this folder:  uv run reasoning.py
"""
from genai.prompting import show_reply, show_cot_comparison, show_step_back

# Misguided attention: a famous puzzle with a trivial twist
show_reply("A farmer has a wolf, goat, and cabbage. "
           "He can carry one at a time.\n"
           "How does he get just the goat safely across? "
           "He doesn't need anything else.",
           model="llama3.2:latest", num_predict=200)

# Chain of thought: cold vs. "Let's think step by step." (answer: 67)
print()
show_cot_comparison("When I was 6 my sister was half my age. "
                    "Now I am 70. How old is my sister?",
                    ["gemma4:latest", "llama3.2:latest"])

# Step-back: name the principle first, then answer
print()
show_step_back("Half")
