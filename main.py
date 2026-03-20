from utils import chunk_text, retrieve_chunks


with open("doc.pdf", "r", encoding="utf-8") as f:
    text = f.read()

print("Document loaded successfully.")

with open("doc.pdf", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)
question = input("Ask a question: ")
top_chunks = retrieve_chunks(question, chunks)


context = "\n\n".join(chunk for score, chunk in top_chunks)

print("\nContext preview:\n")
print(context[:1000])