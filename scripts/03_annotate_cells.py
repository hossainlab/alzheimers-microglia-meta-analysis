#!/usr/bin/env python3
"""Annotate cell types to identify microglial cells."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ad_microglia.analysis.cell_annotation import CellAnnotator

def main():
    print("Running cell annotation...")
    annotator = CellAnnotator()
    annotator.run_annotation()
    print("Cell annotation complete. See results in data/processed/")

if __name__ == "__main__":
    main()
