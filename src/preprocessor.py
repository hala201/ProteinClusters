def preprocess_sequences(data):
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder

    # Simple example: convert sequences to amino acid frequencies
    amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
    encoded = []
    for seq in data['sequence']:
        vec = [seq.count(aa) / len(seq) for aa in amino_acids]
        encoded.append(vec)
    return np.array(encoded)