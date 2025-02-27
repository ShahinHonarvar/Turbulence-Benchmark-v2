import re
from itertools import product

def substrings(s):
    length = len(s)
    for i in range(length):
        for j in range(i + 21, length + 1):
            yield s[i:j]

def generate_palindromes(s):
    chars = set(s.lower())
    center_char = ''.join(chars)
    palindrome_set = set()
    for center in product(*[(center_char, '')] * 10):
        if center != ('',) * 10:
            palindrome_set.add(''.join(center + center[::-1]))
    return palindrome_set

def palindrome_of_length_at_least_n(string):
    return set(filter(lambda s: s.isalpha() and s == s[::-1], substrings(string.lower()))) & generate_palindromes(string.lower())