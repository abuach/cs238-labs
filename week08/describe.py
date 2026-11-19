"""Week 8 · Part 1: what the model actually receives.

Describes your photo, then shows what ask_image really ships to the model: the
picture, turned into text. Run from this folder:  uv run describe.py
"""
import base64
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

img_bytes = my_image("photo1")

print("Asking gemma4 to describe your photo (my_photo1).\n")
print("The model's description:")
print(ask_image(img_bytes,
                "Describe what you see. What is happening, and what "
                "mood does it convey? Two to three sentences.",
                model="gemma4:latest").strip())

encoded = base64.b64encode(img_bytes).decode()
print("\nHow the photo travels to the model: it's turned into plain text.")
print(f"   Your photo is {len(img_bytes):,} bytes.")
print(f"   As text, it's {len(encoded):,} characters long.")
print(f"   The text starts like this: {encoded[:48]}...")
