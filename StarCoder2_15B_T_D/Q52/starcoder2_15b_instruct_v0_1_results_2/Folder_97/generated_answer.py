import re

def palindrome_of_length_n(string):
    substrings = set()
    n = 210
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            substrings.add(substring)
    palindromes = set()
    for substring in substrings:
        match = re.search('^[a-zA-Z]+$', substring)
        if match:
            palindromes.add(substring)
    return palindromes