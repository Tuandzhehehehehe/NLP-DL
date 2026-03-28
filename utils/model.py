from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class BartSummarizer:
    def __init__(self, model_path="models/fine_tuned"):
        print("🔄 Loading BART model...")

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

        print("✅ Model loaded!")

    def summarize(self, text):
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        )

        outputs = self.model.generate(
            inputs["input_ids"],
            max_length=120,
            min_length=40,
            num_beams=4,
            no_repeat_ngram_size=3,
            length_penalty=2.0,
            early_stopping=True
        )

        summary = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return summary