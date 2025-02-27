from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters = set(s[3:10].lower())
    letter_permutations = set((''.join(p) for i in range(3, 10) for p in permutations(letters, i)))
    return {p for p in letter_permutations if is_palindrome(p)}