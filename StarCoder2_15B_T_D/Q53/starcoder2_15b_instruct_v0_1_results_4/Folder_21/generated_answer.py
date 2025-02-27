import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[A-Za-z]{112,}')
    matches = pattern.findall(string)
    palindromes = set((word for word in matches if word.lower() == word[::-1]))
    return palindromes