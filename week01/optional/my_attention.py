"""Week 1 · Optional: your own pronoun test (the chapter's Exercise 2).

Write two sentences that differ by one word, where that word changes which
noun the pronoun points back to. Predict the answer, then run:
    uv run optional/my_attention.py
"""
from pathlib import Path
from genai.viz import plot_attention, plot_attention_votes

HERE = Path(__file__).parent

sentences = [
    "The trophy didn't fit in the suitcase because it was too big.",    # ← yours
    "The trophy didn't fit in the suitcase because it was too small.",  # ← yours
]
pronoun = "it"                                                          # ← yours

plot_attention(sentences, pronoun=pronoun, path=HERE / "my_attention.png")
for i, sentence in enumerate(sentences, start=1):
    plot_attention_votes(sentence, word=pronoun,
                         path=HERE / f"my_attention_votes_{i}.png")
