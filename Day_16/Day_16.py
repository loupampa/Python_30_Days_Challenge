# Python Datetime - Day 16

# Python has got datetime module to handle date and time.
import datetime

print(
    dir(
        datetime
    )  # With dir() function we can see all the attributes and methods of the datetime module.
)  # This will print all the attributes and methods of the datetime module.
# ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

# Getting datetime information

from datetime import datetime

now = datetime.now()  # This will give us the current date and time.
print("datetime: ", now)  # This will print the current date and time.

day = now.day  # This will give us the current day.
month = now.month  # This will give us the current month.
year = now.year  # This will give us the current year.
hour = now.hour  # This will give us the current hour.
minute = now.minute  # This will give us the current minute.
second = now.second  # This will give us the current second.
timestamp = now.timestamp()  # This will give us the current timestamp. Timestamp is the number of seconds elapsed from 1st of january 1970 UTC
print(
    day, month, year, hour, minute, second
)  # This will print the current day, month, year, hour, minute, second.
print("timestamp:", timestamp)  # This will print the current timestamp.
print(
    f"{day}/{month}/{year} {hour}:{minute}:{second}"
)  # This will print the current date and time in a formatted way.
