# Exercises - Day 14

# Explaining the difference between map, filter, and reduce
## Map transforms each item into a collection and a function
## Filter selects items that pass a test into a collection and a predicate which returns true or false
## Recuce aggregate all items into one into a collection and an accumulator function

### Examples
## Map
numbers = [1, 2, 3, 4]
# Double every number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

## Filter
