import chromedriver_binary
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

keys = "東京駅 スペシャルティコーヒー豆"
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.co.jp/maps/')

time.sleep(5)

ids = driver.find_element_by_id("searchboxinput")
ids.send_keys(keys)

time.sleep(1)

search_button = driver.find_element_by_xpath(
    "//*[@id='searchbox-searchbutton']")
search_button.click()

time.sleep(3)

search_results = driver.find_elements_by_class_name("section-result-title")

for i in range(len(search_results)):
    time.sleep(5)
    search_result =\
        driver.find_elements_by_class_name("section-result-title")[i]
    search_result.click()
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    print(soup.title)
    time.sleep(5)

    back_button = driver.find_element_by_xpath(
        '//*[@id="pane"]/div/div[1]/div/div/button')
    back_button.click()
    time.sleep(5)

    if i == 4:
        break

driver.close()
