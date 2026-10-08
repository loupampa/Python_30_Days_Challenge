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


## If you want to generate a list of numbers

# list comprehension way
numbers = [i for i in range(11)]
print(numbers)

# If you want to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)

# If you want to make a list of tuples
tuples = [(i, i * i) for i in range(11)]
print(tuples)

## List comprehension with if expression

## Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)
