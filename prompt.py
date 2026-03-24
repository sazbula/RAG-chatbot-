PROMPT_TEMPLATE = """
You are a question-answering assistant.

Answer the question using ONLY the context below.
If the answer is explicitly stated in the context, answer directly.
If the answer is not in the context, say: "I could not find the answer in the provided text."

Then provide one exact supporting sentence from the context, and quote it.


MUST format:
If the answer is found in the context, write:

Answer: <one clear sentence answering the question>

Supporting sentence from context: "<exact sentence copied from the context>"

If the answer is NOT found in the context, write:

Answer: I could not find the answer in the provided context.
Supporting sentence from context: "None"

Context:
{context}

Question:
{question}

Answer:
"""

def build_prompt(context, question):
    return PROMPT_TEMPLATE.format(context=context, question=question)