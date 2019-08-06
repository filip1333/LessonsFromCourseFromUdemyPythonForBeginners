from datetime import date


def counter():
    # counts how many days have been left until the end of the year
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    left_days = date_today - date_end_year
    print(left_days)


counter()
