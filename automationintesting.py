from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("start-maximized")
options.add_argument("disable-infobars") 
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu") 
options.add_argument("--disable-dev-shm-usage") 

try:
  driver = webdriver.Chrome(options=options)

  driver.get('https://automationintesting.online/')
  title = driver.title
  print(f'Page title is: {title}')
  driver.find_element(By.CLASS_NAME, 'btn').click()
  print('Clicked!')
  WebDriverWait(driver, 3).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'col-sm-4'))
  )
  print('located!')
  driver.find_element(By.CSS_SELECTOR, "input.form-control.room-firstname[placeholder='Firstname']").send_keys("John")
  print('Sent!')
except Exception as e:
  print(f"An unexpected error occurred: {e}")

finally:
  html = driver.page_source
  driver.quit()
