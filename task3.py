
# -- Write a Python program to add 5 seconds to the current time. 

from datetime import datetime as dt, timedelta

current_datetime= dt.today()

# current + 5 seconds.
time_5sec = current_datetime + timedelta(seconds=5)


print('current time:', current_datetime )
print('after adding 5 seconds:', time_5sec)