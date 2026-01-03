import tensorflow as tf
import numpy as np
model=tf.keras.models.load_model("./ml_model/lukemia_prediction_model.keras")
def make_Predictions(img_array):
    pred=model.predict(img_array)
    class_names = ['benign', 'early', 'pre', 'pro']
    predicted_class = class_names[np.argmax(pred)]
    confidence = np.max(pred)
    return predicted_class,confidence
