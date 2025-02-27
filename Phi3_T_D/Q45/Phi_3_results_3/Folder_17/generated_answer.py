from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    from_index = 2
    to_index = 6
    substring = s[from_index:to_index + 1]
    letters = ''.join(set(substring.lower()))
    valid_perms = {''.join(p) for i in range(4, len(substring) + 1) for p in permutations(letters, i)}
    return {p for p in valid_perms if is_palindrome(p)}