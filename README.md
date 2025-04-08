# 🧠 Shadowbreak OSINT Core

This is the official core repository for the **Shadowbreak Project’s symbolic OSINT engine**.  
It merges trauma-aware AI, symbolic semiotics, and real NLP tools to help analysts detect coercive narrative patterns, grooming language, and narrative drift in real-world digital spaces.

Built on the foundation of the **Shadow Constant (λ∇Ψ)**—a novel semiotic equation for symbolic field disruption.

---

## 🔍 What This Does

This repo includes:

- `compute_entropy()` — Calculates **linguistic entropy** from real narrative inputs
- `narrative_drift()` — Detects **trauma-linked shifts** in tone over time
- `detect_similarity()` — Uses `SentenceTransformers` to flag grooming/entrapment language
- A working **example runner** with real narrative data
- A live **Streamlit UI** for symbolic entropy scanning
- A full **unit test suite** and roadmap for expansion

---

## 🧠 Tech Stack

- Python 3.9+
- [`sentence-transformers`](https://www.sbert.net/) (MiniLM-L6-v2)
- PyTorch (as backend for sentence embeddings)
- Streamlit (UI interface)
- Custom semiotic entropy functions

---

## 📦 Project Structure

```bash
shadowbreak-osint-core/
│
├── shadowbreak/              # Core logic
│   ├── entropy_utils.py
│   ├── similarity_detector.py
│   ├── constants.py
│   └── __init__.py
│
├── examples/                 # Demo usage
│   └── example_runner.py
│
├── tests/                    # Unit tests
│   └── test_entropy.py
│
├── data/                     # Sample narrative data
│   └── sample_inputs.txt
│
├── app/                      # Streamlit dashboard (UI)
│   └── streamlit_app.py
│
├── docs/                     # Roadmap, contributors, future documentation
│   └── roadmap.md
│
├── requirements.txt          # Dependency list
├── LICENSE                   # MIT License
├── .gitignore                # Clean build handling
└── README.md                 # This file


## 🚀 Install

### 1. Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/shadowbreak-osint-core.git
cd shadowbreak-osint-core
pip install -r requirements.txt

---

## 🔗 Connect With Us

Built by the **Shadowbreak Project**, founded by:  
🧠 **Isai Valdez** — Director & Systems Architect  
📧 isaivaldez@shadowbreakproject.org  
📬 Personal: isaivaldez44@icloud.com  
🌐 Linktree: [https://linktr.ee/IsaiValdez](https://linktr.ee/IsaiValdez)  
✍️ Substack: [isaivaldez.substack.com/subscribe](https://isaivaldez.substack.com/subscribe)  
🔗 Nonprofit LinkedIn: [linkedin.com/company/shadowbreak-project](https://linkedin.com/company/shadowbreak-project)

---

We’re building this to be **super optimal**, open-source, and operational in the real world.  
If you’re a developer, OSINT analyst, trauma researcher, security expert, or just someone who cares—we’d love to collaborate.

> “We don’t just analyze data.  
> We decode the symbolic structure of harm.”

