from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname_field = (By.NAME, "firstname")
        self.lastname_field = (By.NAME, "lastname")
        self.email_field = (By.NAME, "email")
        self.phone_field = (By.NAME, "phone")
        self.book_button = (By.XPATH, "//button[text()='Book']")
    
    def fill_booking_form(self, firstname, lastname, email, phone):
        self.driver.find_element(*self.firstname_field).send_keys(firstname)
        self.driver.find_element(*self.lastname_field).send_keys(lastname)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.phone_field).send_keys(phone)
    
    def submit_booking(self):
        self.driver.find_element(*self.book_button).click()