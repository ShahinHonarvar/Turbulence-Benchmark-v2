import re

def palindrome_of_length_n(string):
    palindromes = set()
    n = 366
    for i in range(len(string) - n + 1):
        substr = string[i:i + n]
        if substr == substr[::-1] and re.match('^[a-zA-Z]+$', substr):
            palindromes.add(substr)
    return palindromes