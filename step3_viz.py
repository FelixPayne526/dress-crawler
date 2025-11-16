import pandas as pd, matplotlib.pyplot as plt, seaborn as sns

df = pd.read_csv("dress_bs_5000.csv")

# 1. 价格分布
plt.figure(figsize=(6,4))
sns.histplot(df["price"], bins=30, kde=True, color="skyblue").set_title("Price Distribution")
plt.savefig("price_dist.png", dpi=300)
plt.close()

# 2. 评分分布
plt.figure(figsize=(5,4))
sns.histplot(df["rating"], bins=10, kde=True, color="orange").set_title("Rating Distribution")
plt.savefig("rating_dist.png", dpi=300)
plt.close()

# 3. Top10 价格段
top10 = df["price"].round(-1).value_counts().head(10)
plt.figure(figsize=(5,4))
top10.plot(kind="barh", color="green").set_title("Top10 Price Bands ($)")
plt.savefig("top10_price.png", dpi=300)
plt.close()

print("3 张图已保存：price_dist.png、rating_dist.png、top10_price.png")