from booking.booking import Booking


def main():
    with Booking() as bot:
        bot.land_first_page()
        bot.close_popup()
        bot.change_lang(lang='US')
        bot.change_currency(curr="USD")
        bot.choose_destination("Tel Aviv")
        bot.choose_vacation_dates(checkin="2023-12-30",
                                 checkout="2024-01-05",
                                 flex=1)
        # bot.flexible_vacation("other-10-Sunday", [1, 5, 11])
        bot.select_num_adults(3)
        bot.select_num_children([1, 2, 3, 4, 5, 10])
        bot.select_num_rooms(2)
        bot.submit_search()
        print("exiting ...")


if __name__ == "__main__":
    main()
