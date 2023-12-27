DRIVER_PATH = "./chromedriver.exe"
BASE_URL = "https://www.booking.com/"
TIME_OUT = 7.5
MAX_MONTHS = 12
ADULTS_DEFAULT = 2
MIN_NUM_ADULTS = 1
MAX_NUM_ADULTS = 30
MIN_NUM_ROOMS = 1
MAX_NUM_ROOMS = 30
MAX_NUM_CHILDREN = 10
CHILDREN_DEFAULT = 0

CHILD_MIN_AGE = 0
CHILD_MAX_AGE = 18

currencies = {'SGD', 'BHD', 'OMR', 'HUF', 'PLN', 'AED', 'SAR', 'THB', 'CLP', 'CAD', 'GBP', 'SEK', 'BGN', 'MXN',
              'RUB', 'NOK', 'RON', 'GEL', 'KZT', 'TWD', 'DKK', 'MYR', 'KWD', 'JPY', 'IDR', 'TRY', 'ILS', 'COP',
              'ZAR', 'EGP', 'USD', 'BRL', 'NZD', 'QAR', 'KRW', 'XOF', 'JOD', 'INR', 'FJD', 'AUD', 'HKD', 'EUR',
              'CNY', 'CZK', 'ISK', 'MDL', 'NAD', 'CHF', '€$£', 'AZN', 'UAH', 'ARS'}

languages = {'IL': 'עברית',
             'US': 'English (US)',
             'UK': 'English (UK)',
             'GR': 'Deutsch',
             'FR': 'Français',
             'ES': 'Español',
             'IT': 'Italiano'
             }

flexible_dates_options = {0: 1, 1: 2, 2: 3, 3: 4, 7: 5}  # map flexibility to its element position in page

flexible_duration_options = {'weekend', 'week', 'month', 'other'}

MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct',
          11: 'Nov', 12: 'Dec'}
