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


def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"


print(rgb_color_gen())
print("#" * 50)


def list_of_hexa_colors(count=1):
    hex_digits = "0123456789abcdef"
    colors = []
    for _ in range(count):
        hex_code = "#" + "".join(random.choices(hex_digits, k=6))
        colors.append(hex_code)
    return colors


print(list_of_hexa_colors(5))
print(list_of_hexa_colors(1))
print("#" * 50)


def list_of_rgb_colors(count=1):
    colors = []
    for _ in range(count):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r}, {g}, {b})")
    return colors


print(list_of_rgb_colors(5))
print(list_of_rgb_colors(1))
print("#" * 50)
