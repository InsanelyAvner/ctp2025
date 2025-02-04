def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month]


def num_of_leap_years(start_year, end_year):
    count = 0
    for year in range(start_year, end_year):
        if is_leap_year(year):
            count += 1
    return count


def is_valid_date(date):
    if len(date) != 8:
        return False
    try:
        day = int(date[:2])
        month = int(date[2:4])
        year = int(date[4:])
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    max_days = days_in_month(month)
    if month == 2 and is_leap_year(year):
        max_days = 29
    return 1 <= day <= max_days


def num_of_days_from_1900(date):
    if not is_valid_date(date):
        return None
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
    days = (year - 1900) * 365 + num_of_leap_years(1900, year)
    for m in range(1, month):
        days += days_in_month(m)
    if month > 2 and is_leap_year(year):
        days += 1
    days += day - 1
    return days


def days_between_2_dates(date1, date2):
    days1 = num_of_days_from_1900(date1)
    days2 = num_of_days_from_1900(date2)
    if days1 is None or days2 is None:
        return None
    return abs(days2 - days1)


def add_n_days_after_1900(days):
    year = 1900
    month = 1
    day = 1
    while days >= 366 or (days >= 365 and not is_leap_year(year)):
        if is_leap_year(year):
            if days >= 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1
    while days > 0:
        max_days = days_in_month(month)
        if month == 2 and is_leap_year(year):
            max_days = 29
        if days >= max_days:
            days -= max_days
            month += 1
            if month > 12:
                month = 1
                year += 1
        else:
            day += days
            days = 0
    return f"{day:02d}{month:02d}{year}"


def add_n_days_from_a_date(date, days):
    if not is_valid_date(date):
        return None
    total_days = num_of_days_from_1900(date) + days
    return add_n_days_after_1900(total_days)


def weekday_of_date(date):
    weekdays = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    days = num_of_days_from_1900(date)
    if days is None:
        return None
    return weekdays[days % 7]


def date_calculator():
    done = False
    while not done:
        print("-----------------------------------------")
        print("Welcome to date calculator")
        print("  1. Calculate number of days between 2 dates.")
        print("  2. Add n days from a date.")
        print("  3. Find weekday of a date.")
        print("  4. Exit the programme.\n")
        print(
            "**Please note the format of date should follow the format of 'DDMMYYYY'\n"
        )
        try:
            option = int(input("Select a function: "))
            if option == 1:
                date1 = input("Enter first date (DDMMYYYY): ")
                date2 = input("Enter second date (DDMMYYYY): ")
                result = days_between_2_dates(date1, date2)
                if result is not None:
                    print(f"Number of days between dates: {result}")
                else:
                    print("Invalid date format")
            elif option == 2:
                date = input("Enter date (DDMMYYYY): ")
                days = int(input("Enter number of days to add: "))
                result = add_n_days_from_a_date(date, days)
                if result is not None:
                    print(f"Resulting date: {result}")
                else:
                    print("Invalid date format")
            elif option == 3:
                date = input("Enter date (DDMMYYYY): ")
                result = weekday_of_date(date)
                if result is not None:
                    print(f"Weekday: {result}")
                else:
                    print("Invalid date format")
            elif option == 4:
                done = True
                print("Thank you for using date calculator!")
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input")
        input("\nPress Enter to continue...")


date_calculator()
