import difflib

def run_drift_scan(input_path):
    results = ["🌀 Narrative Drift Scanner Results:\n"]

    with open(input_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    for i in range(len(lines) - 1):
        ratio = difflib.SequenceMatcher(None, lines[i], lines[i + 1]).ratio()
        if ratio < 0.6:
            results.append(f"[DRIFT] Line {i+1} → {i+2}: Low similarity ({ratio:.2f}) ❗")
        else:
            results.append(f"         Line {i+1} → {i+2}: High similarity ({ratio:.2f})")
    return results

