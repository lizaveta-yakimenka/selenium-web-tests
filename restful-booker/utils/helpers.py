from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, locator):
    """Wait for an element to be clickable and click it."""
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator)).click()

def fill_field(driver, locator, value):
    """Fill a field with a value."""
    field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
    field.send_keys(value)