from re import S
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



option = webdriver.ChromeOptions()
server = Service(executable_path='/Users/livion/Documents/GitHub/Sources/SeleniumForQichacha/chromedriver')
#初始化webbrowser实例
driver = webdriver.Chrome(service = server,options=option)
# driver.get("https://www.sahitest.com/demo/linkTest.htm")
driver.get("https://www.baidu.com")
driver.find_element(By.LINK_TEXT, "新闻").click()
sleep(2)
current_window = driver.window_handles
while 1:
    for i in current_window:
        driver.switch_to.window(i)
        sleep(2)
    break




sleep(3)
driver.quit()