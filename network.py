import cv2
import numpy as np
import tensorflow as tf
import pandas as pd
from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    img = img.resize((69, 69))
    return np.array(img)


# Read in data
test_data = pd.read_csv('test.csv')
train_data = pd.read_csv('train.csv')

# Split data into x and y
x_train, y_train = np.array([load_image(img) for img in train_data['Image']]), np.array(train_data['Classification'])
x_test, y_test = np.array([load_image(img) for img in test_data['Image']]), np.array(test_data['Classification'])

#Normalize data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#Create model and add layers
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(69,69)))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(3, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

model.save('galaxies.model')

loss, acc = model.evaluate(x_test, y_test)
print(f'Loss: {loss}, Accuracy: {acc}')
