"""Week 8 · Task 3: find the counting cliff (the chapter's Exercise 5).

Asks for a quick count and a careful one-by-one count of each pile. If you
photographed something other than coins, change OBJECT. Run from this folder:
    uv run my_count.py
"""
from pathlib import Path
from genai import ask_image

HERE = Path(__file__).parent
OBJECT = "coins"                                  # ← what you photographed

def my_image(name):
    """Find my_<name>.jpg, .jpeg, or .png in this folder."""
    for ext in (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG"):
        path = HERE / f"my_{name}{ext}"
        if path.exists():
            return path.read_bytes()
    raise SystemExit(f"Couldn't find my_{name}.jpg (or .png) in {HERE}")

print(f"Asking gemma4 to count the {OBJECT} in each photo two ways:")
print("  Quick:   just give the number.")
print("  Careful: count them one at a time, then give the total.")
for name, real in [("pile3", 3), ("pile12", 12), ("pile25", 25)]:
    img = my_image(name)
    quick = ask_image(img, f"How many {OBJECT} are in this image? "
                           "Reply with only the number.",
                      model="gemma4:latest")
    careful = ask_image(img, f"Count the {OBJECT} one at a time, numbering "
                             "each one as you go, then give the total.",
                        model="gemma4:latest")
    print(f"\n── my_{name} (really has {real} {OBJECT})")
    print(f"   Quick count:   {quick.strip()}")
    print(f"   Careful count, the end of its answer: ...{careful.strip()[-120:]}")
