"""Week 8 · Optional: a second opinion from a much smaller vision model.

Reruns the quick counts and both screenshots with gemma4:e2b, a far smaller
model than gemma4, side by side. Run from the week08 folder:
    uv run optional/second_opinion.py
"""
from pathlib import Path
from genai import ask_image

WEEK = Path(__file__).parent.parent
OBJECT = "coins"                                  # ← what you photographed

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in the week08 folder."""
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        path = WEEK / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.jpg (or .png) in {WEEK}")

print(f"Two vision models, gemma4 and the much smaller gemma4:e2b, count the")
print(f"{OBJECT} in your photos and read both of your error screenshots.")
for model in ["gemma4:latest", "gemma4:e2b"]:              # ← or try "llava:latest"
    print(f"\n── {model}")
    for name, real in [("pile3", 3), ("pile12", 12), ("pile25", 25)]:
        count = ask_image(my_image(name), f"How many {OBJECT} are in this image? "
                          "Reply with only the number.", model=model)
        print(f"   my_{name} (really {real}): it counted {count.strip()}")
    for name in ["error_small", "error_big"]:
        diagnosis = ask_image(my_image(name),
                              "This is a terminal screenshot of a Python error. "
                              "What error occurred, in one sentence?", model=model)
        print(f"   my_{name}: {diagnosis.strip()}")
