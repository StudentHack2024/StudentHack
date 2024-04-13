import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
import os

model = tf.keras.models.load_model('galaxies.model')

img = cv2.imread('galaxy.jpg')[:,:,0]
img = cv2.resize(img, (70,70))
img = np.array([img])
prediction = np.argmax(model.predict(img))

if prediction == 0:
    print('This is an Elliptical galaxy')
elif prediction == 2:
    print('This is a Spiral galaxy')
elif prediction ==  1:
    print('This is an Barred Spiral galaxy')
else:
    print("Hmmm")
