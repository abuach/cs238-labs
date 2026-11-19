"""Week 8 · Optional: teach a model to listen.

Record a short voice memo, convert it to a 16 kHz mono WAV named my_memo.wav in
the week08 folder (see the README), and transcribe it. The first run downloads
a small Whisper model. Run from the week08 folder:
    uv run optional/my_listen.py
"""
from pathlib import Path
from genai import transcribe

memo = Path(__file__).parent.parent / "my_memo.wav"
print("Transcribing your voice memo (my_memo.wav)...\n")
print("What the model heard:")
print(transcribe(memo))
