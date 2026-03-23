from utils import chunk_text, retrieve_chunks
from prompt import build_prompt
import requests


# load document 
with open("doc.pdf", "r", encoding="utf-8") as f:
    text = f.read()

print("Document loaded successfully.")

# chunking
chunks = chunk_text(text)

# user question
question = input("Ask a question: ")

# retrieval
top_chunks = retrieve_chunks(question, chunks)

# build context 
context = "\n\n".join(chunk for score, chunk in top_chunks)

# build prompt
prompt = build_prompt(context, question)

# preview
#print("\n--- PROMPT PREVIEW ---\n")
#print(prompt)


# using the LLM 
response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
)

answer = response.json()["response"]

print("\n--- ANSWER ---\n")
print(answer)



