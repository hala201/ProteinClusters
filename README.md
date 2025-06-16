# Protein Clustering Pipeline with DVC, UMAP, and KMeans

This project demonstrates a reproducible, containerized machine learning pipeline to cluster protein sequences from the [UniRef50](https://www.uniprot.org/help/uniref) dataset using KMeans. It leverages UMAP for dimensionality reduction and DVC for pipeline orchestration and data versioning.

## Stack

- Language: Python 3.10
- Workflow Orchestration: DVC
- Cluster Model: KMeans (scikit-learn)
- Visualization: UMAP and Seaborn
- Version Control: Git with DVC and S3 remote
- CI/CD: GitHub Actions
- Containerization: Docker

## Project Structure
```
ProteinClusters/
├── src/ # Core logic (data, model, pipeline)
│ ├── main.py
│ ├── data_loader.py
│ ├── preprocessor.py
│ ├── model.py
│ ├── inference.py
│ ├── visualize.py
│ └── evaluator.py
├── tests/ # Unit tests
├── data/ # Input FASTA files (DVC tracked)
├── models/ # Output models (DVC tracked)
├── visualizations/ # Stores visualization
├── dvc.yaml # Pipeline definition
├── params.yaml # Model parameters
├── metrics.json # Evaluation metrics (ARI)
├── requirements.txt
├── Dockerfile
└── README.md # You're here
```

## Reproducibility with DVC

This pipeline is defined in `dvc.yaml`. All intermediate and final artifacts — from preprocessed tensors to trained models — are versioned and reproducible with the following commands:

```bash
dvc pull        # Pull data and model artifacts from S3
dvc repro       # Reproduce the entire pipeline
dvc push        # Push updated outputs to remote
```

## CI/CD Workflow
Every push or pull request triggers a GitHub Actions workflow that:

- Pulls artifacts from the DVC remote
- Reproduces the pipeline with dvc repro
- Runs unit tests
- Pushes new outputs (models and metrics)

The workflow is defined in .github/workflows/ml-pipeline.yml.

## Metrics and Visualization
The pipeline outputs include:

metrics.json: Captures Adjusted Rand Index (ARI) between predicted and true clusters

UMAP scatterplots: 2D visualizations of embedded protein vectors, colored by true and predicted labels

## Testing
Run unit tests with:

`PYTHONPATH=src pytest`

The test suite validates:
- FASTA file parsing
- Feature preprocessing
- Model inference

## Containerization
To run the project in a container:

```
docker build -t protein-pipeline .
docker run protein-pipeline
```
## Data
The input dataset is a curated subset of UniRef50, filtered to five protein families with approximately 20 sequences each. All data is managed and versioned with DVC and stored in an S3 remote.

## Why This Matters
An AI-first approach to healthcare requires ML infrastructure that is reproducible, auditable, and production-ready. This project simulates those demands by integrating model versioning, pipeline automation, and compliance-friendly traceability, while operating on noisy biological data like protein sequences.

The pipeline is modular, version-controlled, CI-enforced, and production-reproducible, built to meet real-world standards in high-impact, regulated environments.