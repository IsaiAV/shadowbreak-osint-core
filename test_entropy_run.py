import sys
from shadowbreak.entropy_utils import compute_entropy

if len(sys.argv) < 2:
    print("Usage: python test_entropy_run.py 'your text here'")
    sys.exit(1)

text = sys.argv[1]
result = compute_entropy(text)
print("Entropy Result:", result)
