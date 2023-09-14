
# -- Write a Python program to print the dates of yesterday, today, tomorrow.

import datetime as dt

current_datetime= dt.date.today()


yesterday = current_datetime - dt.timedelta(days=1)  
tomorrow = current_datetime +  dt.timedelta(days=1)

print('yesterday:', yesterday) 
# no need of the strftime as it is dt.date not datetime.
print('Today:', current_datetime.strftime('%Y-%m-%d'))
print('Tomorrow:', tomorrow.strftime('%Y-%m-%d'))

# correction , can be done the following ways

days = dt.timedelta(days=1)
yesterday = current_datetime - days
tomorrow = current_datetime + days

