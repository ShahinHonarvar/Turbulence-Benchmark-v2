from itertools import permutations

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    prefix = s[1:6]
    palindromes = set()
    for perm in permutations(prefix):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes