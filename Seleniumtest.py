from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import Chrome

driver = Chrome()
option = webdriver.ChromeOptions()
server = Service(executable_path='/Users/livion/Documents/GitHub/Sources/SeleniumForCAICT/chromedriver')
#初始化webbrowser实例
driver = webdriver.Chrome(service = server,options=option)
driver.get("https://www.baidu.com")





sleep(5)
driver.quit()