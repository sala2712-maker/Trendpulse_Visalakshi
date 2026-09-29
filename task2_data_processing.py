import json
import pandas as pd
import os
import glob
print("Finding latest file...")
list_of_files = glob.glob("data/trends_*.json")
latest_file = max(list_of_files, key=os.path.getctime)
print(f"Using {latest_file}")
with open(latest_file, "r") as f:
    data = json.load(f)
df = pd.DataFrame(data)
print(df.head())
df = df.dropna(subset=["id", "title"])
df = df.fillna({"score": 0, "descendants": 0})
df = df.rename(columns={"id": "post_id", "descendants": "num_comments"})
df = df[["post_id", "title", "score", "num_comments", "by", "time", "type", "url"]]
df.to_csv("data/trends_clean.csv", index=False)
print("Saved to data/trends_clean.csv")
print(df.shape)
