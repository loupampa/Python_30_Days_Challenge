# Exercises - Day 12
import random
import string


def random_user_id():
    user_id = ""
    for i in range(6):
        user_id += random.choice(string.ascii_letters + string.digits)
    return user_id


print(random_user_id())
