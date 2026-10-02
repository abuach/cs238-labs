"""Week 2 · Optional: rewrite a real prompt (the chapter's Exercise 3).

Paste a prompt you recently gave a chatbot into `original`, then write a
version with all four parts of a prompt's anatomy into `rewritten`.
Run from the week02 folder:  uv run optional/my_prompt_rewrite.py
"""
from genai import ask

original = "Help me study for my biology test."                 # ← your real prompt

rewritten = (                                                    # ← your rewrite
    "Instruction: Write five practice questions with answers.\n"
    "Context: I'm a college sophomore with a biology test on cell "
    "respiration on Friday.\n"
    "Example: Q: Where does glycolysis happen? A: In the cytoplasm.\n"
    "Format: A numbered list, one question and its answer per item."
)

print(f"── Original\n{ask(original, max_tokens=250, system=None)}\n")
print(f"── Rewritten\n{ask(rewritten, max_tokens=250, system=None)}")
