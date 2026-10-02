"""Week 1 · Optional: download BERT (about 420 MB, one time only).

Run from the week01 folder:  uv run optional/download_bert.py
"""
from transformers import BertModel, BertTokenizer

BertTokenizer.from_pretrained("bert-base-uncased")
BertModel.from_pretrained("bert-base-uncased")
print("BERT is downloaded.")
