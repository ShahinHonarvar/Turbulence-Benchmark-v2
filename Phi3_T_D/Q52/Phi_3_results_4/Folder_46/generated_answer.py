import re

def palindrome_of_length_n(s):
    set_palindromes = set()
    s = s.lower()
    for i in range(len(s) - 463):
        candidate = s[i:i + 464]
        if candidate == candidate[::-1]:
            set_palindromes.add(candidate)
    return set_palindromes