import pandas as pd
df = pd.read_csv("data/trends_clean.csv")
print("Loaded clean data")
df["engagement"] = df["num_comments"] / (df["score"] + 1)
mean_score = df["score"].mean()
df["is_popular"] = df["score"] > mean_score
print(f"Mean score: {mean_score}")
def assign_category(title):
    title = title.lower()
    if "ai" in title or "gpt" in title or "llm" in title:
        return "AI"
    elif "python" in title or "javascript" in title or "code" in title:
        return "Programming"
    elif "startup" in title or "business" in title:
        return "Business"
    elif "apple" in title or "google" in title or "tech" in title:
        return "Tech"
    else:
        return "General"

df["category"] = df["title"].apply(assign_category)
df.to_csv("data/trends_analysed.csv", index=False)
print("Saved to data/trends_analysed.csv")
print(df["category"].value_counts())
