
# -- Write a Python program to print the next 5 days starting today.

import datetime as dt


# today's date
current_datetime = dt.datetime.today()

print('Today:', current_datetime)
print('Next 5 days:')


for i in range(5):
    next_days = current_datetime + dt.timedelta(i+1)
     # timedelta takes days by default if not mentioned.
    print(next_days)


# other possibility is: 

for i in range(1,6):
    next_days = current_datetime + dt.timedelta(i)
    print(next_days)



# just note from lesson calendar module
#import calendar

#print(calendar.weekday(2087, 12, 25))