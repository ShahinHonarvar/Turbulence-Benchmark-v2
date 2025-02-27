from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    start, end = (6, 8)
    letters = [s[i].lower() for i in range(start, end + 1) if s[i].isalpha()]
    unique_perms = set((''.join(p) for p in permutations(letters)))
    palindromes = {perm for perm in unique_perms if len(perm) >= 3 and is_palindrome(perm)}
    return palindromes