# Exception Handling - Day 17
# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong

# Packing and Unpacking Arguments
## We use two operators: * for tupples and ** for dictionaries
# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             # 6
# print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# Spreading in Python
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Enumerate
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# for index, i in enumerate(countries):
#     if i == 'Finland':
#         print(f'The country {i} has been found at index {index}')

# Zip
# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)
