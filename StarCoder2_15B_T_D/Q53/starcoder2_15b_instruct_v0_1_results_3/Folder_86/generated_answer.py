import re

def palindrome_of_length_at_least_n(s):
    pattern = '[a-zA-Z]{133,}'
    matches = re.findall(pattern, s)
    palindromes = set((m for m in matches if m == m[::-1]))
    return palindromes