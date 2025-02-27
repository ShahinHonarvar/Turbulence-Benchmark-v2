import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '.{' + str(401) + '}'
    substrings = re.findall(pattern, string)
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes