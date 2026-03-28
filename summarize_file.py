from utils.model import BartSummarizer
from utils.preprocess import clean_text
from utils.postprocess import format_summary

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def main():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            text = f.read()

        if not text.strip():
            print("❌ File rỗng")
            return

        text = clean_text(text)

        summarizer = BartSummarizer()
        summary = summarizer.summarize(text)
        summary = format_summary(summary)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(summary)

        print("✅ Done!")
        print("📁 Output:", OUTPUT_FILE)

    except Exception as e:
        print("🔥 Lỗi:", str(e))


if __name__ == "__main__":
    main()