"""Week 5 · Part 2: attacks that ride in on documents.

Indirect injection hides the instruction in a document the system trusts; then
a direct ask versus the same ask in costume. Run from this folder:
    uv run indirect.py
"""
from genai.security import (ask_about_note, ask_naive, CLEAN_NOTE,
                            POISONED_NOTE, DIRECT_ASK, PREFIX_JAILBREAK)

print("How to read this: USER is the request, DOCUMENT is the clinical note the")
print("assistant was handed, and GEMMA4:E2B is its reply.\n")

print("═══ 1. The everyday job: summarize a clean note.\n")
ask_about_note(CLEAN_NOTE)                     # the everyday job

print("\n═══ 2. The same job, but someone planted one extra sentence in the note.\n")
ask_about_note(POISONED_NOTE)                  # one planted sentence

print("\n═══ 3. The poisoned note again, with the security policy turned on.\n")
ask_about_note(POISONED_NOTE, hardened=True)   # the policy doesn't help

print("\n═══ 4. Asking for the secret code directly.\n")
ask_naive(DIRECT_ASK)                          # the blunt ask

print("\n═══ 5. The same ask, in costume: dressed up as a line from a stage play.\n")
ask_naive(PREFIX_JAILBREAK)                    # the same ask, in costume
