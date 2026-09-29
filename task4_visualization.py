import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv("data/trends_analysed.csv")
os.makedirs("outputs", exist_ok=True)
plt.figure()
df["category"].value_counts().plot(kind="bar")
plt.title("Posts per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.savefig("outputs/category_count.png")
print("Saved category_count.png")

plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Num Comments")
plt.savefig("outputs/score_vs_comments.png")
print("Saved score_vs_comments.png")
plt.figure()
df["is_popular"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Popular vs Not Popular")
plt.savefig("outputs/popular_pie.png")
print("Saved popular_pie.png")

print("All visualizations done")
