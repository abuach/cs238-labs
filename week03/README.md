# Week 3 Lab: Tokens and Meaning

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapters 3 (Tokens) and 4 (Semantics) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Predict how a tokenizer will chop up words, emoji, code, and numbers, and explain why that matters
- Explain why models struggle to count letters and multiply long numbers
- Turn text into an embedding and measure how close two meanings are with cosine similarity
- Show where word arithmetic works, where it breaks, and why opposites sit close together
- Build a small semantic search, then find a query that fools it

---

## Before You Start

- Completed the Week 1 and Week 2 labs
- Read Chapters 3 and 4

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week03
```

Run every script below from inside this folder with `uv run`.

**Working locally?** This lab uses `gemma4` and `nomic-embed-text`.

---

# Part 1: Tokens (22 minutes)

A language model never sees your words. It sees *tokens*, chunks of text that are each swapped for an integer ID. `count_tokens` and `tokenize` show you the chunks, using the tokenizer behind GPT-4 unless you name another.

## 1.1 What's a Token? (6 minutes)

`tokens.py` splits five strings into tokens: a short word, a longer word, a very long word, an emoji, and an accented word.

```bash
uv run tokens.py
```

**Task 1 (the chapter's Exercise 1):** Open `my_tokens.py` and put your own strings on the four marked lines: your name, a long technical term from your major, a common English word, and an emoji. **Before running it**, guess whether each will be one clean token or shatter into pieces.

```bash
uv run my_tokens.py
```

How often was your guess right?

## 1.2 Letters the Model Can't See (5 minutes)

If a model only sees chunks, then counting the letters inside a word asks it to read something it can't see. `letters.py` asks the model to count letters in three words (showing each word's tokens beside the answer), then to spell "tokenization" backward.

```bash
uv run letters.py
```

**Task 2:** Count the letters yourself. Which counts did the model get right? Did it spell the word backward correctly? Look at the token pieces: why is this task hard for a model and easy for you?

## 1.3 How Code Gets Tokenized (6 minutes)

Code leans on the vocabulary differently from prose: `=` versus `==` matters, and so does indentation. `code_tokens.py` runs one identifier written four ways (`get_user_by_id`, `get-user-by-id`, `getUserById`, `GETUSERBYID`) through StarCoder2's code tokenizer, then shows how three tokenizers handle twelve spaces of indentation: a modern general one, the code one, and GPT-2's from 2019. The first run downloads the two tokenizers it needs (a few megabytes).

```bash
uv run code_tokens.py
```

**Task 3:** Which naming style costs the fewest tokens? How many tokens does the 2019 tokenizer spend on the indentation, compared with the modern ones?

## 1.4 Numbers Come in Chunks (5 minutes)

`numbers.py` shows how four numbers split into tokens, then asks `gemma4` to multiply 3947 × 6281. The true product is **24,791,107**.

```bash
uv run numbers.py
```

**Task 4:** Did the model get it right? If not, was its answer at least the right *size*? Use the three-digit chunks to explain why a model can't do column-by-column multiplication the way you would.

---

# Part 2: Meaning as Location (21 minutes)

An *embedding* turns text into a long list of numbers, a point in space, and *cosine similarity* measures how closely two of those points line up: `1` for the same direction, `0` for nothing in common.

## 2.1 Words as Locations (5 minutes)

`semantics.py` prints the start of the embedding for "cat" and how long it is, then compares "cat" with "kitten", "dog", and "car".

```bash
uv run semantics.py
```

The ranking should match common sense: kitten closest, car furthest.

## 2.2 Meaning Versus Word Overlap (5 minutes)

This is the chapter's Exercise 1. `meaning_vs_words.py` scores two pairs of sentences. The first pair shares almost no words but means the same thing ("She aced the exam" / "He passed the test with flying colors"); the second shares nearly every word but flips the meaning ("I love this movie" / "I don't love this movie"). **Before running it**, predict each score.

```bash
uv run meaning_vs_words.py
```

**Task 5:** Were your predictions close? Does the embedding rate meaning over surface wording? Where did the negation pair land?

## 2.3 Word Arithmetic, and Where It Breaks (6 minutes)

`analogies.py` tries two word-arithmetic problems: king − man + woman, and happy − sad + rich (hoping for the opposite of "rich"). Then it prints a table of how close real opposites sit.

```bash
uv run analogies.py
```

**Task 6:** The famous trick lands on "queen." What does the opposite of "rich" come back as? Look at the table: where do real opposites like "rich / poor" land on the scale from `-1` to `1`? Why do words that mean opposite things sit so close together? (Hint: "the company it keeps.")

## 2.4 A Semantic Search You Can Fool (5 minutes)

`search.py` is the chapter's demo: six sentences about AI, cooking, and space, searched for "artificial intelligence" and "dinner". Neither query shares a word with the documents it finds.

```bash
uv run search.py
```

**Task 7 (the chapter's Exercise 5):** Open `my_search.py`. Replace the corpus with six to eight sentences of your own on two or three topics. Set `finds_it` to a query that shares no words with the document you want, and `fools_it` to a query designed to *mislead* the search.

```bash
uv run my_search.py
```

Did the first query still find your document? What did the second one return? Does the search ever warn you that it missed?

---

## Part 3: Lab Questions (5 minutes)

Open `lab3_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **Tokens (Tasks 1 and 2):** Which of your strings split the way you guessed, and which surprised you? Why can't a model reliably count the letters in "strawberry"?
2. **Numbers (Task 4):** What did the model answer for 3947 × 6281, and how do the three-digit chunks explain the mistake? Is this a failure of *perception* or of *reasoning*?
3. **Meaning (Tasks 5 and 6):** Which of your similarity predictions was furthest off? Explain in a sentence or two why "rich" and "poor" sit close together in embedding space.
4. **Search (Task 7):** What query fooled your search, and what did it return? Where would you add a plain keyword check to catch what the embeddings blur together?

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab3_results.txt` to the **Week 3 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week03` folder.

- **Prose versus code (Tokens Exercise 3).** In `optional/my_prose_vs_code.py`, put a paragraph of English and a Python snippet of about the same length on screen. Predict which costs more tokens, then run it. It also tries the snippet with tabs instead of spaces.
  ```bash
  uv run optional/my_prose_vs_code.py
  ```
- **The borrowed arrow (Semantics Exercise 3).** An analogy works by lifting the step from one word pair and dropping it on another. `optional/borrowed_arrow.py` checks whether "man → woman" points the same way as "king → queen", and whether "happy → sad" points the same way as "rich → poor". Why can "gender" be one direction in the space when "opposite" can't?
  ```bash
  uv run optional/borrowed_arrow.py
  ```
- **Cluster a corpus (Semantics Exercise 6).** In `optional/my_clusters.py`, put nine or ten sentences from three topics you know well, plus one sentence that straddles two of them. Do the groups match your topics, and which group claims the straddler?
  ```bash
  uv run optional/my_clusters.py
  ```
