import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{86,}\\b'
    matches = re.findall(pattern, string)
    palindromes = [word for word in matches if word == word[::-1]]
    return set(palindromes)