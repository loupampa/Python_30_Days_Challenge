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


def uppercase_decorator(func):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


g = uppercase_decorator(greeting)
print(g())
