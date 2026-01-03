import tensorflow as tf
import numpy as np
def processing(img):
    img = tf.keras.utils.load_img(img, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array