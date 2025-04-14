from shadowbreak.entropy_utils import compute_entropy
from shadowbreak.similarity_detector import detect_similarity

print(compute_entropy("This is a test sentence."))
print(detect_similarity("Are you okay?", ["Everything will be fine."]))
