PROMPT_TEMPLATE = """
You are a question-answering assistant.

Answer the question using ONLY the context below.
If the answer is explicitly stated in the context, answer directly.
If the answer is not in the context, say: "I could not find the answer in the provided text."

Then provide one exact supporting sentence from the context.

Context:
{context}

Question:
{question}

Answer:
"""

def build_prompt(context, question):
    return PROMPT_TEMPLATE.format(context=context, question=question)