# File Handling - Day 19

import os


# Write a function which count number of lines and number of words in a text.
## Read obama_speech.txt, michelle_obama_speech.txt, donald_speech.txt, melina_trump_speech.txt
def count_lines_and_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count


files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt",
]

for filename in files:
    path = os.path.join("data", filename)
    lines, words = count_lines_and_words(path)
    print(f"{filename}: {lines} lines, {words} words")
