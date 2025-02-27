import re

def palindrome_of_length_n(s):
    s = s.lower()
    four_ninety_palindromes = {s[i:i + 49] for i in range(len(s) - 48)}
    return {p for p in four_ninety_palindromes if p == p[::-1] and re.match('^[a-z]*$', p)}