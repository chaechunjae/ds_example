import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("train.csv")
print(titanic)
titanic.info()
titanic.describe()
print(titanic.loc[titanic["Age"]>= 30, "Name"])

print(pd.pivot_table(data=titanic, index="Sex", values="Survived", aggfunc=["mean", "sum", "count"]))
print(pd.pivot_table(data=titanic, index=["Pclass", "Sex"], values="Survived", aggfunc=["count", "sum", "mean"]))