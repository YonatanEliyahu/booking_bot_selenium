from booking.booking import Booking


def main():
    with Booking() as bot:
        bot.land_first_page()
        bot.close_popup()
        bot.change_lang(lang='US')
        bot.change_currency(curr="USD")
        bot.choose_destination("Tel Aviv")
        bot.choose_dates(checkin="2023-12-26",
                         checkout="2023-12-30")
        bot.flexiable_dates(1)
        bot.select_num_adults(3)
        bot.select_num_children([1,2,3,4,5,10])
        bot.select_num_rooms(2)
        bot.submit_search()
        print("exiting ...")


if __name__ == "__main__":
    main()
