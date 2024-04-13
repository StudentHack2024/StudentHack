import pandas as pd

import os

df = pd.read_csv("image_classification.csv")
df = df.sort_values(by='Image', ascending=True)

train_data = df.iloc[:int(len(df)*0.8)]
test_data = df.iloc[int(len(df)*0.8):]

train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)