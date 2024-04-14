import cv2
import numpy as np
import tensorflow as tf
import os
from django.templatetags.static import static


# url = os.path.join(settings.BASE_DIR, '/galaxies.keras')

def classify_img(image):
    url = "upload" + static('galaxies.weights.h5')
    print(url)
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(100, 100)))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))
    model.load_weights(url)
    file = image.file
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), 1)
    img = cv2.resize(img, (100,100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.array([img])
    prediction = np.argmax(model.predict(img))
    return prediction

