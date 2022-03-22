import re
import sys
from typing import List
from bs4 import BeautifulSoup
import requests
import csv
from googletrans import Translator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



BASE_URL = "https://www3.nhk.or.jp/news/easy/"

def translate(source: str)->str:
    translator = Translator()
    return translator.translate(sentence, src='ja', dest='en').text



options = Options()
options.binary_location = "X:\Program files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(r'X:\Desktop\PracaInzynierska\kanji-learn\chromedriver.exe')
# driver = webdriver.Chrome(chrome_options=options)
driver.get(BASE_URL)
# page = requests.get(BASE_URL)
# soup = BeautifulSoup(page.content, "html.parser")
soup = BeautifulSoup(driver.page_source, "html.parser")

sentence = "ここに　えいごおはなせるひとはいますか。"

for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

# print(soup)

driver.quit()