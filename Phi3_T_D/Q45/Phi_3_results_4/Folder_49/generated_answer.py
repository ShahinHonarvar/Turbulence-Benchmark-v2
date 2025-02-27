from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8].lower()
    n = len(substring)
    palindromic_permutations = set([''.join(p) for p in permutations(substring) if p == p[::-1] and n >= 3])
    return set((w for w in palindromic_permutations if len(w) >= 3))