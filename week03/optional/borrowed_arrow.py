"""Week 3 · Optional: the borrowed arrow (Semantics Exercise 3).

An analogy works by lifting the step from one word pair and dropping it on
another. Do the steps really point the same way?
Run from the week03 folder:  uv run optional/borrowed_arrow.py
"""
from genai import embed, similarity
from genai.embed import show_offset_consistency

gender_1 = embed("woman") - embed("man")
gender_2 = embed("queen") - embed("king")
opposite_1 = embed("sad") - embed("happy")
opposite_2 = embed("poor") - embed("rich")

print(f"man→woman vs king→queen:  {similarity(gender_1, gender_2):.2f}")
print(f"happy→sad vs rich→poor:   {similarity(opposite_1, opposite_2):.2f}\n")
show_offset_consistency()
