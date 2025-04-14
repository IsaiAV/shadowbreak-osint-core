import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nlp = spacy.load("en_core_web_md")


# shadowbreak/context_shift_detector.py
def run_context_shift_scan(input_path):
    results = ["🔀 Context Shift Detector\n"]

    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    for i in range(len(lines) - 1):
        doc1 = nlp(lines[i])
        doc2 = nlp(lines[i + 1])

        vec1 = doc1.vector.reshape(1, -1)
        vec2 = doc2.vector.reshape(1, -1)

        similarity = cosine_similarity(vec1, vec2)[0][0]

        if similarity < 0.85:
            results.append(f"[SHIFT] Line {i + 1} → {i + 2}: Similarity = {similarity:.2f} ❗")
        else:
            results.append(f"         Line {i + 1} → {i + 2}: Similarity = {similarity:.2f}")

    return results


