from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from .text_utils import chunk_text
from ..config import SUMMARY_RATIO, CHUNK_WORDS

import torch


class Summarizer:
    def __init__(self, model_name="sshleifer/distilbart-cnn-12-6"):
        print("🔹 Loading summarization model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        print("✅ Model loaded")

    def _summarize_once(self, text, max_len, min_len):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=1024
        )

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    def summarize(self, text: str) -> str:
        if not text.strip():
            return ""

        chunks = chunk_text(text, CHUNK_WORDS)
        summaries = []

        for chunk in chunks:
            max_len = int(len(chunk.split()) * SUMMARY_RATIO)
            min_len = max(30, int(max_len * 0.4))

            s = self._summarize_once(chunk, max_len, min_len)
            summaries.append(s)

        return "\n".join(summaries)
