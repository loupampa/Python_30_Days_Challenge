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
