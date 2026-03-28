def format_summary(text):
    text = text.strip()
    if not text.endswith("."):
        text += "."
    return text