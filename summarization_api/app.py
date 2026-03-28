from flask import Flask, request, jsonify
from utils.model import BartSummarizer
from utils.preprocess import clean_text
from utils.postprocess import format_summary

app = Flask(__name__)

summarizer = BartSummarizer()


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()

    if "text" not in data:
        return jsonify({"error": "Missing text"}), 400

    text = clean_text(data["text"])

    summary = summarizer.summarize(text)
    summary = format_summary(summary)

    return jsonify({"summary": summary})


if __name__ == "__main__":
    app.run(debug=True)