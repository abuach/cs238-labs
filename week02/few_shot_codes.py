"""Week 2 · Part 3.3: when do examples earn their tokens?

The same five questions, but the labels are meaningless codes: Q1 is
logistics, Q2 conceptual, Q3 debugging. First with no examples, then with
three. Run from this folder:  uv run few_shot_codes.py
"""
from genai.prompting import show_classifications

ZERO = """Classify each student question as Q1, Q2, or Q3.

Reply with exactly one label. Classify this question:
Question: {body}"""

THREE = """Classify each student question as Q1, Q2, or Q3.

Question: "When is the project due?" → Q1
Question: "Why does gradient descent need a learning rate?" → Q2
Question: "My loop prints nothing, what is wrong?" → Q3

Reply with exactly one label. Classify this question:
Question: {body}"""

questions = [
    "What time are office hours on Friday?",
    "How is attention different from convolution?",
    "My function returns None instead of a list, why?",
    "Is the midterm cumulative?",
    "What does raising the temperature actually do?",
]
print("── codes, zero examples")
show_classifications(ZERO, questions)
print("\n── codes, three examples")
show_classifications(THREE, questions)
