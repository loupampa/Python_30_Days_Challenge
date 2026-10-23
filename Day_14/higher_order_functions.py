# Exercises - Day 14
from functools import reduce

# 1. Explaining the difference between map, filter, and reduce

## Map transforms each item into a collection and a function
## Filter selects items that pass a test into a collection and a predicate which returns true or false
## Recuce aggregate all items into one into a collection and an accumulator function

### Examples
## Map : Applied given function to every item in an iterable and returns the transfromed items
##  (truning a basket of whole oranges into a basket of orange juice glasses)
numbers = [1, 2, 3, 4]
# Double every number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

## Filter : Tests each element with a conditional function (predicate). Only items where the function
##  evaluates to True are kept, items that return False are discarded (Using a sieve or colander to keep big pasta shells and drain out water)
numbers = [1, 2, 3, 4, 5, 6]
# Keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

## Reduce : Takes elements pair by pair, applies a function to combine them, and repeats until only a single
## cumulative value remains
numbers = [1, 2, 3, 4]

# Multiply all numbers together: (((1*2) *3 *4)) =24
product = reduce(lambda acc, x: acc * x, numbers)
print(product)

# 2. Explaining the difference between higher order function, closure and decorator

## Higher-Order Function: Is any function that accepts a function as an argument, returns a function, or both, Funcftions treated as first-class data.
### Passing callbacks, sorting bykeys ( sorted(...,key=fn)), map(), filter()

## Closure is an inner function that retains access to variables from its outer enclosing scope, even after the outer function has finished executing, it captures and "closes over" lexical scope state
### Function factories lightweight data hiding without classes.

## Decorator is a design pattern (and syntax sugar @) that takes a function, extends or alters its behavior using a closure and returns the modified function, it wraps an existing callable without altering its source code.
### Logging, access control/auth. timing/profiling, caching.

# 3. Defining a call function before map, filter or reduce


## Transforming Elements by defining a function that takes one element and returns the transformed element:
def to_uppercase(text):  # Defining the callback function
    return text.upper()


words = ["python", "javascript", "golang"]

transformed = list(
    map(to_uppercase, words)
)  # Passing the function by name (without parentheses) to map
print(transformed)


## Conditional Selection defining a predicatet function that takes one element and returns True to keep it, or False to discard it
def is_even(n):  # Defining the predicate function
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(is_even, numbers))  # Passing the function to filter
print(evens)


## Aggregation by defining an accumulator function that takes two arguments; the rolling total/accumulator and the current item


def multiply_numbers(acc, curr):  # Defining the binary reduction function
    return acc * curr


values = [2, 3, 4, 5]

total_product = reduce(multiply_numbers, values)  # Passing the function to reduce
print(total_product)

# 4. Use for loop to print each country in the countries list.
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
for country in countries:
    print(country)

## If my list have nested Tuples
countries2 = [
    [("Finland", "Helsinki")],
    [("Sweden", "Stockholm")],
    [("Norway", "Oslo")],
]
for [(country, capital)] in countries2:
    print(country)

# 5. Use for to print each name in the names list.
