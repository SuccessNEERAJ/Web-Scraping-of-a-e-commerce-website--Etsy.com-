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
search = driver.find_element(By.NAME, 'search_query')
search.send_keys("birthday")
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"main")))
    print(main.text)
except:
    driver.quit()
    
time.sleep(5)
