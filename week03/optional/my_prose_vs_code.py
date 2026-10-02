"""Week 3 · Optional: prose versus code (Tokens Exercise 3).

Put a paragraph of English and a Python snippet of about the same length on
screen in the marked strings. Predict which costs more, then run from the
week03 folder:  uv run optional/my_prose_vs_code.py
"""
from genai import count_tokens

prose = ("Tokenization is the very first thing that happens to your text "     # ← yours
         "before a language model ever sees it, the step that chops words "
         "and code into the units a model reads.")

code = '''def first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
    return None
'''                                                                              # ← yours

for label, text in [("prose", prose), ("code (spaces)", code),
                    ("code (tabs)", code.replace("    ", "\t"))]:
    print(f"{label:14} {len(text):4} chars  {count_tokens(text):3} tokens  "
          f"{len(text) / count_tokens(text):.1f} chars/token")
