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

import sys

# This line would print out: filename argument1 argument2
print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!")
