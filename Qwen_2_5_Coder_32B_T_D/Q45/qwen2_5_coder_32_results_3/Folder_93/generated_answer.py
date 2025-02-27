from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 6:
            palindromes.add(p)
    return palindromes