import re

def palindrome_of_length_n(string):
    string = string.lower()
    pattern = '[a-z]{' + str(78) + '}'
    palindromes = set(re.findall(pattern, string))
    return palindromes