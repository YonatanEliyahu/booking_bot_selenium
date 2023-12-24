from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from booking.helper import sleep_decorator
import booking.constants as const
from booking.constants import currencies
from booking.constants import languages


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=const.DRIVER_PATH, detach=True):
        # Set the private attribute to the provided or default driver path
        self.__driver_path = driver_path
        # Add the driver path to the system's PATH environment variable
        os.environ['PATH'] += self.__driver_path

        # Configure Chrome options
        chrome_options = webdriver.ChromeOptions()
        # If detach is True, add the experimental option to detach the browser window
        if detach:
            chrome_options.add_experimental_option("detach", True)

        # Initialize the base class (webdriver.Chrome) with the configured options
        super(Booking, self).__init__(options=chrome_options)

        # Set implicit wait time to const.TIME_OUT
        self.implicitly_wait(const.TIME_OUT)
        # Maximize the browser window
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):  # exit function for context manager
        if exc_type is not None:  # if the program not closes properly -> close window
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)  # open booking.com

    def close_popup(self):
        try:
            # Wait for the popup button to be clickable within a timeout of 5 seconds
            popup_close_window = WebDriverWait(self, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[role='dialog'] button"))
            )
            # Click the popup button
            popup_close_window.click()

        except TimeoutException:
            # Handle the case where the element is not found within the timeout
            print("Popup button not found within the specified timeout.")

    @sleep_decorator()
    def change_lang(self, lang='US'):
        if lang not in languages:
            raise ValueError

        # Use a CSS_SELECTOR expression to find the language popup element
        lang_lst = self.find_element(By.CSS_SELECTOR, "[data-testid='header-language-picker-trigger']")
        lang_lst.click()

        # Use an XPath expression to find the button containing the English (US) text
        lang_button = self.find_element(By.XPATH,
                                        f"//button[@data-testid='selection-item']//span[contains(text(),'{languages[lang]}')]")
        lang_button.click()

    @sleep_decorator()
    def change_currency(self, curr="USD"):
        if curr not in currencies:
            raise ValueError

        # Use a CSS_SELECTOR expression to find the currency popup element
        curr_lst = self.find_element(By.CSS_SELECTOR, "[data-testid='header-currency-picker-trigger']")
        curr_lst.click()

        # Use an XPath expression to find the button containing the specified span with the currency text
        curr_button = self.find_element(By.XPATH, f"//button[.//div[text()='{curr}']]")
        curr_button.click()

    def choose_destination(self, destination: str):
        if destination is None:
            raise ValueError

        # Use a CSS_SELECTOR expression to find the destination input field
        destination_elm = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[id=':re:']"))
        )

        # Clear the input field in case there is already some text
        destination_elm.clear()

        # Send keys to the input field
        destination_elm.send_keys(destination)
