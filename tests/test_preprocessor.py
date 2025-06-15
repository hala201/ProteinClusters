from preprocessor import preprocess_sequences
import pandas as pd

def test_preprocessing_shape():
    df = pd.DataFrame({"sequence": ["PA", "HEMA"]})
    X = preprocess_sequences(df)
    print(X.shape)
    assert X.shape == (2, 20)
