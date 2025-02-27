import re

def palindrome_of_length_at_least_n(text):
    pattern = '[A-Za-z]{30,}'
    matches = re.findall(pattern, text)
    palindromes = set((match for match in matches if match == match[::-1]))
    return palindromes