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
