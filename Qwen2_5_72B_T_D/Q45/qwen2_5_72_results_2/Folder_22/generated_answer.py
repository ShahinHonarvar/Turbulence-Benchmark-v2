from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:7].lower()
    perms = set([''.join(p) for p in permutations(substring)])
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 3}
    return palindromes