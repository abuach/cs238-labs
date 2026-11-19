"""Week 8 · Part 5: alt-text that does its job (the chapter's Exercise 6).

One sentence of alt-text for three of your photos.
Run from this folder:  uv run alt_text.py
"""
from pathlib import Path
from genai import ask_image

HERE = Path(__file__).parent

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in this folder."""
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        path = HERE / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.jpg (or .png) in {HERE}")

print("Alt-text is the description a screen reader speaks aloud for someone")
print("who can't see an image. gemma4's alt-text for each of your images:\n")
for name in ["photo1", "photo2", "unusual"]:
    alt = ask_image(my_image(name),
                    "Write one sentence of alt-text for this image, "
                    "the kind a screen reader would speak aloud.",
                    model="gemma4:latest")
    print(f"   my_{name}: {alt.strip()}")
