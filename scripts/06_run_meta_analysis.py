#!/usr/bin/env python3
"""Run meta-analysis validation across datasets."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ad_microglia.analysis.meta_analysis import main as run_meta_analysis

if __name__ == "__main__":
    run_meta_analysis()
