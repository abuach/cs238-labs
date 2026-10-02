"""Week 3 · Task 7: a semantic search you can fool (the chapter's Exercise 5).

Replace the corpus with six to eight sentences of your own on two or three
topics. Set `finds_it` to a query that shares no words with the document you
want, and `fools_it` to a query designed to mislead. Then run:
    uv run my_search.py
"""
from genai import semantic_search

corpus = [                                                   # ← your sentences
    "The Seahawks won in overtime on a last-second field goal",
    "Our soccer team practices twice a week at the park",
    "Sourdough needs a starter that has been fed for days",
    "The croissants came out flaky and golden",
    "Our cat naps in the sunniest spot in the house",
    "The puppy chewed through another shoe this morning",
]
finds_it = "bread baking"                                    # ← your query
fools_it = "football club"                                   # ← your tricky query

for query in [finds_it, fools_it]:
    print(f"\n{query!r}:")
    for doc in semantic_search(query, corpus):
        print("  ", doc)
