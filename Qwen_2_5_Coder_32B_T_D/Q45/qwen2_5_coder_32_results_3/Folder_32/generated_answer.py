from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(x):
        return x == x[::-1]
    letters = [c.lower() for c in s[1:8] if c.isalpha()]
    perms = set([''.join(p) for p in permutations(letters)])
    return {p for p in perms if len(p) >= 5 and is_palindrome(p)}