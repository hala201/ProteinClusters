from sklearn.cluster import KMeans
import joblib

def load_model(path, X, n_clusters=5):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)

    joblib.dump(model, path)
    return joblib.load(path)