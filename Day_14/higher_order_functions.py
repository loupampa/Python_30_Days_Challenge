# Exercises - Day 14
from functools import reduce

# Explaining the difference between map, filter, and reduce
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

# Explaining the difference between higher order function, closure and decorator
## Higher-Order Function: Is any function that accepts a function as an argument, returns a function, or both, Funcftions treated as first-class data.
### Passing callbacks, sorting bykeys ( sorted(...,key=fn)), map(), filter()
