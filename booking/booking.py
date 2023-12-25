import time
import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from booking.helper import sleep_decorator
from booking.helper import check_date_format
from booking.helper import is_valid_date
from booking.helper import date_diff
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
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[action*=searchresults] input[id=':re:']"))
        )

        # Clear the input field in case there is already some text
        destination_elm.clear()

        # Send keys to the input field
        destination_elm.send_keys(destination)
        time.sleep(1)  # load auto completion

        # Use a CSS_SELECTOR expression to find the destination input field
        autocomplete_elm = WebDriverWait(self, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='autocomplete-result']"))
        )
        autocomplete_elm.click()

    def choose_dates(self, checkin: str, checkout: str):
        """
        The function get two string based dates,
        at the first part, the function validate the dates in several checks,
        and then it picks the date elements in the webdriver
        Note: dates are limited for 12 mounts from today to save time,
            to change that, please change the booking.constants.MAXMOUNTS
        """
        #  validate dates format
        if check_date_format(checkin) is False or check_date_format(checkout) is False:
            raise ValueError

        #  validate dates as real dates
        if is_valid_date(checkin) is False or is_valid_date(checkout) is False:
            raise ValueError

        #  checks that the checkin is today or after that, and that the checkout is after the checkin
        if date_diff(None, checkin) < 0 or date_diff(checkin, checkout) < 0:
            raise ValueError

        max_tries = 0
        checked_in = False  # will help us to pick the checkin date at the beginning and the checkout after that
        next_date_btn = self.find_element(By.CSS_SELECTOR, "[id*='searchboxdatepicker'] button")  # next month btn
        while max_tries < const.MAXMOUNTS:  # picked dates are in the following MAXMOUNTS (12) months:
            try:
                date = WebDriverWait(self, 0.5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                f"[data-date='{checkin if not checked_in else checkout}']"))
                )  # selects checkin date and then checkout date
                date.click()
                if checked_in:
                    break
                else:
                    checked_in = True
            except Exception:
                next_date_btn.click()  # if date not found in the presented calendar, change months
                max_tries += 1
                if max_tries == const.MAXMOUNTS:
                    raise ValueError

    def flexiable_dates(self, flex: int = 0):
        if flex not in const.flexible_dates_options.keys():
            return
        try:
            self.find_element(By.XPATH,
                              f"//div[@data-testid='flexible-dates-container']//li[{const.flexible_dates_options[flex]}]") \
                .click()
        except selenium.common.exceptions.NoSuchElementException:
            # if button not found, that indicates that the date picking nav is closed and we need to reopen it.
            self.find_element(By.XPATH, "//div[@data-testid='searchbox-dates-container']/button").click()
            self.flexiable_dates(flex)

    def select_adults(self, num_of_adults: int = const.ADULTS_DEFAULT):
        if not (const.MIN_NUM_ADULTS <= num_of_adults <= const.MAX_NUM_ADULTS):
            raise ValueError
        selection_menu_btn = self.find_element(By.CSS_SELECTOR, "[data-testid='occupancy-config']")
        selection_menu_btn.click()  # open selection menu
        # get necessary elements
        minus_adult_btn = self.find_element(By.XPATH,
                                            f"//span[text()='{const.ADULTS_DEFAULT}']/parent::*/button[1]")
        plus_adult_btn = self.find_element(By.XPATH,
                                           f"//span[text()='{const.ADULTS_DEFAULT}']/parent::*/button[2]")
        curr_num_adults = int(self.find_element(By.XPATH,
                                                f"//span[text()='{const.ADULTS_DEFAULT}']/parent::*/span").text)

        if num_of_adults < curr_num_adults:
            for i in range(curr_num_adults, num_of_adults, -1):
                minus_adult_btn.click()
        elif num_of_adults > curr_num_adults:
            for i in range(curr_num_adults, num_of_adults):
                plus_adult_btn.click()
        selection_menu_btn.click()  # close selection menu

    def submit_search(self):
        sub_btn = self.find_element(By.CSS_SELECTOR, "form[action*=searchresults] button[type='submit']")
        sub_btn.click()
