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

## Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

## Filtering numbers, positive even numbers from the next list
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

## Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for row in list_of_lists for i in row]
print(flattened_list)
