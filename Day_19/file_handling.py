# File Handling - Day 19
from pathlib import Path


# Write a function which count number of lines and number of words in a text.
## Read obama_speech.txt, michelle_obama_speech.txt, donald_speech.txt, melina_trump_speech.txt
def count_lines_and_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
    return line_count, word_count


script_dir = Path(__file__).resolve().parent

files = [
    "obama_speech.txt",
    "michelle_obama_speech.txt",
    "donald_speech.txt",
    "melina_trump_speech.txt",
]

for filename in files:
    path = script_dir / filename
    lines, words = count_lines_and_words(path)
    print(f"{filename}: {lines} lines, {words} words")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages.
