import tensorflow as tf
from pathlib import Path

model_path=Path(__file__).resolve().parent / "lukemia_prediction_model.keras"
def load_model():
    return tf.keras.models.load_model(model_path)