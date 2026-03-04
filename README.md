# Alzheimer's Disease Microglia Meta-Analysis

## Overview

A comprehensive meta-analysis of microglial activation states across multiple Alzheimer's disease (AD) single-cell RNA-sequencing studies. This pipeline identifies conserved microglial activation programs that are reproducible across datasets, species, and experimental conditions.

## Research Question

**Are there conserved microglial activation states across Alzheimer's single-cell studies?**

## Key Findings (Expected)

1. **3-5 conserved microglial activation states** identified across all datasets, including:
   - **Homeostatic microglia** — characterized by core markers (CX3CR1, P2RY12, TMEM119)
   - **Disease-associated microglia (DAM)** — upregulation of TREM2, APOE, LPL, SPP1
   - **Inflammatory microglia** — enriched in cytokine/chemokine signaling (IL1B, TNF, CCL2)
   - **Proliferative microglia** — cell-cycle gene enrichment (MKI67, TOP2A)
   - **Interferon-responsive microglia** — ISG signature (IFIT1, ISG15, MX1)
2. **Cross-species conservation** — Major activation programs (DAM, inflammatory) conserved between human and mouse
3. **Statistical validation** — Fixed-effects meta-analysis confirms conservation across studies (I² heterogeneity assessment, p < 0.05)
4. **Gene signatures** — 50-200 differentially expressed genes per activation state
5. **Pathway enrichment** — Functional annotation revealing neuroinflammation, phagocytosis, lipid metabolism, and complement pathways

## Methods

### Study Design

Cross-study meta-analysis of 5 publicly available scRNA-seq datasets from GEO, spanning human and mouse AD models.

### Computational Pipeline

| Step | Method | Tool/Algorithm |
|------|--------|---------------|
| Quality control | Cell/gene filtering | Scanpy (min 200 genes/cell, <20% MT, min 1000 counts) |
| Normalization | CPM + log1p | Scanpy (target_sum=10,000) |
| Cell annotation | Automated classification | CellTypist (Immune_All_High model) |
| Microglial filtering | Marker validation | CX3CR1, P2RY12, TMEM119 expression |
| Batch integration | Deep generative model | scVI (n_latent=30, n_layers=2, max_epochs=400) |
| Batch integration (alt.) | Mutual nearest neighbors | Scanorama |
| Clustering | Community detection | Leiden algorithm (multi-resolution 0.1-1.0) |
| Resolution selection | Cluster quality | Silhouette score optimization |
| Differential expression | Rank-based test | Wilcoxon rank-sum (min log2FC=0.25) |
| Pathway enrichment | Gene set analysis | decoupler + MSigDB |
| Meta-analysis | Pooled effect estimation | Fixed-effects model with Wilson score CIs |
| Heterogeneity testing | Consistency metric | I² statistic |

### Statistical Framework

- **Effect sizes**: Activation state proportions per dataset with Wilson score confidence intervals
- **Meta-analysis**: Fixed-effects model for pooled proportion estimates
- **Conservation testing**: Cross-dataset reproducibility with statistical significance testing
- **Multiple testing correction**: Applied where appropriate

## Datasets

| GEO ID | Reference | Species | Tissue | Condition |
|--------|-----------|---------|--------|-----------|
| [GSE98969](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE98969) | Keren-Shaul et al. (2017) | Mouse | Whole brain | AD model |
| [GSE103334](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103334) | Mathys et al. (2019) | Human | Hippocampus | AD |
| [GSE135437](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE135437) | Sankowski et al. (2019) | Human | Cortex | AD |
| [GSE157827](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE157827) | Leng et al. (2021) | Human | Prefrontal cortex | AD |
| [GSE129788](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE129788) | — | Mouse | Brain | Aging |

## Project Structure

```
alzheimers-microglia-meta-analysis/
├── src/ad_microglia/              # Installable Python package
│   ├── config/settings.py         # Centralized configuration
│   ├── data/
│   │   ├── download.py            # GEO dataset downloading
│   │   └── preprocessing.py       # QC, normalization, HVG, PCA
│   ├── integration/
│   │   └── integration.py         # scVI & Scanorama integration
│   ├── analysis/
│   │   ├── cell_annotation.py     # CellTypist annotation + marker validation
│   │   ├── activation_states.py   # Leiden clustering, DE, pathway enrichment
│   │   └── meta_analysis.py       # Fixed-effects meta-analysis, conservation
│   └── utils/
│       └── plot_manager.py        # Publication-quality figure management
├── scripts/                       # Pipeline entry points
│   ├── 01_download_data.py
│   ├── 02_preprocess_data.py
│   ├── 03_annotate_cells.py
│   ├── 04_integrate_datasets.py
│   ├── 05_analyze_activation_states.py
│   ├── 06_run_meta_analysis.py
│   └── run_full_pipeline.py       # Run all steps sequentially
├── config/
│   ├── datasets.yaml              # Dataset metadata (5 studies)
│   └── analysis_params.yaml       # All analysis parameters
├── data/
│   ├── raw/                       # Downloaded GEO datasets
│   ├── processed/                 # Processed .h5ad files
│   └── metadata/                  # Dataset metadata
├── results/
│   ├── figures/                   # Publication-quality plots (by category)
│   ├── tables/                    # Statistical results & gene signatures
│   ├── reports/                   # Analysis summary reports
│   └── meta_analysis/             # Forest plots, conservation results
├── plots/                         # Organized plot outputs (PlotManager)
├── tests/                         # pytest test suite
├── docs/                          # Analysis protocol & installation guide
├── pyproject.toml                 # Package configuration (PEP 518)
└── environment.yml                # Conda environment specification
```

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd alzheimers-microglia-meta-analysis

# Option 1: pip (recommended)
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"

# Option 2: conda
conda env create -f environment.yml
conda activate ad-microglia
pip install -e .
```

## Usage

### Full Pipeline

```bash
python scripts/run_full_pipeline.py
# Options:
#   --skip-download          Skip data download step
#   --integration-method scvi|scanorama
```

### Step-by-Step

```bash
python scripts/01_download_data.py
python scripts/02_preprocess_data.py
python scripts/03_annotate_cells.py
python scripts/04_integrate_datasets.py
python scripts/05_analyze_activation_states.py
python scripts/06_run_meta_analysis.py
```

### Configuration

All parameters are configurable via:
- `config/analysis_params.yaml` — Analysis parameters
- `config/datasets.yaml` — Dataset metadata
- `.env` file — Environment variable overrides (see `.env.example`)

## Key Outputs

| Output | Path | Description |
|--------|------|-------------|
| Meta-analysis results | `results/meta_analysis/meta_analysis_results.csv` | Pooled effect sizes and CIs |
| Gene signatures | `results/tables/gene_signatures/conserved_signatures.csv` | Conserved activation state genes |
| DE markers | `results/tables/activation_state_markers.csv` | Per-state marker genes |
| Forest plots | `results/meta_analysis/forest_plots.pdf` | Meta-analysis visualization |
| Conservation plots | `results/meta_analysis/conservation_significance.pdf` | Cross-study conservation |
| Analysis figures | `results/figures/activation_states/` | UMAP, heatmaps, dot plots |
| Summary reports | `results/reports/` | Markdown analysis summaries |

## Testing

```bash
# Quick single-dataset test
python -m pytest tests/test_quick.py -v

# Full pipeline tests
python -m pytest tests/ -v
```

## References

1. Lopez, R., Regier, J., Cole, M.B., Jordan, M.I. & Yosef, N. Deep generative modeling for single-cell transcriptomics. *Nat. Methods* **15**, 1053-1058 (2018).
2. Hie, B., Bryson, B. & Berger, B. Efficient integration of heterogeneous single-cell transcriptomes using Scanorama. *Nat. Biotechnol.* **37**, 685-691 (2019).
3. Dominguez Conde, C. et al. Cross-tissue immune cell analysis reveals tissue-specific features in humans. *Science* **376**, eabl5197 (2022).
4. Borenstein, M., Hedges, L.V., Higgins, J.P.T. & Rothstein, H.R. *Introduction to Meta-Analysis* (John Wiley & Sons, 2009).
5. Wilson, E.B. Probable inference, the law of succession, and statistical inference. *J. Am. Stat. Assoc.* **22**, 209-212 (1927).

## License

This project is for research purposes. Dataset usage is subject to original publication terms.
