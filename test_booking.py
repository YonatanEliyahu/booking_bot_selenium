import time

import pytest
from booking.booking import Booking
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def booking_bot():
    """
    The fixture yields the Booking instance for use in the tests.
    Every test will start by opening the main page of Booking,
    and trying to close the popup message.
    At the end of every test, the browser will close.
    """
    with Booking(detach=False) as bot:
        bot.land_first_page()
        bot.close_popup()
        yield bot


def test_land_first_page(booking_bot: Booking):
    """
    Test the landing page by checking if 'Booking.com' is in the page title.
    """
    assert 'Booking.com' in booking_bot.title


def test_submit_search_without_values(booking_bot: Booking):
    """
    Test submitting a search without providing destination values.
    """
    # Click the submit search button
    booking_bot.submit_search()

    try:
        # Attempt to find and retrieve the alert text
        alert_text = booking_bot.find_element(By.CSS_SELECTOR, "[data-testid='searchbox-alert'] div").text
        # Check if the alert text is as expected
        assert alert_text == "Enter a destination to start searching."
    except:
        # Handle the case where the element is not found
        assert False  # Assert failure to indicate test failure
