"""Week 5 · Part 3: leaks nobody typed.

Memorization, an embedding that gives away its secret, and poisoned examples.
Run from this folder:  uv run leaks.py
"""
from genai.security import show_recitation, show_embedding_attack, show_poisoning

# 1. Memorization: famous lines come back word for word, with high confidence
print("═══ 1. MEMORIZATION. We give the model the start of some famous lines")
print("(and one made-up line it can't have seen) and it finishes each one.")
print("p is how sure it was of its first word: 1.00 means completely certain.\n")
show_recitation(model="llama3.2:latest")

# 2. An embedding is not a disguise: guess the diagnosis from the vector alone
print("\n═══ 2. EMBEDDING LEAK. The attacker has only the stored embeddings of")
print("patient records, not the text. They embed a few guesses and keep the")
print("closest (cosine near 1 = very close). Then we reveal the real record.\n")
show_embedding_attack()

# 3. Poisoned examples: swap the labels and the judgment flips
print("\n═══ 3. POISONING. The model sorts emails using labeled examples.")
print("CLEAN is its answer with honest examples; POISON is its answer after")
print("the example labels were swapped.\n")
show_poisoning()
