# Exercises - Day 18
import re
from collections import Counter

# What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
words = re.findall(r"\b\w+\b", paragraph.lower())
word_counts = Counter(words)
print(word_counts)
