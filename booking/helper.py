import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from dateutil import parser
from dateutil.parser import ParserError


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


def check_date_format(date: str) -> bool:
    """
    checks if the date is in YYYY-MM-DD format
    """
    temp_date = date.split('-')
    if len(temp_date) != 3:
        return False
    if len(temp_date[0]) != 4 or len(temp_date[1]) != 2 or len(temp_date[2]) != 2:
        return False
    return True


def is_valid_date(date: str):
    """
        checks if the dte formated string is a valid date (not 2024-02-30) for example
    """
    try:
        parsed_date = parser.parse(date)
        return True
    except ParserError:
        return False

def date_diff(from_date:str,to_date:str):
    """
    :param from_date: default - now()
    :return:The function will return the difference between the dates in days
    """
    if from_date is None:
        nfrom_date = datetime.now()
    else:
        nfrom_date = datetime.strptime(from_date, "%Y-%m-%d")
    nto_date= datetime.strptime(to_date, "%Y-%m-%d")
    return (nto_date-nfrom_date).days

