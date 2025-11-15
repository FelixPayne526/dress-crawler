import pandas as pd, random, numpy as np

# ① 读你现成的 48 条真数据
real = pd.read_csv("page1.csv")

# ② 随机采样+抖动生成 5000 条
np.random.seed(42)
rows = []
for _ in range(5000):
    base = real.sample(1).iloc[0]          # 随机选 1 条真数据
    price = round(base.price * random.uniform(0.8, 1.2), 2)   # 价格±20%
    rating = round(min(5.0, base.rating + random.uniform(-0.5, 0.5)), 1)
    reviews = int(base.review_count * random.uniform(0.5, 2.0))
    # 生成新 ASIN（B0 + 10 位随机大写）
    asin = "B0" + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10))
    rows.append([asin, base.title, price, rating, reviews])

# ③ 保存仿真 5000 条
df = pd.DataFrame(rows, columns=["asin", "title", "price", "rating", "review_count"])
df.to_csv("dress_bs_5000.csv", index=False)
print("完事！共保存", len(df), "条仿真数据")