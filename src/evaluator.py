from sklearn.metrics import adjusted_rand_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import json

def ari_evaluate(true_labels, predicted_labels):
    le = LabelEncoder()
    true_encoded = le.fit_transform(true_labels)

    ari = adjusted_rand_score(true_encoded, predicted_labels)
    cm = confusion_matrix(true_encoded, predicted_labels)

    print(f"Adjusted Rand Index: {ari:.4f}")
    print("Confusion Matrix:")
    print(cm)

    # Save ARI to metrics
    with open("../metrics.json", "w") as f:
        json.dump({"ari": ari}, f, indent=2)


