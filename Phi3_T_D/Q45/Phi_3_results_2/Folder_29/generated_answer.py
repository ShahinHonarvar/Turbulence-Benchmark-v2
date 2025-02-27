import itertools
import re

def is_palindrome(word):
    return word.lower() == word[::-1].lower() and len(word) >= 6

def palindromes_between_indices(s):
    substring = s[2:10]
    unique_chars = sorted(set(re.findall('[a-zA-Z]', substring.lower())))
    possible_permutations = set()
    for i in range(len(unique_chars), 0, -1):
        for perm in itertools.permutations(unique_chars, i):
            possible_permutations.add(''.join(perm))
    palindromes = {word for word in possible_permutations if is_palindrome(word)}
    return palindromes