import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv("train.csv")
print(titanic)
titanic.info()
titanic.describe()