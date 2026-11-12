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

# Formatting Date Output usin strftime

from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")  # This will give us the current time in HH:MM:SS format.
print("time:", t)  # This will print the current time in HH:MM:

time_one = now.strftime(
    "%m/%d/%Y, %H:%M:%S"
)  # This will give us the current date and time in MM/DD/YYYY, HH:MM:SS format.
print(
    "time_one:", time_one
)  # This will print the current date and time in MM/DD/YYYY, HH:MM:SS format.

time_two = now.strftime(
    "%d/%m/%Y, %H:%M:%S"
)  # This will give us the current date and time in DD/MM/YYYY, HH:MM:SS format.
print(
    "time_two:", time_two
)  # This will print the current date and time in DD/MM/YYYY, HH:MM:SS format.

# strftime symbols:
# %a - Weekday, short version
# %A - Weekday, full version
# %w - Weekday as a number 0-6, 0 is Sunday
# %d - Day of month 01-31
# %b - Month name, short version
# %B - Month name, full version
# %m - Month as a number 01-12
# %y - Year, short version, without century
# %Y - Year, full version
# %H - Hour 00-23
# %I - Hour 00-12
# %p - AM/PM
# %M - Minute 00-59
# %S - Second 00-59
# %f - Microsecond 000000-999999
# %z - UTC offset
# %Z - Timezone
# %j - Day number of year 001-366
# %U - Week number of year, Sunday as the first day of week, 00
# %W - Week number of year, Monday as the first day of week, 00-53
# %c - Local version of date and time
# %x - Local version of date
# %X - Local version of time
# %% - A % character
