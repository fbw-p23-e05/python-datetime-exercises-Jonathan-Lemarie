
# -- Write a Python program to print the dates of yesterday, today, tomorrow.

from datetime import datetime as dt, timedelta

current_datetime= dt.today()


yesterday = current_datetime - timedelta(days=1)  
tomorrow = current_datetime +  timedelta(days=1)

print('yesterday:', yesterday.strftime('%Y-%m-%d'))
print('Today:', current_datetime.strftime('%Y-%m-%d'))
print('Tomorrow:', tomorrow.strftime('%Y-%m-%d'))
