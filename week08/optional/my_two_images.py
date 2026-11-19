"""Week 8 · Optional: two images at once.

Photograph a sketch of an app screen (my_sketch) and your notes on what the app
should do (my_notes), save both in the week08 folder, and ask whether the
design covers everything. Run from the week08 folder:
    uv run optional/my_two_images.py
"""
from pathlib import Path
from genai import ask_images

WEEK = Path(__file__).parent.parent

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in the week08 folder."""
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        path = WEEK / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.jpg (or .png) in {WEEK}")

print("Showing gemma4 two images at once: your app sketch (my_sketch) and your")
print("feature list (my_notes), and asking whether the sketch covers the list.\n")
print("The model's answer:")
print(ask_images(
    [my_image("sketch"), my_image("notes")],
    "The first image is a sketch of an app screen. The second is a list of "
    "what the app should do. In 4-5 sentences: does the screen support "
    "everything on the list, and is anything missing?",
    model="gemma4:latest").strip())
