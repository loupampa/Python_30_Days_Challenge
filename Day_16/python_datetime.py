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

# Calculate the time difference between 1 january 1970 and now

back_date = datetime(year=1970, month=1, day=1)
time_difference = now - back_date
print(f"Time difference between 1 January 1970 and now: {time_difference}")

# Wwhat can you use the datetime module for?
## In production software engineering, you use it to prevent corruption, manage user sessions, keep distributed systems in sync.

# 1. Authentication & Security Tokens: JSON Web Tokens, password reset links, or Api keys, we use datetime and timedelta to enforce strict expiration windows.
# from datetime import datetime, timedelta, timezone

# issued_at = datetime.now(timezone.utc)
# expires_at = issued_at + timedelta(minutes=15)

###############################################################
# 2. Database Records & Audit Trails: Every production database table typically tracks created_at, and updated_at timestamps.
# When debugging a production incident, engineers query logs and database rows using datetime boundaries to isolate what changed right before a crash.
# Always save timezone-aware UTC objects(datetime.now(timezone.utc) to your databe, and only convert them to a user's local time zone at the very last
# second on the front-end. Mixing naive (timezone-unaware) and aware datetimes is a classic cause of TypeError crashes in Python.

###############################################################
# 3. API Serialization & Parsing: Microservices and front-end apps communicate using ISO 8601 strings.
# Incoming requests: you use datetime.fromisoformat() to turn a JSON string payload from a client into a Python object you can validate.
# Outgoing responses: You use .isoformat() to serialize Python objects back into clean JSON string.

###############################################################
# 4. Background Jobs, Caching & Rate Limiting
# Cache Invalidation: Checking if cached data is stale( if datetime.not(timezone.utc) - cache.timestamp > timedelta(hours=1) : fetch_fresh_data())
# Scheduled Tasks / Cron Logic: Determining if a recurring billing cycle is due, or filtering out weekend days using .weekday() so automated emails aren't sent on a Sunday
# Rate Limiting / Backoff : Calculating exponential backoff timers when retrying a failed thrid-party API call.

###############################################################
# 5. When processing CSVs, clickstreams, or financial transactions, you use strptime to normalize messy third-party date formats (like "11/13/26" vs "2026-11-13") into a uniform
# datetime format before loading them into a data warehouse, or tuncating timestamps to the start of the hour/day to group metrics
