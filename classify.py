import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
import os

model = tf.keras.models.load_model('galaxies.model')

img = cv2.imread('galaxy.jpg')[:,:,0]
img = cv2.resize(img, (69,69))
img = np.array([img])
prediction = np.argmax(model.predict(img))

if prediction == 'Elliptical':
    print('This is an Elliptical galaxy')
elif prediction == 'Spiral':
    print('This is a Spiral galaxy')
elif prediction == 'Irregular':
    print('This is an Irregular galaxy')
else:
    print("Hmmm")
