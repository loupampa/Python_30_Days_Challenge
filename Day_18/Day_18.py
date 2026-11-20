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


txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

matches = re.sub("%", "", txt)
print(matches)

### Splitting Text Using RegEx Split
txt = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""
print(re.split("\n", txt))  # splitting using \n - end of line symbol

### Writing RegEx Patterns
regex_pattern = r"apple"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. "
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.IGNORECASE)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r"[Aa]pple"  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# []: A set of characters
# [a-c] means, a or b or c
# [a-z] means, any letter from a to z
# [A-Z] means, any character from A to Z
# [0-3] means, 0 or 1 or 2 or 3
# [0-9] means any number from 0 to 9
# [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# \d means: match where the string contains digits (numbers from 0-9)
# \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
# r'^substring' eg r'^love', a sentence that starts with a word love
# r'[^abc] means not a, not b, not c.
# $: ends with
# r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
# r'[a]*' means a optional or it can occur many times.
# +: one or more times
# r'[a]+' means at least once (or more)
# ?: zero or one time
# r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
# r'apple|banana' means either apple or a banana
# (): Capture and group

### Square Bracket
regex_pattern = r"[Aa]pple"  # this square bracket mean either A or a
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

regex_pattern = r"[Aa]pple|[Bb]anana"  # this square bracket means either A or a
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
