import re

def palindromes_of_specific_lengths(text):
    substring = text[27:78]
    palindromes = set(filter(lambda word: word == word[::-1] and len(word) in {18, 19} and re.match('[a-z]+$', word, re.IGNORECASE), re.findall('\\\\b[a-zA-Z]{18,19}\\\\b', substring)))
    return palindromes