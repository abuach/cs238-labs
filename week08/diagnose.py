"""Week 8 · Part 4: reading an error screenshot (the chapter's Exercise 2).

Asks for a diagnosis of your small and zoomed-in screenshots.
Run from this folder:  uv run diagnose.py
"""
from pathlib import Path
from genai import ask_image

HERE = Path(__file__).parent

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in this folder, or else use the sample."""
    for ext in (".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"):
        path = HERE / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    for path in sorted((HERE / "samples").glob(f"{name}.*")):
        print(f"(No my_{name} found, so using the sample samples/{path.name}. "
              f"Save your own as my_{name}.png to use it instead.)")
        return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.png or a sample in {HERE}")

prompt = ("This is a terminal screenshot of a Python error. In 3-4 "
          "sentences: what error occurred, which line caused it, and "
          "what is the most likely fix?")
print("Asking gemma4 to read each of your error screenshots.")
for name, size in [("error_small", "normal-size text"),
                   ("error_big", "zoomed-in text")]:
    print(f"\n── my_{name} ({size}). The model's diagnosis:")
    print(ask_image(my_image(name), prompt, model="gemma4:latest").strip())
