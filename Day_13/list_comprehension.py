# Exercises - Day 13

# filtering only negatrive and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_only = [i for i in numbers if i < 0]
print(negatives_only)

# Flattening the list of lists of lists to one dimensional list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for group in list_of_lists for i in group]
print(flattened_list)
