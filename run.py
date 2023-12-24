from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.close_popup()
    print(bot.get_all_currencries())
