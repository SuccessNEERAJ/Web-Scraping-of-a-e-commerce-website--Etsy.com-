from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service =service)

driver.get("https://www.etsy.com/in-en/")
print(driver.title)

link = driver.find_element(By.LINK_TEXT,"Birthday Gifts")
link.click()


time.sleep(5)
