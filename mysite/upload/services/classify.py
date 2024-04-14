import cv2
import numpy as np
import tensorflow as tf
import os
from django.templatetags.static import static

def classify_img(image):
    url = "upload" + static('galaxies.weights.h5')

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (100,100,1)))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Conv2D(64, (3,3), activation = 'relu'))
    model.add(tf.keras.layers.MaxPooling2D((2,2)))
    model.add(tf.keras.layers.Conv2D(128, (3,3), activation = 'relu'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(128, activation="relu"))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(3, activation="softmax"))
    model.load_weights(url)
    file = image.file
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), 1)
    img = cv2.resize(img, (100,100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.array([img])
    prediction = np.argmax(model.predict(img))
    return prediction

