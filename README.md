# Selenium Automation for Booking.com

This project aims to provide hands-on experience with Selenium and Python for web automation, specifically targeting the
Booking.com main page.

## Prerequisites

Before running the automation scripts, ensure that you have the following installed:

-Python (>= 3.8)

-Selenium (>= 4.16.0)

-ChromeDriver (WebDriver for Chrome) (included in project)

You can install the required Python packages using the following command:

```commandline
pip install -r requirements.txt
```

## Project Structure

The project consists of the following main components:

booking.py: The main module containing the Booking class, which is a subclass of webdriver.Chrome with additional
automation functionalities.

constants.py: Constants used throughout the project, such as URLs, time-outs, and other configuration values.

helper.py: Helper functions, including decorators for sleep and date-related operations.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/YonatanEliyahu/booking_bot_selenium
    ```

2. Navigate to the project directory:

    ```bash
    cd booking_bot_selenium
    ```

3. Run the automation script by executing the `main()` function in the `main.py` file:

    ```bash
    python main.py
    ```

This script will launch a Chrome browser, navigate to Booking.com, perform various actions (such as closing pop-ups,
changing language and currency, selecting destination and dates, etc.), and finally submit the search.

#### Contributing

Contributions are welcome! Feel free to open issues or pull requests.

#### License

This project is licensed under the MIT License - see the LICENSE file for details.