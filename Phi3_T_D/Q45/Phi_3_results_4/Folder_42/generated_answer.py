from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def create_palindromes(chunk):
    perms = [''.join(p) for p in permutations(chunk)]
    return set(filter(is_palindrome, perms))

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    chunk = s[6:10].lower()
    return create_palindromes(chunk)