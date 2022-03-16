from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("chromedriver")
action = webdriver.ActionChains(driver)

driver.get("https://popcat.click/")

cat = driver.find_element_by_id("app")

time.sleep(2)

x = 0
while(x<12000):
    webdriver.ActionChains(driver).double_click(cat).perform()
    x=x+1
