from entropy_utils import compute_entropy, narrative_drift
from similarity_detector import detect_similarity

# Example: Entropy Scan
text1 = "He said everything was fine."
text2 = "He won’t stop texting me. I'm scared."
print("Text 1 Entropy:", compute_entropy(text1))
print("Text 2 Entropy:", compute_entropy(text2))
print("Narrative Drift:", narrative_drift(text1, text2))

# Example: Grooming Language Detection
flagged = [
    "Don't tell anyone",
    "You're so mature for your age",
    "This is our secret"
]
incoming = "Hey, let’s keep this between us okay?"
sim_score, sim_matrix = detect_similarity(incoming, flagged)
print("Max Similarity to Red Flags:", sim_score)
