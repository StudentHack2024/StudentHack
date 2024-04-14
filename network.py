import cv2
import numpy as np
import tensorflow as tf, keras.preprocessing.image as image
import pandas as pd
import random

def load_image(image_path):
    img = image.load_img("./images/" + image_path, target_size=(100, 100), color_mode='grayscale')
    img = img.rotate(random.randint(-180, 180))
    img = np.asarray(img)
    return img


# Read in data
test_data = pd.read_csv('test_data.csv', nrows=7000)
train_data = pd.read_csv('train_data.csv', nrows=30000)

# Split data into x and y
x_train, y_train = np.array([load_image(img) for img in train_data['Image']]), np.array(train_data['Classification'])
x_test, y_test = np.array([load_image(img) for img in test_data['Image']]), np.array(test_data['Classification'])

#Normalize data
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#Create model and add layers
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

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.save_weights('galaxies.weights.h5')

loss, acc = model.evaluate(x_test, y_test)
print(f'Loss: {loss}, Accuracy: {acc}')
