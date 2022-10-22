from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import argparse

def login_mail():
    driver.get('http://gmail.com')
    # exit()
    actions = ActionChains(driver)
    time.sleep(0.75)
    actions.send_keys(mail_address)
    actions.perform()
    actions = ActionChains(driver)
    time.sleep(1.75)
    actions.send_keys(password)
    actions.perform()

def login_meet(url, flag):
    if flag:
        driver.get(url)
    # time.sleep(1)
    driver.get(url)
    time.sleep(1.5)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    join = driver.find_element(By.XPATH,'/html/body/div/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span')
    join.click()

def open_new_tab(url, i):
    driver.execute_script("window.open();")
    driver.switch_to.window(driver.window_handles[i])
    login_meet(url, False)


mail_address = 'your_account@sssh.tp.edu.tw' + '\n'
password = 'your_password' + '\n'

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
  })

driver = webdriver.Chrome('./chromedriver', options=opt)
parser = argparse.ArgumentParser()
parser.add_argument('--url', help = 'The url of meeting')
parser.add_argument('-n', help = 'The amounts of tabs(it will open n+1 tabs)')
args = parser.parse_args()
login_mail()
login_meet(args.url, True)
for i in range(int(args.n)): open_new_tab(args.url, i+1)

