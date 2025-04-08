from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def detect_similarity(input_text, flagged_phrases):
    embeddings = model.encode([input_text] + flagged_phrases, convert_to_tensor=True)
    similarities = util.cos_sim(embeddings[0], embeddings[1:])
    return similarities.max().item(), similarities.tolist()
