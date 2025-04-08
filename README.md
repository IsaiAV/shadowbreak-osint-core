# Shadowbreak OSINT Core 

This is the official core repository for the Shadowbreak Project’s symbolic OSINT engine. It merges trauma-aware AI, symbolic semiotics, and real NLP tools to help analysts detect coercive narrative patterns and grooming language online.

##  What This Does

This repo includes:

- `compute_entropy()` — calculates linguistic entropy from real narrative inputs
- `narrative_drift()` — detects trauma-linked shifts in tone over time
- `detect_similarity()` — uses SentenceTransformers to flag grooming/entrapment language
- A working example runner with real narrative data

## Tech Stack

- Python 3.9+
- [sentence-transformers](https://www.sbert.net/)
- PyTorch (as backend for sentence embeddings)

## Install

Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/shadowbreak-osint-core.git
cd shadowbreak-osint-core
pip install -r requirements.txt
