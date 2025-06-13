import matplotlib.pyplot as plt
import seaborn as sns
import umap
from sklearn.preprocessing import LabelEncoder

def visualize_clusters(processed, predicted_labels, true_labels):
    reducer = umap.UMAP(random_state=42)
    X_umap = reducer.fit_transform(processed)

    le_true = LabelEncoder()
    y_true = le_true.fit_transform(true_labels)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, labels, title in zip(axes, [y_true, predicted_labels], ["True UniRef Clusters", "Predicted Clusters"]):
        scatter = sns.scatterplot(x=X_umap[:, 0], y=X_umap[:, 1], hue=labels, palette='tab20', s=40, ax=ax, legend=False)
        ax.set_title(title)
        ax.set_xlabel("UMAP-1")
        ax.set_ylabel("UMAP-2")

    plt.tight_layout()
    plt.show()
