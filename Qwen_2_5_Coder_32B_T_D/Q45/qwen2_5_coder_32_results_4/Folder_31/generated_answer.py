from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:9] if c.isalpha()]
    letters = ''.join(letters).lower()
    n = len(letters)
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 6:
            palindromes.add(p)
    return palindromes