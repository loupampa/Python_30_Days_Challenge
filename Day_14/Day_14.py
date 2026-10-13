# Higher Order Functions - Day 14
# Function as a Parameter

## Normal function
def sum_number(nums):
    return sum(nums)


## Function as a Parameter
def higher_order_function(f, lst):
    sum = f(lst)
    return sum


result = higher_order_function(sum_number, [1, 2, 3, 4, 5])
print(result)


## Function as a Return Value
# Normal function
def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


# Higher Order Function
def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    else:
        return absolute


result = higher_order_function("square")
print(result(3))
result = higher_order_function("cube")
print(result(3))
result = higher_order_function("absolute")
print(result(-3))


## Python Closures
# Python allows a nested function to access the outer scope of the enclosing function.
# This is known as a Closure. Let us have a look at how closures work in Python
# Python closures are used to avoid the use of global values and provides some form of data hiding. A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
def add_ten():
    ten = 10

    def add(num):
        return num + ten

    return add


closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))


## Python Decorators
# Decorators is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
# Normal function
def greeting():
    return "Hello, welcome to Python"


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())


# Higher order function that takes a function as a parameter
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello, welcome to Python"


print(greeting())


## Applying Multiple Decorators to a Single function
# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# Second Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


# Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator
def greeting():
    return "Hello, welcome to Python"


print(greeting())


## Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print(f"I live in {para3}")

    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to code.")


print_full_name("Lourdes", "Pampa", "Peru")

## Built-in Higher Order Functions
# Python Map Function
numbers = [1, 2, 3, 4, 5]


def square_two(x):
    return x**2


numbers_squared = map(square_two, numbers)
print(list(numbers_squared))

# Lets apply it with a lambda function
numbers_squared = map(lambda x: x**2, numbers)
print(list(numbers_squared))

numbers_str = ["1", "2", "3", "4", "5"]
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ["Lourdes", "Pampa", "William", "Suarez"]


def change_to_upper(name):
    return name.upper()


names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

# Lets apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

## Python Filter Function
