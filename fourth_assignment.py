import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("http://www.amazon.com")

# title = driver.title
# print(title)
# driver.refresh()
# if title==driver.title:
#     print("equal")
driver.get("https://translate.google.com/")
time.sleep(10)
driver.find_element(By.TAG_NAME, "textarea").click();
time.sleep(5)
driver.find_element(By.CLASS_NAME,"er8xn").send_keys("anshul")
time.sleep(5)