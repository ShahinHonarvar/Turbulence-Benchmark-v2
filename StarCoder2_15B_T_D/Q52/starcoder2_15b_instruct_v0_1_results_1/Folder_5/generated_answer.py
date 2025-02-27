import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = re.compile('[a-zA-Z]{17}')
    for i in range(len(string) - 16):
        substring = string[i:i + 17]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes