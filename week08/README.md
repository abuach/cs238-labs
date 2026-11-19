# Week 8 Lab: Giving the Model Eyes

**CS238 · Instructor: Chiké Abuah**
**Lab Duration:** ~50 minutes
**Reading:** Chapter 9 (Multimodal) of *Illustrating Generative AI*

---

## Learning Objectives

By the end of this lab, you will be able to:
- Send your own images to a vision-language model and write prompts that get specific answers
- Explain what the model actually receives when you "show" it a picture
- Catch a vision model being confidently wrong, and find where its counting breaks down
- Use a model to read an error screenshot, and show how much resolution matters
- Judge machine-written alt-text the way a low-vision user would

---

## Before You Start

- Completed the earlier labs (`gemma4` can read images as well as text)
- Read Chapter 9

Get this week's lab and go into its folder. From your `cs238` folder:

```bash
cd cs238-labs
```
```bash
git pull
```
```bash
cd week08
```

Run every script below from inside this folder with `uv run`. Every script passes `model="gemma4:latest"`, the chapter's capable vision model.

**Working locally?** This lab uses `gemma4`; the optional second opinion also uses `gemma4:e2b`.

### Bring Your Own Images (before lab, ~10 minutes)

This week you supply the pictures. Take these photos with your phone and copy them to your computer as **JPG or PNG** files (on an iPhone, export or AirDrop them as "Most Compatible" so they aren't HEIC). Save them in this `week08` folder with exactly these names:

| File | What it shows |
|---|---|
| `my_unusual.jpg` | Something a little unusual: a rare plant, an odd gadget, a pet of an unusual breed, or an object that looks like something else |
| `my_pile3.jpg`, `my_pile12.jpg`, `my_pile25.jpg` | Three piles of coins (or paper clips, or buttons) on a plain table: **3**, **12**, and **25** objects. Let a few in the big pile touch or overlap, the way a real pile would. Count them carefully yourself! |
| `my_photo1.jpg`, `my_photo2.jpg` | Two ordinary photos you'd be comfortable describing to a stranger (a room, a street, a meal) |

`.png` works too (`my_unusual.png`, and so on); the scripts look for either.

---

## Part 1: What the Model Actually Receives (7 minutes)

`describe.py` asks the model to describe `my_photo1` and the mood it conveys. Then it shows what `ask_image` really ships to the model: your picture, turned into a long string of text.

```bash
uv run describe.py
```

**Task 1:** How accurate and how specific was the description? The image traveled to the model as one enormous "word" of text; inside the model it's sliced into a grid of *patches*, each treated like a token. Roughly how many characters long was your image?

---

## Part 2: Confidently Wrong (8 minutes)

The chapter's small model called a mandrill a silverback gorilla without a flicker of doubt. This is its Exercise 1. `identify.py` asks about `my_unusual` three ways: name it precisely, say how sure it is, and list three things it could be.

```bash
uv run identify.py
```

**Task 2:** Was the first answer right? Did its *tone* ever hint at uncertainty? Did the answer change when you framed the question differently? (Cross-examining an unreliable witness with different framings is one of the few ways to spot a confident mistake.)

---

## Part 3: Find the Counting Cliff (10 minutes)

Vision models are strong at *what* is in a picture and weak at *how many*. This is the chapter's Exercise 5. `my_count.py` asks for a quick count of each pile, then a careful count that numbers each object one at a time. If you photographed something other than coins, change `OBJECT` on the marked line first.

```bash
uv run my_count.py
```

**Task 3:** At which pile did the count first go wrong? (If every count came back right, add a few more objects to the big pile, or let more of them overlap, and run it again.) Run the script a second time: did the quick counts change? Did asking it to count one by one move the answer closer to the truth? Why does a pattern-matching machine without an internal counter struggle here?

---

## Part 4: Reading an Error Screenshot (10 minutes)

The chapter found that a small, blurry screenshot made the model *invent* an error, while the same screen at a readable size got a correct diagnosis. This is its Exercise 2. First, make a real error. `broken.py` crashes on purpose:

```bash
uv run broken.py
```

It ends with a `KeyError`. Take **two** screenshots of the traceback and save them in this folder:
1. `my_error_small.png`: the whole terminal window at its normal size.
2. `my_error_big.png`: the same traceback after zooming the terminal text way up.

On a campus computer (Ubuntu), press `Shift+Print Screen` to select an area (it saves to `~/Pictures/Screenshots`), and zoom the terminal text with `Ctrl+Shift++`. On a Mac, use `Cmd+Shift+4` and `Cmd++`; on Windows, `Win+Shift+S` and `Ctrl++`.

`diagnose.py` asks the model to diagnose each screenshot:

```bash
uv run diagnose.py
```

**Task 4:** Did both diagnoses name the right error (`KeyError: 'fn'`) and the right line? Did either one invent something that isn't on the screen? Was the advice specific to *your* error, or generic boilerplate?

---

## Part 5: Alt-Text That Does Its Job (7 minutes)

Screen readers speak a one-sentence description of each image aloud to blind and low-vision users. This is the chapter's Exercise 6. `alt_text.py` writes alt-text for `my_photo1`, `my_photo2`, and `my_unusual`.

```bash
uv run alt_text.py
```

**Task 5:** Grade each caption as if you couldn't see the photo. What did a low-vision user just miss that mattered? What did the caption include that didn't matter?

---

## Part 6: Lab Questions (5 minutes)

Open `lab8_results.txt` in this folder, fill in your names and the date, and answer the questions in it **without using GenAI**:

1. **Confidence (Task 2):** What was your unusual object, what did the model call it, and did its tone ever match its accuracy?
2. **Counting (Task 3):** Where was your counting cliff? Give the true and reported counts for each pile, with and without counting one by one. Did a second run give the same counts?
3. **Screenshots (Task 4):** Compare the two diagnoses. What does this tell you about pasting screenshots into an AI assistant instead of copying the text?
4. **Alt-text (Task 5):** Write a better alt-text for one of your photos than the model's, and explain what you changed and why.

*There's no right or wrong answer here, I just want to see some thought go into the response. Base your answers on what you actually saw in this lab, and feel free to ask me any questions.*

---

## Submission

Upload `lab8_results.txt` to the **Week 8 Lab** assignment on D2L/Brightspace. If you worked with a partner, both partners should upload a copy.

Great work exploring multimodal AI! 🖼️

---

## Optional (if you finish early, or at home)

The files for these are in the `optional/` folder. Run them from this `week08` folder.

- **Two images at once.** Sketch a simple app screen on paper and photograph it as `my_sketch.jpg`, and photograph a list of what the app should do as `my_notes.jpg`, both in this folder. `optional/my_two_images.py` asks whether the design covers everything. Can the model reason *across* the two?
  ```bash
  uv run optional/my_two_images.py
  ```
- **A second opinion.** `optional/second_opinion.py` reruns your quick counts and both screenshots with `gemma4:e2b`, a much smaller model, next to `gemma4`. How much does the smaller model lose on counting and on reading screens? (The chapter compares `llava`, an older vision model; if the class server has it, change the model name on the marked line to try it.)
  ```bash
  uv run optional/second_opinion.py
  ```
- **Teach a model to listen.** Record a short voice memo and convert it to a 16 kHz mono WAV named `my_memo.wav` in this folder. On a Mac: `afconvert -f WAVE -d LEI16@16000 -c 1 memo.m4a my_memo.wav`; on Ubuntu: `ffmpeg -i memo.m4a -ar 16000 -ac 1 my_memo.wav`. Then transcribe it (the first run downloads a small Whisper model):
  ```bash
  uv run optional/my_listen.py
  ```
- **Draw instead of read (Exercise 3).** `optional/my_draw.py` turns text into a picture with a diffusion model. It needs two extra packages and a multi-gigabyte model download, so try it at home. From your `cs238` folder, first run `uv add diffusers accelerate`. Then ask for "a horse riding an astronaut" and see who ends up in the saddle.
  ```bash
  uv run optional/my_draw.py
  ```
