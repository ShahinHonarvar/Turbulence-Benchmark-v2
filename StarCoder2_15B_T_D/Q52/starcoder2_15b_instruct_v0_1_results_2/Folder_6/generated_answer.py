import re

def palindrome_of_length_n(string):
    pattern = re.compile('[a-zA-Z]{474}')
    substrings = pattern.findall(string)
    palindromes = set(filter(lambda x: x == x[::-1], substrings))
    return palindromes