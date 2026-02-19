class TextBuffer:
    def __init__(self):
        self.buffer = []

    def add(self, text: str):
        self.buffer.append(text)

    def get_full_text(self):
        return " ".join(self.buffer)

    def clear(self):
        self.buffer = []
