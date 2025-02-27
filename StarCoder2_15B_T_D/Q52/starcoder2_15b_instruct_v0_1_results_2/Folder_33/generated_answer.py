import re

def palindrome_of_length_n(string):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(n) + '}'
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes