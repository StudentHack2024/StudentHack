import pandas as pd

import os

mapping = pd.read_csv("gz2_filename_mapping.csv")
df = pd.read_csv("gz2_hart16.csv")
df = df[["dr7objid", "gz2_class"]]
mapping = mapping[mapping["sample"] == "original"] # Only use the original sample

mapped = pd.merge(left=df, right=mapping, left_on="dr7objid", right_on="objid")
mapped = mapped.drop(columns=["dr7objid", "sample"])

images = []
classifications = []


for filename in os.listdir("./images_gz2/images/"):
    entry = mapped[mapped["asset_id"] == int(filename[:-4])]
    if len(entry) > 0:
        images.append(filename)
        classification = entry.iloc[0].gz2_class
        new_class = ""
        for char in classification:
            if char.isupper():
                new_class += char 

        if new_class == "E":
            classification = "Eliptical"
        elif new_class == "SB":
            classification = "Spiral"
        else:
            classification = "Barred Spiral"
        classifications.append(classification)

results = pd.DataFrame(classifications, images).reset_index()
results.columns=["Image", "Classification"]

results.to_csv("image_classification.csv", index=False)