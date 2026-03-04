#!/usr/bin/env python3
"""Integrate datasets using scVI or Scanorama."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ad_microglia.integration.integration import main as run_integration

if __name__ == "__main__":
    run_integration()
