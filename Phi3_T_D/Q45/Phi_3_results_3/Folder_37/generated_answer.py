from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    for length in range(5, len(s) + 1):
        perms = set((''.join(p) for p in permutations(s[1:5])))
        palindromes = {perm for perm in perms if is_palindrome(perm.upper())}
        if palindromes:
            return palindromes
    return set()