# Exercises - Day 12
import random
import string


def random_user_id():
    user_id = ""
    for i in range(6):
        user_id += random.choice(string.ascii_letters + string.digits)
    return user_id


print(random_user_id())
print("#" * 50)


def user_id_gen_by_user():
    characters_count = int(input("Enter the number of characters: "))
    id_count = int(input("Enter number of IDs: "))
    characters = string.ascii_letters + string.digits

    generated_ids = [
        "".join(random.choice(characters) for _ in range(characters_count))
        for _ in range(id_count)
    ]
    return "\n".join(generated_ids)


print(user_id_gen_by_user())
print("#" * 50)
