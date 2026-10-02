"""Week 1 · Optional: paying attention, the chapter's BERT demo.

Needs BERT first:  uv run optional/download_bert.py
Then run:          uv run optional/attention.py
"""
from pathlib import Path
from genai.viz import plot_attention, plot_attention_votes

HERE = Path(__file__).parent

# One word changes, and "it" points somewhere else
plot_attention([
    "The cat sat on the laptop because it was tired.",
    "The cat sat on the laptop because it was warm.",
], pronoun="it", path=HERE / "attention_it.png")

# All 144 of BERT's heads vote on what "standing" attends to most
plot_attention_votes("She opened the door and saw a man standing.",
                     word="standing",
                     path=HERE / "attention_standing.png")
