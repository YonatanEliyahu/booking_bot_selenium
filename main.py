from booking.booking import Booking


def main():
    # Create a Booking instance using a context manager for automatic cleanup
    with Booking() as bot:
        # Land on the booking.com homepage
        bot.land_first_page()

        # Close any popup that may appear
        bot.close_popup()

        # Change the language to English (US)
        bot.change_lang(lang='US')

        # Change the currency to US Dollar (USD)
        bot.change_currency(curr="USD")

        # Choose the destination as "Tel Aviv"
        bot.choose_destination("Tel Aviv")

        # Choose specific vacation dates with flexibility option
        bot.choose_vacation_dates(checkin="2023-12-30", checkout="2024-01-05", flex=1)

        # Alternatively, use flexible vacation method with specific parameters
        # bot.flexible_vacation("other-10-Sunday", [1, 5, 11])

        # Select the number of adults for the booking
        bot.select_num_adults(3)

        # Select the ages of children accompanying for the booking
        bot.select_num_children([1, 2, 3, 4, 5, 10])

        # Select the number of rooms for the booking
        bot.select_num_rooms(2)

        # Submit the search query
        bot.submit_search()

        # Print a message indicating the end of the script
        print("Exiting...")


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
