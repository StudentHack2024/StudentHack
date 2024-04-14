import cv2
import numpy as np
import tensorflow as tf
import os

def classify_img(image):
    model = tf.keras.models.load_model('galaxies.keras')
    img = cv2.imread(image)[:,:,0]
    img = cv2.resize(img, (70,70))
    img = np.array([img])
    prediction = np.argmax(model.predict(img))
    return prediction

