import re

def palindrome_of_length_n(text):
    palindromes = set()
    regex = re.compile('[a-zA-Z]{20}')
    for i in range(len(text) - 19):
        substring = text[i:i + 20]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes