from shadowbreak.entropy_utils import compute_entropy, narrative_drift
from shadowbreak.similarity_detector import detect_similarity
from shadowbreak.constants import RED_FLAG_PHRASES

# Entropy + Narrative Drift
text1 = "He said everything was fine."
text2 = "He won’t stop texting me. I'm scared."
print("Text 1 Entropy:", compute_entropy(text1))
print("Text 2 Entropy:", compute_entropy(text2))
print("Narrative Drift:", narrative_drift(text1, text2))

# Grooming Language Detection
incoming = "Hey, let’s keep this between us okay?"
score, _ = detect_similarity(incoming, RED_FLAG_PHRASES)
print("Similarity Score to Grooming Phrases:", score)
