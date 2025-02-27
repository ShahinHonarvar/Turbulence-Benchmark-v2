import re

def palindrome_of_length_at_least_n(string):
    min_length = 41
    english_letters = re.sub('[^A-Za-z]+', '', string)
    palindromes = set()
    for i in range(len(english_letters) - min_length + 1):
        for j in range(i + min_length, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes