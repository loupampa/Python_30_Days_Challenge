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

txt = "I love to teach python, JavaScript, and Java"
match = re.match("I love to teach", txt, re.IGNORECASE)
print(match)  # It returns an object with span, and match
