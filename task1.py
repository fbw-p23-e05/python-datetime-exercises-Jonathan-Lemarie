
# -- Write a Python script to display the various Date Time formats.

#Current date and time
# Current year
# Month of year
# Week number of the year
# Weekday of the week
# Day of year
# Day of the month
# Day of week

import datetime as dt

current_datetime= dt.datetime.today()


print(current_datetime)



print('Current date and time:', current_datetime)
print('Current year:', current_datetime.strftime('%Y'))
print('Month of year:', current_datetime.strftime('%B'))
print('Week number of the year:',current_datetime.strftime('%U'))
print('Weekday of the week:', current_datetime.strftime('%w')) 
print('Day of year:', current_datetime.strftime('%j'))
print('Day of the month :', current_datetime.strftime('%d'))
print('Day of week:', current_datetime.strftime('%A'))