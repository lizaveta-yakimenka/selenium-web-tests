from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')

options.add_argument("start-maximized"); 
options.add_argument("disable-infobars"); 
options.add_argument("--disable-extensions"); 
options.add_argument("--disable-gpu"); 
options.add_argument("--disable-dev-shm-usage"); 
try:
  driver = webdriver.Chrome(options=options)

  driver.get('https://lyakimenka.com')
  title = driver.title
  print(f'Page title is: {title}')
  #Test Header value Home
  try:
    home_link = driver.find_element(By.LINK_TEXT, 'Home')
    home_link.click()
    
    WebDriverWait(driver, 10).until(EC.url_contains('#home'))
    
    assert "Home" in driver.title or driver.current_url == 'https://lyakimenka.com/#home'
    
    print("Navigation link test passed successfully to Home!")
    
  except NoSuchElementException:
    print("Error: Home link not found")
  except TimeoutException:
    print("Error: Timeout waiting for Home link")
  except AssertionError:
    print("Error: Home link did not navigate to the expected URL")
    
  #Test Header value Projects
  try:
    home_link = driver.find_element(By.LINK_TEXT, 'Projects')
    home_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('#projects'))
    assert "Projects" in driver.title or driver.current_url == 'https://lyakimenka.com/#projects'

    print("Navigation link test passed successfully to Projects!")
  except NoSuchElementException:
    print("Error: Projects link not found")
  except TimeoutException:
    print("Error: Timeout waiting for Home link")
  except AssertionError:
    print("Error: Projects link did not navigate to the expected URL")
  #Test Header value Social
  try:
    home_link = driver.find_element(By.LINK_TEXT, 'Social')
    home_link.click()

    WebDriverWait(driver, 10).until(EC.url_contains('#social'))
    assert "Social" in driver.title or driver.current_url == 'https://lyakimenka.com/#social'

    print("Navigation link test passed successfully to Social!")
  except NoSuchElementException:
    print("Error: Social link not found")
  except TimeoutException:
    print("Error: Timeout waiting for Home link")
  except AssertionError:
    print("Error: Social link did not navigate to the expected URL")
    
except Exception as e:
  print(f"An unexpected error occurred: {e}")
