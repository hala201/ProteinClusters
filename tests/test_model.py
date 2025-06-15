from model import load_model
from inference import run_inference
import numpy as np

def test_model_inference():
    dummy = load_model("tests/models/test.pkl", [[0]*20, [1]*20], 2)
    preds = run_inference(dummy, np.array([[0]*20, [1]*20]))
    assert len(preds) == 2
