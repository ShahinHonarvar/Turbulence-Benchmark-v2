import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '.{' + str(92) + '}'
    palindromes = set()
    for match in re.finditer(pattern, string):
        substring = match.group()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes