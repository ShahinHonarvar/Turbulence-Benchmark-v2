from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = ''.join(set(s))
    if len(letters) < 6:
        return set()
    perms = {''.join(p) for i in range(1, len(letters) + 1) for p in permutations(letters, i) if len(p) >= 6}
    return {p for p in perms if is_palindrome(p)}