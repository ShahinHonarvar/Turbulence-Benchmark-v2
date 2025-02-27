import re

def palindrome_of_length_n(string):
    pattern = '.{{{n}}}'.format(n=15)
    substrings = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = set((s for s in substrings if s == s[::-1]))
    return palindromes