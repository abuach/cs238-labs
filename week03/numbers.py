"""Week 3 · Part 1.4: numbers come in chunks.

Run from this folder:  uv run numbers.py
"""
from genai import tokenize
from genai.tokens import show_digit_product

# Numbers chunk three digits from the left, not by place value
for n in ["42", "1234", "1234567", "8675309"]:
    print(f"{n:9} -> {tokenize(n)}")

print()
show_digit_product()   # asks gemma4 for 3947 × 6281 (the answer is 24,791,107)
