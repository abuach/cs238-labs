"""Week 3 · Part 2.4: semantic search, the chapter's demo.

Neither query shares a word with the documents it finds.
Run from this folder:  uv run search.py
"""
from genai import semantic_search

corpus = [
    "Neural networks learn patterns from data",
    "Machine learning powers modern AI systems",
    "The chef simmered the tomato sauce for an hour",
    "Fresh basil and garlic make the pasta fragrant",
    "The telescope captured a distant spiral galaxy",
    "A rocket launched toward the moon at dawn",
]
for query in ["artificial intelligence", "dinner"]:
    print(f"\n{query!r}:")
    for doc in semantic_search(query, corpus):
        print("  ", doc)
