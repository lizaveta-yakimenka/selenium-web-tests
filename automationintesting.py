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

driver = webdriver.Chrome(options=options)
driver.get('https://automationintesting.online/')

#Wait for the hidden elements to appear
wait = WebDriverWait(driver, 10)

def wait_and_click(by, value, description="element"):
  """Wait for an element to be clickable and click it."""
  print(f"Waiting for {description} to be clickable...")
  element = wait.until(EC.element_to_be_clickable((by, value)))
  element.click()
  print(f"Clicked {description}.")
  return element
  
def fill_field(by, value, text, description="field"):
  """Wait for a field to be visible and fill it with text."""
  print(f"Waiting for {description}...")
  field = wait.until(EC.visibility_of_element_located((by, value)))
  field.send_keys(text)
  print(f"Filled {description} with '{text}'.")
  return field
  
try:
  #Click on Book this room button
  wait_and_click(By.CLASS_NAME, "openBooking", "Book this room")
  
  #Test Next, Back, Today buttons on the calendar
  toolbar_label = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "rbc-toolbar-label"))
  )
  print(f"Initial Calendar Month and Year: {toolbar_label.text}")

  wait_and_click(By.XPATH, "//button[text()='Today']", "Today button")
  print(f"Calendar Month and Year: {toolbar_label.text}")

  wait_and_click(By.XPATH, "//button[text()='Next']", "Next button")
  print(f"Calendar Month and Year: {toolbar_label.text}")

  wait_and_click(By.XPATH, "//button[text()='Back']", "Back button")
  print(f"Calendar Month and Year: {toolbar_label.text}")
  
  #Wait until calendar element is visible
  calendar_dates = wait.until(
      EC.presence_of_all_elements_located((By.CLASS_NAME, "rbc-date-cell"))
  )
  
  start_date = calendar_dates[3].find_element(By.CLASS_NAME, "rbc-button-link")
  end_date = calendar_dates[4].find_element(By.CLASS_NAME, "rbc-button-link")
  
  #Perform action chain to press and drag to select dates
  actions = ActionChains(driver)
  actions.click_and_hold(start_date).move_to_element(end_date).release().perform()
  
  #This is to confirm that action
  print("Dates selected!")

  #Fill text data into the form
  fill_field(By.NAME, 'firstname', 'John', "Firstname")
  fill_field(By.NAME, 'lastname', 'Smith', "Lastname")
  fill_field(By.NAME, 'email', 'test123@email.com', "Email")
  fill_field(By.NAME, 'phone', '12345678900', "Phone")
  
  #Find and click the button that says Book
  wait_and_click(By.XPATH, "//button[text()='Book']", "Book")
  
except Exception as e:
  print(f"An unexpected error occurred: {e}")

finally:
  html = driver.page_source
  driver.quit()
