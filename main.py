from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import xml
PATH = "chromedriver.exe"

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
#
# driver = webdriver.Chrome()
#
# driver.get("https://ya.ru/")
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

driver.get('https://mail.ru')
