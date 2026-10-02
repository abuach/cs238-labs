"""Week 2 · Part 3.2: few-shot examples, the chapter's classifier.

Run from this folder:  uv run few_shot.py
"""
from genai.prompting import show_classifications

FEW_SHOT = """Classify each student question as LOGISTICS, CONCEPTUAL, or DEBUGGING.

Question: "When is the project due?" → LOGISTICS
Question: "Why does gradient descent need a learning rate?" → CONCEPTUAL
Question: "My loop prints nothing, what is wrong?" → DEBUGGING
Question: "Can I use a late day on the lab?" → LOGISTICS

Reply with exactly one word. Classify this question:
Question: {body}"""

questions = [
    "What time are office hours on Friday?",
    "How is attention different from convolution?",
    "My function returns None instead of a list, why?",
    "Is the midterm cumulative?",
    "What does raising the temperature actually do?",
]
show_classifications(FEW_SHOT, questions)
