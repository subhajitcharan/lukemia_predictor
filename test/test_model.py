import numpy as np
import tensorflow as tf
from ml_model.loader import load_model
from main import computation
test_img="WBC-Malignant-Pre-024.jpg"
def test_loding():
    model=load_model()
    assert model is not None
    assert isinstance(model, tf.keras.Model)
def test_model():
    model=load_model()
    dummy_input = np.random.rand(1, 224, 224, 3).astype("float32")
    pred=model.predict(dummy_input)
    assert pred is not None

def test_computation():
    prediction,confidence=computation("test/WBC-Malignant-Pre-024.jpg")
    assert prediction is not None
    assert confidence is not None

