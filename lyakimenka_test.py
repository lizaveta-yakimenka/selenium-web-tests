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
    
  #Test Card element
  cards = driver.find_elements(By.CLASS_NAME, "card")
  actions = ActionChains(driver)
  try:
    for card in cards:
      actions.move_to_element(card).perform()
      
      learn_more_button = WebDriverWait(card, 10).until(
       EC.visibility_of_element_located((By.CLASS_NAME, "button")))
      
      WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(learn_more_button))
      
      card_title = card.find_element(By.CLASS_NAME, 'card-title').text
      
      print(f"Attempting to click 'Learn More' on card '{card_title}'")
      learn_more_button.click()
      
      time.sleep(2)
      
      #Since "Learn More" is leading to a new tab, we need to handle switching tabs
      current_window_handle = driver.current_window_handle
      all_window_handles = driver.window_handles
      new_window_handle = [handle for handle in all_window_handles if handle != current_window_handle][0]
      driver.switch_to.window(new_window_handle)
      current_url = driver.current_url
      
      print(f"Card with title '{card_title}' leads to: {current_url}")
      assert current_url.startswith("http"), f"Invalid URL: {current_url}"
      
      driver.close()
      driver.switch_to.window(current_window_handle)
      
      time.sleep(2)
  except(NoSuchElementException) as e:
    try:
      card_title = card.find_element(By.CLASS_NAME, "card-title").text
    except NoSuchElementException:
      card_title = "Unknown"
    except TimeoutException as e:
      print(f"Timeout while waiting for 'Learn More' button on card '{card_title}': {e}")
    
except Exception as e:
  print(f"An unexpected error occurred: {e}")

finally:
  html = driver.page_source
  driver.quit()
