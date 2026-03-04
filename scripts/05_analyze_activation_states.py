#!/usr/bin/env python3
"""Analyze microglial activation states."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ad_microglia.analysis.activation_states import main as run_activation_analysis

if __name__ == "__main__":
    run_activation_analysis()
