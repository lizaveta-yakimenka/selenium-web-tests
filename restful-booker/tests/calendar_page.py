from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalendarPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.toolbar_label = (By.CLASS_NAME, "rbc-toolbar-label")
        self.today_button = (By.XPATH, "//button[text()='Today']")
        self.next_button = (By.XPATH, "//button[text()='Next']")
        self.back_button = (By.XPATH, "//button[text()='Back']")
        self.date_cells = (By.CLASS_NAME, "rbc-date-cell")
    
    def get_month_year(self):
        return self.wait.until(EC.visibility_of_element_located(self.toolbar_label)).text
    
    def click_today(self):
        self.wait.until(EC.element_to_be_clickable(self.today_button)).click()
    
    def click_next(self):
        self.wait.until(EC.element_to_be_clickable(self.next_button)).click()
    
    def click_back(self):
        self.wait.until(EC.element_to_be_clickable(self.back_button)).click()
    
    def select_dates(self, start_index, end_index):
        date_cells = self.wait.until(EC.presence_of_all_elements_located(self.date_cells))
        actions = ActionChains(self.driver)
        actions.click_and_hold(date_cells[start_index]).move_to_element(date_cells[end_index]).release().perform()
        print("Dates selected!")