
# -- Write a Python program to print the next 5 days starting today.

from datetime import datetime as dt, timedelta


# today's date
current_datetime = dt.datetime.now()

print('Today:', current_datetime)
print('Next 5 days:')


for i in range(1, 6):
    #next_days = current_datetime + timedelta(days=1)
    print(current_datetime + datetime.timedelta(days=1))


# just note from lesson calendar module
#import calendar

#print(calendar.weekday(2087, 12, 25))