from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    target_letters = set(s[3:9].lower())
    valid_letters = ''.join(sorted(target_letters.intersection(alphabet)))
    valid_perms = set((''.join(p) for p in permutations(valid_letters, 6)))
    palindromes = set(filter(is_palindrome, valid_perms))
    return palindromes