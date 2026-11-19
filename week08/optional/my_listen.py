"""Week 8 · Optional: teach a model to listen.

Record a short voice memo, convert it to a 16 kHz mono WAV named my_memo.wav in
the week08 folder (see the README), and transcribe it. The first run downloads
a small Whisper model. Run from the week08 folder:
    uv run optional/my_listen.py
"""
from pathlib import Path
from genai import transcribe

WEEK = Path(__file__).parent.parent
memo = WEEK / "my_memo.wav"
if memo.exists():
    print("Transcribing your voice memo (my_memo.wav)...\n")
else:
    memo = WEEK / "samples" / "memo.wav"
    print("No my_memo.wav found, so transcribing the sample samples/memo.wav.")
    print("Save your own recording as my_memo.wav to use it instead.\n")
print("What the model heard:")
print(transcribe(memo))
