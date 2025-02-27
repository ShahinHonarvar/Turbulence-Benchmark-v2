from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[:8] if c.isalpha()]
    if len(letters) < 7:
        return set()
    palindromes = set()
    for perm in permutations(letters, 7):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes