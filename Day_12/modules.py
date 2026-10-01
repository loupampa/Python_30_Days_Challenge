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
    

print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr