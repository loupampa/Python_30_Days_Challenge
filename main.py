import Day12

# importing the function from Day12.py file and calling it in main.py file
print(Day12.generate_full_name("Lou", "Pampa"))

# importing all the functions in case we had
##from Day12 import *

###########################################################

# importing the module OS
# OS module automatically perform many operating system tasks.
# Provides function for creating, changing current working directory, and removing a directory(folder), fetching its contents, changing and identifying the current directory.

# import os

# os.mkdir("directory_name")  # create a directory
# os.chdir("path")  # change the current working directory
# os.getcwd()  # get the current working directory
# os.rmdir  # removes directory

###########################################################

# importing sys module
# SYS module provides functions and variables used to manipulate different parts of the Python runtime environment.
# Function sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

# import sys

# # This line would print out: filename argument1 argument2
# print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!")

# Statistics Module
# Provides functions for mathematical statistics of numeric data. The popular statistical functions which are defince in this module: mean, median, mode, stdev etc.

from statistics import *

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(mean(ages))  # mean
print(median(ages))  # median
print(mode(ages))  # mode
print(stdev(ages))  # standard deviation

# Math Module
# Provides many mathematical operations and constants.

import math

print(math.pi)  # pi constant
print(math.sqrt(2))  # square root
print(math.pow(3, 2))  # power / 8.0
print(math.floor(9.81))  # rounding to lowest integer / 9.0
print(math.ceil(9.81))  # rounding to highest integer / 10.0
print(math.log10(100))  # logarithm / 2.0

# we can also import all

# from math import *
# print(pi)                  # 3.141592653589793, pi constant
# print(sqrt(2))             # 1.4142135623730951, square root
# print(pow(2, 3))           # 8.0, exponential
# print(floor(9.81))         # 9, rounding to the lowest
# print(ceil(9.81))          # 10, rounding to the highest
# print(math.log10(100))     # 2

# we can rename the name of the function

# from math import pi as  PI
# print(PI) # 3.141592653589793

# String module
# Many purposes like checking if a string is printable, checking if a string is whitespace, checking if a string is a digit, checking if a string is a letter, checking if a string is alphanumeric, checking if a string is lowercase, checking if a string is uppercase, and many more.
import string

print(
    string.ascii_letters
)  # all ascii letters / abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(
    string.ascii_lowercase
)  # all ascii lowercase letters / abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # all ascii uppercase letters / ABCDEFGHIJKLMNOP
print(string.digits)  # all ascii digits / 0123456789
print(string.punctuation)  # all ascii punctuation / !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)  # all ascii whitespace /  \t\n\r\x0b\x0c
print(
    string.printable
)  # all printable ascii characters / 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(
    string.capwords("hello world")
)  # capitalizes the first letter of each word / Hello World
print(
    string.capwords("hello world", sep=",")
)  # capitalizes the first letter of each word / Hello,World
