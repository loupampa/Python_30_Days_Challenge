# Exercises - Day 16
from datetime import date, datetime

now = datetime.now()

# Get the current day, month, year, hour, minute, and timestamp from datetime module

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print(
    f"Current day: {day}, month: {month}, year: {year}, hour: {hour}, minute: {minute}, timestamp: {timestamp}"
)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

current_date_formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Current date formatted: {current_date_formatted}")

# Today is 13 November 2026. Change this time string to time

today_string = "13 November, 2026"
time_object = datetime.strptime(today_string, "%d %B, %Y")
print(f"Time object from string: {time_object}")

# Calculate the time difference between now and new year

today = date(year=2026, month=11, day=13)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print(f"Time left for new year: {time_left_for_newyear}")
