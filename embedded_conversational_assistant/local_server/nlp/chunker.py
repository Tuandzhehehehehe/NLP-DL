def chunk_text(text: str, max_words: int = 200):
    """
    Chia văn bản dài thành nhiều đoạn nhỏ theo số từ
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks
