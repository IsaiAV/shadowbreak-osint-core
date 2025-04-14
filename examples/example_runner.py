from shadowbreak.entropy_utils import compute_entropy, narrative_drift

# Load input safely
with open("data/entropy_inputs.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

print("\n📊 Entropy Scores:\n")
for i, line in enumerate(lines):
    try:
        entropy = compute_entropy(line)
        print(f"Line {i + 1}: {entropy:.4f}")
    except Exception as e:
        print(f"Error in Line {i + 1}: {e}")

print("\n📈 Narrative Drift Between Lines:\n")
for i in range(len(lines) - 1):
    try:
        drift = narrative_drift(lines[i], lines[i + 1])
        print(f"Line {i + 1} → {i + 2}: Drift = {drift:.4f}")
    except Exception as e:
        print(f"Error in Drift from Line {i + 1} → {i + 2}: {e}")
