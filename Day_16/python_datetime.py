# Exercises - Day 16
from datetime import datetime

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
