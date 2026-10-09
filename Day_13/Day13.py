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

# Lambda Function
## It can take any number of arguments, but can only have one expression.
## Syntax : x = lambda param1, param2, param3:param1 + param2 + param3 ; print(x(arg1, arg2, arg3))

# EXAMPLES


# Named function
# Normal way
def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 3))

# Lambda function way
add_two_numbers = lambda a, b: a + b
print(add_two_nums(2, 3))

# Self invking lambda function
(lambda a, b: a + b)(2, 3)
square = lambda x: x**2
print(square(3))
cube = lambda x: x**3
print(cube(3))

# Multiple variables
multiple_variable = lambda a, b, c: a**2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))
