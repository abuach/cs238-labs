"""Week 2 · Optional: your own step-back question (the chapter's Exercise 2).

Find a question where your own first instinct tends to be wrong.
Run from the week02 folder:  uv run optional/my_step_back.py
"""
from genai import ask
from genai.prompting import step_back

question = ("If it takes 5 machines 5 minutes to make 5 widgets, how many "   # ← yours
            "minutes would it take 100 machines to make 100 widgets?")

print(f"── Asked cold\n{ask(question, max_tokens=100)}\n")
principle, answer = step_back(question)
print(f"── Principle first\n{principle}\n\n{answer}")
