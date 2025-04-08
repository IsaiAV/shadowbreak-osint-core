from collections import Counter
import math

def compute_entropy(text):
    """
    Calculates the Shannon entropy of a given text.
    """
    tokens = text.lower().split()
    freq = Counter(tokens)
    total = sum(freq.values())
    entropy = -sum((count/total) * math.log2(count/total) for count in freq.values())
    return entropy

def narrative_drift(text1, text2):
    """
    Calculates the absolute entropy difference (drift) between two text inputs.
    """
    e1 = compute_entropy(text1)
    e2 = compute_entropy(text2)
    return abs(e2 - e1)
