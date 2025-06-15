from sklearn.cluster import KMeans
import joblib

def load_model(path, X):
    model = KMeans(n_clusters=5, random_state=42)
    model.fit(X)

    joblib.dump(model, path)
    return joblib.load(path)