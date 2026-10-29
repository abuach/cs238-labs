"""Week 5 · Task 4: what has the model memorized?

Write the start of a few lines you think the model has seen many times (a
famous speech, a poem, a saying) and one line you made up yourself. For each,
the model finishes the line, and we read how sure it was of the next word.
Run from this folder:  uv run my_recitation.py
"""
import ollama
from genai import get_host, next_token_distribution

MODEL = "llama3.2:latest"
client = ollama.Client(host=get_host())

lines = [
    ("famous",  "Four score and seven years"),                    # ← yours
    ("famous",  "Ask not what your country can do for"),          # ← yours
    ("made up", "The purple calculator whispered to the"),        # ← one you made up
]

print(f"{MODEL} finishes the start of each line. We write the start into the")
print("model's own reply (the Week 1 trick), so it has to continue it. 'How sure'")
print("is the probability it gave the next word, from 0% to 100%. A memorized")
print("line comes back nearly certain; a line it has never seen forces a guess.\n")
for kind, start in lines:
    reply = client.chat(model=MODEL, messages=[
        {"role": "user", "content": "Finish this line."},
        {"role": "assistant", "content": start}],            # the model continues this
        options={"temperature": 0, "num_predict": 12})
    finish = reply["message"]["content"].strip().replace("\n", " ")
    word, p = next_token_distribution("Finish this line.", model=MODEL, top_k=1,
                                      reply_start=start)[0]
    print(f"── ({kind}) {start} ...")
    print(f"   The model continues:  {finish}")
    print(f"   How sure it was of the next word, '{word.strip()}':  {p:.0%}\n")
