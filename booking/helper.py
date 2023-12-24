import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def sleep_decorator(sleepTime=1):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            time.sleep(sleepTime)
            result = func(self, *args, **kwargs)
            return result

        return wrapper

    return decorator


def get_all_currencries(driver: webdriver.Chrome):
    """
    :param driver: webdriver.Chrome obj
    :return: list of currencies from Booking.com site
    """
    # Use a CSS_SELECTOR expression to find the currency popup element
    curr_elem = driver.find_element(By.CSS_SELECTOR, "[data-testid='header-currency-picker-trigger']")
    curr_elem.click()
    # Use an XPath expression to find the button containing the specified span with the currency text
    curr_elem_lst = driver.find_elements(By.CSS_SELECTOR, "button[data-testid='selection-item'] span>div")
    currencies = set()
    for elem in curr_elem_lst:
        currencies.add(elem.text)

    return currencies
