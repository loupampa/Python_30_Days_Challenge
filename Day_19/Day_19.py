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

## Opening File for Writing and Updating
# To write to an existing file, we must add a mode as parameter to the open() function:
# "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.
# with open('./files/reading_file_example.txt','a') as f:
#     f.write('This text has to be appended at the end')

## Deleting Files
# We have seen in previous section, how to make and remove a directory using os module.
# import os
# os.remove('./files/example.txt')
# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:
# import os
# if os.path.exists('./files/example.txt'):
#     os.remove('./files/example.txt')
# else:
#     print('The file does not exist')

## File Types
# File with txt extension is a very common form of data and we have covered it in previous section.
# File with json extension is a stringified JavaScript object
# dictionary
# person_dct= {
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }
# # JSON: A string form a dictionary
# person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# # we use three quotes and make it multiple line to make it more readable
# person_json = '''{
#     "name":"Asabeneh",
#     "country":"Finland",
#     "city":"Helsinki",
#     "skills":["JavaScrip", "React","Python"]
# }'''

## Changing JSON to Dictionary
# first we import the json module and then we use loads method.
# import json
# # JSON
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''
# # let's change JSON to dictionary
# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])
