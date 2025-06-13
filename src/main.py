import yaml
import umap
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_fasta_sequences
from preprocessor import preprocess_sequences
from model import load_model
from inference import run_inference
from visualizer import visualize_clusters


def main():
    with open("../config.yaml", "r") as f:
        config = yaml.safe_load(f)

    data = load_fasta_sequences(f"../{config["fasta_path"]}")
    processed = preprocess_sequences(data)
    model = load_model(f"../{config["model_path"]}", processed)
    predictions = run_inference(model, processed)

    print("Inference completed. Results:", predictions)
    visualize_clusters(processed, predictions, data['cluster_id'])


if __name__ == "__main__":
    main()