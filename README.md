# 🧠 Shadowbreak OSINT Core

This is the official core repository for the **Shadowbreak Project’s symbolic OSINT engine**.  
It merges trauma-aware AI, symbolic semiotics, and real NLP tools to help analysts detect coercive narrative patterns, grooming language, and narrative drift in real-world digital spaces.

Built on the foundation of the **Shadow Constant (λ∇Ψ)**—a novel semiotic equation for symbolic field disruption.

---

## 🔍 What This Does

This repo includes:

- `compute_entropy()` — Calculates **linguistic entropy** for narrative segments
- `narrative_drift()` — Detects **symbolic tone shifts** and potential trauma ruptures
- `detect_similarity()` — Flags **grooming or coercive language patterns**
- `mimicry_cluster()` — Clusters **linguistically altered duplications** to find mimic traps
- `context_shift_detector()` — Detects **subtle context changes** in multi-turn inputs
- `symbolic_field_analysis()` — Core λ∇Ψ system for symbolic semiotic compression

---

## 🧠 Tech Stack

- Python 3.11+
- [`sentence-transformers`](https://www.sbert.net/)
- `spacy`, `numpy`, `torch`, `streamlit`
- Custom symbolic entropy models built for trauma analysis
- Fully terminal-operable via `run_fde.sh`

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
git clone https://github.com/IsaiAV/shadowbreak-osint-core.git
cd shadowbreak-osint-core
pip install -r requirements.txt

---

🧠 Launch Shadowbreak Terminal Interface

After cloning the repo, make the launcher script executable:

```bash
chmod +x run_fde.sh

---

Then launch the Shadowbreak OSINT Intelligence Terminal:

./run_fde.sh

---

## 🧪 Quick Test: Run Entropy Analysis

After installing, you can test the symbolic entropy engine with a single script:

```bash
python test_entropy_run.py

---

Or pass your own sentence directly via CLI:

python test_entropy_run.py "This narrative reveals signs of grooming tactics masked as care."

This runs the core entropy analysis module and outputs a symbolic entropy score based on the Shadow Constant equation (λ∇Ψ).


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

