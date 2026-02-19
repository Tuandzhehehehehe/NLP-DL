from nlp.summarizer import Summarizer
from config import SUMMARY_MODEL

INPUT_FILE = "input.txt"
OUTPUT_FILE = "summary.txt"


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    summarizer = Summarizer(SUMMARY_MODEL)
    summary = summarizer.summarize(text)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(summary)

    print("✅ Summary saved to summary.txt")


if __name__ == "__main__":
    main()
