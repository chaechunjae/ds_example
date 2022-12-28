import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


page_no = 1
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page=1"

result = requests.get(page_url).text

# print(result)

result_parse = bs(result)
# print(result_parse)
# print(result_parse.prettify)

f_result = result_parse.find_all('td', class_='number_1')
# print(f_result)

result_date = result_parse.find_all('td', class_='date')
print(result_date)
for date in result_date:
    print(date.text)

last_url = result_parse.find_all('td', class_='pgRR')[0].find_all('a')[0]['href']
print(last_url)
last_page = last_url.split('&page=')[-1]
print(last_page)

date_list = []
price_list = []

for i in range(1, int(last_page)+1):
    dates = result_parse.find_all("td", class_="date")

    for date in dates:
        date_list.append(date)

    prices = result_parse.find_all("td", class_="number_1")

    for price in prices[::4]:
        price_list.append(price)

df = pd.DataFrame({"date": date_list, "price": price_list})
print(df)

df.to_excel("kpi200.xlsx", index=False)