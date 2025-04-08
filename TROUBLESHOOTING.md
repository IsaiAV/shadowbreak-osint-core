# 🛠️ Shadowbreak OSINT Core — Troubleshooting & Setup Guide

Welcome to the Shadowbreak OSINT Core engine.  
This system includes entropy analysis, trauma-aware narrative detection, and real-time NLP similarity scanning.

Below are some common issues users may encounter during setup, with clear and tested fixes to ensure a smooth launch.

---

## 🔍 Common Setup Issues & Fixes

---

### ❗ Error: `ModuleNotFoundError: No module named 'shadowbreak'`

**What’s happening:**  
Python doesn’t recognize the local folder structure as a valid package path.

**Fix:**

From the root of the repo, set your Python path:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)

This makes sure Python can import from your local shadowbreak/ folder when running scripts like example_runner.py.

---

❗ Error: `Narrative drift test fails with 0.0 not greater than 0` 

What’s happening:

The test sentences used may be too semantically similar, producing no meaningful entropy difference.

Fix:

Edit the tests/test_entropy.py file to include more emotionally contrasting text examples.

Example:

t1 = "Everything is fine and calm."
t2 = "I can't sleep. I'm scared. They're watching me."

then rerun:

python3 -m unittest discover tests

---

❗ Error: zsh: command not found: streamlit

What’s happening:

Streamlit is not yet installed on your system.

Fix:
Install it with:

python3 -m pip install streamlit

---

❗ Error: File does not exist: app/streamlit_app.py

What’s happening:

Maybe you just have a typo. So always double check 

Fix:

app/streamlit.app.py

You should see a live dashboard in your browser at http://localhost:8501

---

❗ Error: fatal: 'orgin' does not appear to be a git repository

What’s happening:

This is a simple typo—origin was misspelled as orgin.

Fix:

Use the correct push command:


git push -u origin main

---

✅ Pro Tip: Test Everything in Order


1. Install requirements
python3 -m pip install -r requirements.txt

2. Run the example 
python3 examples/example_runner.py

3.Run the unit tests
python3 -m unittest discover tests

4. Launch the Streamlit UI
streamlit run app/streamlit_app.py

This guide is maintained by the Shadowbreak Project for community ease of use.
If you encounter any additional issues, feel free to submit an Issue or PR.

Together, we’re decoding the symbolic structure of harm.

— Shadowbreak Project

