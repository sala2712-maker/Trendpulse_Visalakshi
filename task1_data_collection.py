import requests
import json
import os
from datetime import datetime
print("Fetching top stories...")
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)
story_ids = response.json()[:100]  # first 100 stories
all_data = []
for sid in story_ids:
    print(f"Fetching story {sid}")
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
    r = requests.get(item_url)
    data = r.json()
    all_data.append(data)
os.makedirs("data", exist_ok=True)
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"
with open(file_path, "w") as f:
    json.dump(all_data, f, indent=2)
print(f"Saved {len(all_data)} stories to {file_path}")
