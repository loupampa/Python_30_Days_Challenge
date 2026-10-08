# List Comprehension - Day 13

# We are going to create list from a sequence.
## Syntax: [expression for item in iterable if condition == True]

# EXAMPLES
## If you wanna create a list of characters. we can use methods

# Normal way
language = "Python"
lst = list(language)
print(type(lst))
print(lst)

# List comprehension way
lst = [i for i in language]
print(type(lst))
print(lst)
