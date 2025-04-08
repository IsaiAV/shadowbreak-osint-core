import streamlit as st
from shadowbreak.entropy_utils import compute_entropy

st.title("🔍 Shadowbreak Entropy Scanner")
text = st.text_area("Enter Narrative Text:", height=150)

if st.button("Analyze"):
    entropy = compute_entropy(text)
    st.write(f"🧠 Entropy Score: **{entropy:.3f}**")
    if entropy > 3.5:
        st.warning("⚠️ High entropy — may indicate symbolic trauma.")
    elif entropy > 2.0:
        st.info("Moderate entropy — monitor for shifts.")
    else:
        st.success("Low entropy — low immediate concern.")

# To run this
# ---> streamlit run app/streamlit_app.py <----
