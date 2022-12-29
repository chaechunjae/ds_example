import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

item_1 = pd.Series([1,3,5,6,8])
print(item_1)

df = pd.DataFrame(data=np.arange(1, 49).reshape(12, 4), columns=["X1", "X2", "X3", "X4"])
print(df)
print(df.index)
print(df.columns)
print(df.values)
print(df["X1"])
print(df["X1"] + 2)
print(df.head())
print(df.info())
print(df.describe())
print(df.sort_values(by="X2", ascending=False))
print(df[0:3])
print(df.loc[0])
# df.loc["row"]["col"]
print(df.loc[0][2], df.loc[0]["X3"])
print(df.loc[[0,3], ["X1", "X3"]])
print(df.loc[0:4, "X1":"X3"])

# boolean mask == filter
mask = df["X1"] > 10
print(mask)
print(df.loc[mask])

mask2 = df["X2"] >= 20
print(df.loc[mask2])

print(df.loc[df["X2"] >=20, "X4"])

mask3 = (10 <= df["X3"]) & (df["X3"]<= 30) 
print(df.loc[mask3, "X3"])

print(df.iloc[2:7, 0:3])