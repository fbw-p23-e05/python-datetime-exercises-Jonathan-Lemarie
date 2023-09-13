
# - - Write a Python program to convert Year/Month/Day to Day of Year using datetime module.

from datetime import datetime as dt

current_date = dt.today()

print('Today: ', current_date)
print('Day of the year: ', current_date.strftime('%j'))
