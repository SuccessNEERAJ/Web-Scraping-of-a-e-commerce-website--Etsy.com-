from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open Etsy website
driver.get("https://www.etsy.com/in-en/")

# Click on the sign-in button
signin = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/header/div[4]/nav/ul/li[1]/button")))
signin.click()
time.sleep(2)

# Fill in the email field
email_field = driver.find_element(By.ID, "join_neu_email_field")
email_field.send_keys("cuneerajjaiswal@gmail.com")

# Fill in the password field
password_field = driver.find_element(By.ID, "join_neu_password_field")
password_field.send_keys("Etsy12012003")

# Click on the sign-in button
sign_in_button = driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[3]/div/div/div/div/div/div[2]/form/div[1]/div/div[7]/div/button")
sign_in_button.click()
time.sleep(20)

# Search for a product
search = driver.find_element(By.NAME, 'search_query')
search.send_keys("perfume set")
search.send_keys(Keys.RETURN)
time.sleep(5)

# Click on the first product
first_product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ui-toolkit .v2-listing-card:first-child")))
first_product.click()
time.sleep(5)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Click on the "Add to Basket" button
add_to_basket_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/div[1]/div[2]/div/div/div[1]/div[2]/div/div[6]/div[1]/div[2]/div[3]/div/form/div/button")))
add_to_basket_button.click()
time.sleep(5)

# Click on the checkout button
checkout_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "submit-button-text")))
checkout_button.click()
time.sleep(5)

# Navigate back to the previous page
driver.back()
time.sleep(5)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Scroll up the page
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)

# Click on the "Categories" button
categories_button = driver.find_element(By.CSS_SELECTOR, "button.wt-menu__trigger")
categories_button.click()

# Click on the "Home & Living" option
home_living_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home & Living")))
home_living_option.click()
time.sleep(5)

# Click on the "Home Favourites" option
home_fav = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home Favourites")))
home_fav.click()
time.sleep(5)

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Scroll up the page
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(5)
