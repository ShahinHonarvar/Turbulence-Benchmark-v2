from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[4:7]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    unique_permutations = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i)))
    return {p for p in unique_permutations if is_palindrome(p)}