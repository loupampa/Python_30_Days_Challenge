# Exercises - Day 13

# filtering only negatrive and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_only = [i for i in numbers if i < 0]
print(negatives_only)
