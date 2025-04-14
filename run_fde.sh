#!/bin/bash
clear

# Terminal Banner
echo "███████╗██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗"
echo "██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝"
echo "███████╗███████║███████║██████╔╝██████╔╝ ╚████╔╝ "
echo "╚════██║██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝  "
echo "███████║██║  ██║██║  ██║██║     ██║        ██║   "
echo "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝   "
echo ""
echo "      SHADOWBREAK OSINT INTELLIGENCE TERMINAL"
echo "------------------------------------------------"
echo "Analyst:        $USER"
echo "Hostname:       $(hostname)"

# Cross-platform uptime detection
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  UPTIME=$(uptime -p)
else
  UPTIME=$(uptime | cut -d ',' -f 1)
fi

echo "Uptime:         $UPTIME"
echo "λ∇Ψ Engine:     ACTIVE"
echo "Entropy Core:   Loaded"
echo "Access Level:   GRANTED"
echo ""

# Menu
echo "╔══════════════════════════════════════════════╗"
echo "║     Shadowbreak Field Distortion Engine      ║"
echo "╠══════════════════════════════════════════════╣"
echo "║ [1] Run Entropy Analysis                     ║"
echo "║ [2] Run Narrative Drift Analysis             ║"
echo "║ [3] Run Grooming Similarity Detection        ║"
echo "║ [4] Run Mimicry Clustering Detection         ║"
echo "║ [5] Launch Streamlit Dashboard               ║"
echo "║ [6] Run Context Shift Detection              ║"
echo "║ [7] Exit                                     ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

read -p "Choose an option: " option

case $option in
  1)
    echo "Running Entropy Analysis..."
    python3 examples/example_runner.py
    ;;
  2)
    echo "Running Narrative Drift..."
    python3 -c "from shadowbreak.entropy_utils import narrative_drift; print(narrative_drift('He said it was safe.', 'Now I don’t know who to trust.'))"
    ;;
  3)
    echo "Running Grooming Similarity Detection..."
    python3 -c "from shadowbreak.similarity_detector import detect_similarity; print(detect_similarity('Let’s keep this between us'))"
    ;;
  4)
    echo "Running Mimicry Clustering..."
    python3 -c "from shadowbreak.mimicry_cluster import run_mimicry_analysis; run_mimicry_analysis('data/sample_inputs.txt')"
    ;;
  5)
    echo "Launching Streamlit Dashboard..."
    streamlit run app/streamlit_app.py
    ;;
  6)
    echo "Running Context Shift Detection..."
    python3 -c "from shadowbreak.context_shift_detector import run_context_shift_scan; run_context_shift_scan('data/context_shift_sample.txt')"
    ;;
  7)
    echo "Goodbye, Analyst. Resonance collapsing..."
    exit 0
    ;;
  *)
    echo "Invalid option. Please try again."
    ;;
esac

