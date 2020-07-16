from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd


# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
# options.add_argument('--headless'); # ※ヘッドレスモードを使用する場合、コメントアウトを外す

DRIVER_PATH = 'パス'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

longin_URL = "URL"
driver.get(longin_URL)

# ID/PASSを入力
id = driver.find_element_by_id("email")
id.send_keys("ログインアドレス")
password = driver.find_element_by_id("password")
password.send_keys("ログインパス")

time.sleep(1)

# ログインボタンをクリック
login_button = driver.find_element_by_xpath('XPATH')
login_button.click()

time.sleep(1)

# カテゴリーごとのURLを格納
target_url = ["URL1",
              "URL2",
              "URL3",
              "URL4",
              "URL5",
              "URL6",
              "URL7",
              "URL8",
              "URL9"]

# カテゴリーごとの名前を格納
category = ["カテゴリ1",
            "カテゴリ2",
            "カテゴリ3",
            "カテゴリ4",
            "カテゴリ5",
            "カテゴリ6",
            "カテゴリ7",
            "カテゴリ8",
            "カテゴリ9"]

list = [["カテゴリ","講座名","リンク先URL"]]

for i in range(0,9):
    driver.get(target_url[i])
    time.sleep(10)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    elems = soup.find_all(class_="クラス名")
    for elem in elems:
        title = elem.get("title")
        link = elem.get("href")
        if title == None and link == None:
            pass
        else:
            target_link = "ドメインURL"+link
            list.append([category[i],title,target_link])

df = pd.DataFrame(list)
df.to_csv("ファイル名.csv", encoding='utf_8_sig')

