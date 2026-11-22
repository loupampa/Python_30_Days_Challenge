# Exercises - Day 18
import re
from collections import Counter

# What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
words = re.findall(r"\b\w+\b", paragraph.lower())
word_counts = Counter(words)
print(word_counts)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ["-12", "-4", "-3", "-1", "0", "4", "8"]

sorted_points = sorted(int(p) for p in points)
distance = sorted_points[-1] - sorted_points[0]
print(sorted_points)
print(distance)
