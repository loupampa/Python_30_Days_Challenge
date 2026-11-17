# Regular Expressions - Day 18

## A regular expression or RegEx is a special text string that helps to find patterns in data.
## A RegEx can be used to check if some pattern exists in a different data type.

import re

print("Showing attributes and methods of the re module", dir(re))

# These are the most importants:
# re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
# re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall: Returns a list containing all matches
# re.split: Takes a string, splits it at the match points, returns a list
# re.sub: Replaces one or many matches within a string

### Match
txt = "I love to teach python, JavaScript, and Java"
match = re.match("I love to teach", txt, re.IGNORECASE)
print(match)  # It returns an object with span, and match

span = match.span()
print(
    span
)  # We can get the starting and ending position of the match as tuple using span

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)

match = re.match("I like to teach", txt, re.IGNORECASE)
print(match)  # There is no match with the previos txt

### Search
txt = """Python is the most beautiful language that a human being has ever I recommend python for a first programming language"""

match = re.search("first", txt, re.IGNORECASE)
print(match)

span = match.span()
print(
    span
)  # We can get the starting and ending position of the match as tuple using span

start, end = span
print(start, end)  # Lets find the start and stop position from the span # 100 105

substring = txt[start:end]
print(substring)  # first

### Searching for All Matches Using findall
txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

matches = re.findall("language", txt, re.IGNORECASE)  # It return a list
print(matches)  # ['language', 'language']

matches = re.findall("python", txt, re.IGNORECASE)
print(matches)  # ['Python', 'python']

# In case we dont use re.IGNORECASE
# matches = re.findall("Python|python", txt)
# print(matches)  # ['Python', 'python']

# matches = re.findall("[Pp]ython", txt)
# print(matches)  # ['Python', 'python']
