import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(str(driver))
time.sleep(5)