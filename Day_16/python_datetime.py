# Exercises - Day 16
from datetime import datetime

# Get the current day, month, year, hour, minute, and timestamp from datetime module
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp

print(
    f"Current day: {day}, month: {month}, year: {year}, hour: {hour}, minute: {minute}, timestamp: {timestamp}"
)
