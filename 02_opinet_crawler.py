from selenium import webdriver
from selenium .webdriver.common.by import By
import time

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.opinet.co.kr/searRgSelect.do')

time.sleep(2)

# <a href="javascript:goSubPage(0, 0, 99);"><span>지역별</span></a>
driver.execute_script('goSubPage(0, 0, 99);')

time.sleep(2)

# //*[@id="SIDO_NM0"]
sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
sido_names = sido.find_elements(By.TAG_NAME, 'option')

sido_list = []
for sido_name in sido_names:
    sido_list.append(sido_name.get_attribute('value'))

sido_list = sido_list[1:]

for sido_item in sido_list:
    sido = driver.find_element(By.XPATH, '//*[@id="SIDO_NM0"]')
    sido.send_keys(sido_item)
    time.sleep(1)
    
    sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
    sigungu_names = sigungu.find_elements(By.TAG_NAME, 'option')
    
    sigungu_list = []
    for sigungu_name in sigungu_names:
        sigungu_list.append(sigungu_name.get_attribute('value'))

    sigungu_list = sigungu_list[1:]
    print(sigungu_list)

    for sigungu_item in sigungu_list:
        sigungu = driver.find_element(By.XPATH, '//*[@id="SIGUNGU_NM0"]')
        time.sleep(1)
        sigungu.send_keys(sigungu_item)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="searRgSelect"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="glopopd_excel"]').click()