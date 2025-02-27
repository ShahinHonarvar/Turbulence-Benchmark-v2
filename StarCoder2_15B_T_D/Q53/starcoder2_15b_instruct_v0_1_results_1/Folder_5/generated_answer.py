import re

def palindrome_of_length_at_least_n(string):
    pattern = '\\b[a-zA-Z]{46,}\\b'
    matches = re.findall(pattern, string)
    palindromes = set((match for match in matches if match == match[::-1]))
    return palindromes