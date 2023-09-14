

# - - Write a Python program to select all the Sundays in a specified year.

import datetime as dt


year = int(input('input a year: '))

date = dt.date(year, 1, 1)

print('output:')

while year == date.year:
    if date.weekday() == 6:
        print(date)
    date += dt.timedelta(1)


# or possible with for loop

