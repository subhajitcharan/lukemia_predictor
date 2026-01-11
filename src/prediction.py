import numpy as np
from ml_model.loader import load_model
model=load_model()
def make_Predictions(img_array):
    pred=model.predict(img_array)
    class_names = ['benign', 'malignent:early-B', 'malignent:pre-B', 'malignent:pro-B']
    predicted_class = class_names[np.argmax(pred)]
    confidence = np.max(pred)
    return predicted_class,confidence
