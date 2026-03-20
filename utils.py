import re

STOP_WORDS = {
    "the", "is", "a", "an", "of", "to", "in", "and", "on", "at", "for", "with",
    "what", "who", "when", "where", "why", "how", "was", "were", "are", "be",
    "it", "this", "that", "these", "those", "as", "by", "from", "or", "but"
}

def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def clean_words(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return set(text.split()) - STOP_WORDS

def retrieve_chunks(question, chunks):
    question_words = clean_words(question)
    scored_chunks = []

    for chunk in chunks:
        chunk_words = clean_words(chunk)
        score = len(question_words & chunk_words)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])
    return scored_chunks[:3]