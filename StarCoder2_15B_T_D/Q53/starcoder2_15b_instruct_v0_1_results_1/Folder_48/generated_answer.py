import re

def palindrome_of_length_at_least_n(string):
    pattern = re.compile('[a-zA-Z]{150,}')
    matches = pattern.findall(string)
    palindromes = set((match for match in matches if match.lower() == match[::-1].lower()))
    return palindromes