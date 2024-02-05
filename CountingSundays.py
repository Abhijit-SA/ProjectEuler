# You are given the following information, but you may prefer to do some research for yourself.
# - Jan 1900 was a Monday.
# - Thirty days has September, April, June and November.
# - All the rest have thirty-one, Saving February alone, has twenty-eight, rain or shine.
# - And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

import datetime


def count_sundays_on_first_of_month():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            # Create a datetime object for the first day of the month
            date = datetime.datetime(year, month, 1)
            # print(date.weekday())
            # Check if the day is a Sunday (weekday() returns 6 for Sunday)
            if date.weekday() == 6:
                count += 1

    return count


result = count_sundays_on_first_of_month()
print(
    "Number of Sundays on the first of the month during the twentieth century:", result
)
