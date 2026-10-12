# Exercises - Day 13

# 1. filtering only negatrive and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_only = [i for i in numbers if i < 0]
print(negatives_only)
print(50 * "#")

# 2 .Flattening the list of lists of lists to one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for group in list_of_lists for i in group]
print(flattened_list)
print(50 * "#")

# 3. Creating a list of tuples
tuples = [
    (
        i,
        1,
        1 * i,
        (1 * i) * (1 * i),
        (1 * i) * (1 * i) * (1 * i),
        (1 * i) * (1 * i) * (1 * i) * (1 * i),
        (1 * i) * (1 * i) * (1 * i) * (1 * i) * (1 * i),
    )
    for i in range(11)
]
print(tuples)
print(50 * "#")

# 4. Flattening a new list
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattened_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for [(country, city)] in countries
]
print(flattened_countries)
print(50 * "#")

# 5.Changing the list to a list of dictionaries
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
keys = ["country", "city"]

dictionary_list = [
    {keys[0]: country.upper(), keys[1]: city.upper()} for [(country, city)] in countries
]

print(dictionary_list)
print(50 * "#")

# 6. Changing the list to a list of concatenated strings
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
concatenated_names = [f"{first} {last}" for [(first, last)] in names]
print(concatenated_names)
print(50 * "#")

# 7. Writing a lambda function
# Slope: m = (y2 - y1) / (x2 - x1)
get_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Y-intercept: b = y1 - m * x1
get_intercept = lambda x1, y1, x2, y2: y1 - get_slope(x1, y1, x2, y2) * x1

# Example usage:
print(get_slope(2, 5, 4, 9))  # Output: 2.0
print(get_intercept(2, 5, 4, 9))  # Output: 1.0
print(50 * "#")
