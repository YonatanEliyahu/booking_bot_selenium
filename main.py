from booking.booking import Booking


def main():
    with Booking() as bot:
        bot.land_first_page()
        bot.close_popup()
        bot.change_lang(lang='US')
        bot.change_currency(curr="USD")
        bot.choose_destination("Tel Aviv")
        bot.choose_dates(checkin="2024-01-25",
                         checkout="2024-02-28")
        bot.submit_search()
        print("exiting ...")


if __name__ == "__main__":
    main()
