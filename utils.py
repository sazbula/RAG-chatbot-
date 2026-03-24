import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def chunk_text(text, chunk_size=800, overlap=150):
    # Split the full text into sentences using punctuation (. ! ?)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = ""
    # Build chunks by adding full sentences one by one
    for sentence in sentences:
        # If adding the next sentence keeps us within the size limit
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "
        else:
        # Otherwise, save the current chunk and start a new one
            chunks.append(current_chunk.strip())

            # keep last part of previous chunk as overlap
            overlap_text = current_chunk[-overlap:]
            
            # start new chunk with overlap + new sentence
            current_chunk = overlap_text + sentence + " "
            
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks



def retrieve_chunks_tfidf(question, chunks, k=5):
    #tokenize text, remove common english stopwords, compute tf idf scores
    vectorizer = TfidfVectorizer(stop_words="english")
    #each chunk is made into a list of numbers, that represent the importance of words
    chunk_vectors = vectorizer.fit_transform(chunks)
    #using the same vocab as the chunks, converts questions into numbers 
    question_vector = vectorizer.transform([question])

    # computes similarity between questions and each chunk vector
    similarities = cosine_similarity(question_vector, chunk_vectors).flatten()
    #returns a list of pairs of chunk,score
    scored_chunks = list(zip(similarities, chunks))
    #keeps only chunk w similarity above 0 , sorts and returns
    scored_chunks = [item for item in scored_chunks if item[0] > 0]
    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    return scored_chunks[:k]