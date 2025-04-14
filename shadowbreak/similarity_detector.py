from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def detect_similarity(input_text, flagged_phrases):
    results = []
    for phrase in flagged_phrases:
        embeddings = model.encode([input_text, phrase], convert_to_tensor=True)
        score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
        results.append((phrase, score))
    return results


