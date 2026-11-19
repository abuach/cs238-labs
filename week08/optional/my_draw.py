"""Week 8 · Optional: draw instead of read (the chapter's Exercise 3).

Turns text into a picture. Needs extra packages and a multi-gigabyte model
download, so try it at home (see the README). Run from the week08 folder:
    uv run optional/my_draw.py
"""
from pathlib import Path
from genai import generate_image

prompt = "a horse riding an astronaut, photorealistic, dramatic lighting"   # ← yours
print(f"Drawing: {prompt}")
print("This can take a few minutes...")
image = generate_image(prompt, seed=0)
out = Path(__file__).parent / "my_drawing.png"
image.save(out)
print(f"Done. The picture is saved as {out.name} in the optional folder. Open it to look.")
