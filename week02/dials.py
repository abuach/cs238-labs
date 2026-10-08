"""Week 2 · Part 1.2: seeing the dials.

Temperature reshapes the odds; top-k and top-p trim which words are allowed.
Run from this folder:  uv run dials.py
"""
from pathlib import Path
from genai import next_token_distribution
from genai.viz import plot_sampling_controls
from genai.prompting import show_sampling_dials

HERE = Path(__file__).parent

dist = next_token_distribution("She opened the door and saw a",
                               model="llama3.2:latest", top_k=10)
plot_sampling_controls(dist, k=3, p=0.9, n=5,
                       save_path=HERE / "sampling_controls.png")

# Temperature is the accelerator; top-k and top-p are the brakes
show_sampling_dials("Describe a walk on the beach in one sentence.", [
    ("safe",       {"temperature": 0.7, "top_k": 40, "top_p": 0.9}),
    ("hot only",   {"temperature": 2.0, "top_k": 40, "top_p": 0.9}),
    ("brakes off", {"temperature": 2.0, "top_k": 0,  "top_p": 1.0}),
])
