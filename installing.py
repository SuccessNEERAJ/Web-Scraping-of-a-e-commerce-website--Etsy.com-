from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service =service)

driver.get("https://www.amazon.in/")
time.sleep(20)