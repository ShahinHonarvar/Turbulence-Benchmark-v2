from collections import defaultdict
import re
import string

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    substring = text[:8]
    valid_letters = set(string.ascii_letters)
    length_to_palindromes = defaultdict(set)
    substring = ''.join((ch for ch in substring if ch in valid_letters))
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                candidate = substring[i:i + length]
                if is_palindrome(candidate):
                    length_to_palindromes[length].add(candidate.lower())
    if 4 in length_to_palindromes or 5 in length_to_palindromes:
        min_length = 4
        return set.union(*[length_to_palindromes[l] for l in range(min_length, min(6, len(substring) + 1))])
    else:
        return set()