# File Handling - Day 19

## File handling is an import part of programming which allows us to create, read, update and delete file.
# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

## Opening File for Reading
# The default mode of open is reading, so we do not have to specify 'r' or 'rt'
# f = open('./files/reading_file_example.txt')
# print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# read(): read the whole text as string, If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method
# f = open('./files/reading_file_example.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()

# readline(): read only the first line
# f = open('./files/reading_file_example.txt')
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# readlines(): read all the text line by line and returns a list of lines
# f = open('./files/reading_file_example.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# splitlines()
# f = open('./files/reading_file_example.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()
