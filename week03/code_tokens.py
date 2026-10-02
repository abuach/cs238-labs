"""Week 3 · Part 1.3: how code gets tokenized.

The first run downloads two small tokenizer files (a few megabytes).
Run from this folder:  uv run code_tokens.py
"""
from genai import count_tokens, tokenize
from genai.tokens import show_indent_tokens

# Same identifier, four naming styles, through a code tokenizer (StarCoder2's)
for name in ["get_user_by_id", "get-user-by-id",
             "getUserById", "GETUSERBYID"]:
    print(f"{name:16} {count_tokens(name, 'code'):2d} -> "
          f"{tokenize(name, 'code')}")

# Twelve spaces of indentation, through three tokenizers
print()
show_indent_tokens("            return value")
