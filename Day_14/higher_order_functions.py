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
names = ["William", "Marga", "Lili", "Kami", "Ale"]
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
numbers = [27, 24, 7, 10, 4]
for number in numbers:
    print(number)

# 7. Use map to create a new list by changing each country to uppercase in the countries list.
countries = ["Peru", "USA", "Finland", "Spain", "Tokyo"]
uppercase_countries = list(map(str.upper, countries))
print(uppercase_countries)

# 8. Use map to create a new list by changing each number to its square in the numbers list.
numbers = [1, 2, 3, 4, 5, 6]
## squared_numbers = list(map(lambda x: x**2, numbers)) ##old method
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# 9. Use map to change each name to uppercase in the names list.
names = ["William", "Marga", "Lili", "Kami", "Ale"]
uppercase_names = list(map(str.upper, names))
print(uppercase_names)

# 10. Use filter to filter out countries containing 'land'.
countries3 = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
countries_filter = list(filter(lambda c: "land" not in c.lower(), countries3))
print(countries_filter)

# 11. Use filter to filter out countries having exactly six characters.
countries4 = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]
countries_length_filter = list(filter(lambda c: len(c) != 6, countries4))
print(countries_length_filter)

# 12. Use filter to filter out countries starting with an 'E'.
countries5 = ["Estonia", "Finland", "Sweden", "Egypt", "Norway", "Ecuador", "Denmark"]
countries_without_e = list(filter(lambda c: not c.lower().startswith("e"), countries5))
print(countries_without_e)


# 13. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Using map(), filter() and reduce()
class FluentList(list):
    def map(self, func):
        return FluentList(map(func, self))

    def filter(self, func):
        return FluentList(filter(func, self))

    def reduce(self, func, initial=None):
        if initial is not None:
            return reduce(func, self, initial)
        return reduce(func, self)


# Method-chaining usage:
numbers = FluentList([2, 5, 11, 8, 14, 3, 20])
total = (
    numbers.filter(lambda x: x > 10).map(lambda x: x**2).reduce(lambda acc, x: acc + x)
)
print(total)


# 14. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))


mixed_list = ["Finland", 25, "Sweden", 3.14, True, "Norway", None, "Denmark"]
print(get_string_lists(mixed_list))

# 15. Use reduce to sum all the numbers in the numbers list.
numbers_list = [2, 27, 10, 30, 22, 15, 14, 28, 17]
sum_numbers_list = reduce(lambda acc, curr: acc + curr, numbers)
print(sum_numbers_list)

# 16. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries6 = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]


def format_countries(acc, curr):
    # If on the last element, add ', and '
    if curr == countries[-1]:
        return f"{acc}, and {curr}"
    # Otherwise, join with a comma and space
    return f"{acc}, {curr}"


# Reduce to format the list, then append the ending phrase
sentence = reduce(format_countries, countries) + " are north European countries"

print(sentence)
# Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# 17. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


def categorize_countries(pattern, countries):
    pattern_lower = pattern.lower()
    return list(filter(lambda country: pattern_lower in country.lower(), countries))


countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Finland",
    "Iceland",
    "Ireland",
    "Marshall Islands",
    "Kazakhstan",
    "Nigeria",
    "Pakistan",
    "Poland",
    "Solomon Islands",
    "Switzerland",
    "Uzbekistan",
]
print(categorize_countries("land", countries))

print(categorize_countries("stan", countries))

print(categorize_countries("ia", countries))

print(categorize_countries("island", countries))


# 18. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_starting_letter(countries):
    letter_counts = {}
    for country in countries:
        if country:
            first_letter = country[0].upper()
            letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1
    return letter_counts


countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Brazil",
    "Canada",
    "China",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
]
print(count_countries_by_starting_letter(countries))
