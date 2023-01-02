import pandas as pd
from glob import glob
# from tqdm.notebook import tqdm
import os

temp = pd.read_excel("./opinet/지역_위치별(주유소).xls")
temp

stations_files = glob("./opinet/*.xls")

total = pd.DataFrame()
for file_name in stations_files:
    temp = pd.read_excel(file_name, header=2)
    total = pd.concat([total, temp])

total = total.sort_values(by="지역")
total = total.reset_index(drop=True)

total.to_excel("전국_주유소_가격.xlsx", index=False)
