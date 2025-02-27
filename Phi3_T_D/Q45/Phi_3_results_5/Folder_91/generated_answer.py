from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(p):
        return p == p[::-1]
    letters = sorted([c.lower() for c in s[2:7] if 'a' <= c.lower() <= 'z'])
    unique_perms = set((''.join(p) for p in permutations(letters, len(letters))))
    return {p for p in unique_perms if is_palindrome(p) and len(p) >= 3}