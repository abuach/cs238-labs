"""Week 8 · Part 2: confidently wrong (the chapter's Exercise 1).

The same unusual photo, asked three ways. Run from this folder:
    uv run identify.py
"""
from pathlib import Path
from genai import ask_image

HERE = Path(__file__).parent

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in this folder, or else use the sample."""
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        path = HERE / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    for path in sorted((HERE / "samples").glob(f"{name}.*")):
        print(f"(No my_{name} found, so using the sample samples/{path.name}. "
              f"Save your own as my_{name}.jpg to use it instead.)")
        return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.jpg or a sample in {HERE}")

img = my_image("unusual")
print("Asking gemma4 about your unusual object (my_unusual) three different ways.")
for prompt in [
    "What is this? Name it as precisely as you can in one sentence.",
    "What is this, and how sure are you? If you're not sure, say so.",
    "List three different things this could be, most likely first.",
]:
    print(f"\n── We asked: {prompt}")
    print(ask_image(img, prompt, model="gemma4:latest").strip())
