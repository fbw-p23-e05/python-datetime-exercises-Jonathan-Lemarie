
# -- Write a Python program to find the date of the first Monday of a given week.

import datetime as dt

#import calendar



week = input("Enter the Week of the Year :")
year = input("Enter the Year :")
monday = '1'
date = dt.datetime.strptime(year + week + monday, "%Y%W%w")
print('The first Monday of this week was:', date.date())


# also trying to figure out how to make it happen using the calendar module.


# - - correction :

week = 37
first_day = dt.date(2023, 1, 1)

days = dt.timedelta((week - 1) * 7)

new_date = first_day + days

print(new_date.weekday())

first_monday = new_date + dt.timedelta(1)


print(first_monday)
