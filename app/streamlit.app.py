# app/streamlit_app.py

import streamlit as st
from shadowbreak.entropy_utils import compute_entropy
from shadowbreak.similarity_detector import detect_similarity
from shadowbreak.narrative_drift import run_drift_scan
from shadowbreak.context_shift_detector import run_context_shift_scan

st.set_page_config(page_title="Shadowbreak OSINT Dashboard", layout="wide")

st.title("🧠 Shadowbreak OSINT Scanner")
st.markdown("Paste text below to analyze symbolic narrative patterns.")

text_input = st.text_area("Input Narrative Text", height=300)

# --------------------------
# 🔹 Entropy Scan
# --------------------------
if st.button("Run Entropy Scan"):
    if text_input:
        entropy = compute_entropy(text_input)
        st.success(f"Linguistic Entropy: **{entropy:.4f}**")
    else:
        st.warning("Please input narrative text.")

# --------------------------
# 🔹 Grooming Similarity Check
# --------------------------
if st.button("Run Grooming Similarity Check"):
    if text_input:
        flagged = ["You can trust me", "Don't tell anyone", "You're special"]
        results = detect_similarity(text_input, flagged)

        st.info("Similarity Scores to Grooming Phrases:")
        for phrase, score in results:
            st.write(f"**{phrase}** → Score: **{score:.4f}**")
    else:
        st.warning("Please input narrative text.")



# --------------------------
# 🔹 Narrative Drift Detection
# --------------------------
# 🔹 Narrative Drift Detection
if st.button("Run Narrative Drift Detection"):
    if text_input:
        with open("data/entropy_inputs.txt", "w") as f:
            f.write(text_input.strip())
        output = run_drift_scan("data/entropy_inputs.txt")

        st.subheader("🌀 Narrative Drift Results")
        for line in output:
            st.write(line)
    else:
        st.warning("Please input narrative text.")


# 🔹 Context Shift Detection
if st.button("Run Context Shift Detection"):
    if text_input:
        with open("data/context_shift_sample.txt", "w") as f:
            f.write(text_input.strip())
        output = run_context_shift_scan("data/context_shift_sample.txt")

        st.subheader("🔀 Context Shift Results")
        for line in output:
            st.write(line)
    else:
        st.warning("Please input narrative text.")


