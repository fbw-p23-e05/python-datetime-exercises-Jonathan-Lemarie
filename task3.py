
# -- Write a Python program to add 5 seconds to the current time. 

import datetime as dt
current_datetime= dt.datetime.today()

# current + 5 seconds.
time_5sec = current_datetime + dt.timedelta(seconds=5)


print('current time:', current_datetime )
print('after adding 5 seconds:', time_5sec)

# or correction :

seconds = dt.timedelta(seconds=5)
new_time = current_datetime + seconds

print(new_time)