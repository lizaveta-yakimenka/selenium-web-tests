from selenium import webdriver
from src.tests.calendar_page import CalendarPage
from src.tests.booking_page import BookingPage

def test_booking_flow():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://automationintesting.online/')
    
    try:
        # Initialize page objects
        calendar = CalendarPage(driver)
        booking = BookingPage(driver)
        
        # Interact with the calendar
        print(f"Initial Month/Year: {calendar.get_month_year()}")
        calendar.click_today()
        print(f"After Today: {calendar.get_month_year()}")
        calendar.click_next()
        print(f"After Next: {calendar.get_month_year()}")
        calendar.click_back()
        print(f"After Back: {calendar.get_month_year()}")
        calendar.select_dates(3, 4)
        
        # Fill the booking form
        booking.fill_booking_form("John", "Smith", "test123@email.com", "1234567890")
        booking.submit_booking()
        print("Booking submitted successfully!")
    
    finally:
        driver.quit()