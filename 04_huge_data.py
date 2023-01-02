import pandas as pd
import time

start = time.time()
train = pd.read_csv("./transactions_train.csv")
end = time.time()
print(f"loading time: {end-start} secs.")
# print(train)

# mem_usage = train.memory_usage(deep=True).sum() / 1024 / 1024 /1024
# print(f"Memory Usage: {mem_usage:.4} GiB")

part = pd.read_csv("./transactions_train.csv", nrows=1000)
print(part)
# part2 = pd.read_csv("./transactions_train.csv", usecols=["t_dat", "sales_channel_id"])
# print(part2)

# sales = pd.Series()
sales = part["sales_channel_id"].value_counts() * 0

#for chunk in pd.read_csv("./transactions_train.csv", chunksize=3000000):
#    print(chunk["sales_channel_id"].value_counts())
#    sales = sales + chunk["sales_channel_id"].value_counts()

print(sales)

train_20200601 = train.loc[train['t_dat'] > '2020-06-01']
train_20200601.to_csv("train_20200601.csv", index=False)

