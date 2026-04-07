from transformers import BartTokenizer, BartForConditionalGeneration

class BartSummarizer:
    def __init__(self, model_path="models/fine_tuned"):
        self.tokenizer = BartTokenizer.from_pretrained(model_path)
        self.model = BartForConditionalGeneration.from_pretrained(model_path)

    def summarize(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )

        summary_ids = self.model.generate(
            inputs["input_ids"],
            max_length=120,
            min_length=40,
            num_beams=6,
            length_penalty=1.2,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)