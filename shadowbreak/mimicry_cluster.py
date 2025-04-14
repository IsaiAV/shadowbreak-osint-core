from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run_mimicry_analysis(input_path):
    with open(input_path, 'r') as file:
        corpus = [line.strip() for line in file if line.strip()]

    vectorizer = TfidfVectorizer().fit_transform(corpus)
    similarity_matrix = cosine_similarity(vectorizer)

    print("\n🌀 Mimicry Clustering (Cosine Similarity Matrix):\n")
    for i in range(len(corpus)):
        for j in range(i + 1, len(corpus)):
            if similarity_matrix[i][j] > 0.6:
                print(f"[MATCH] Line {i + 1} ⇄ Line {j + 1} (Similarity: {similarity_matrix[i][j]:.2f})")
