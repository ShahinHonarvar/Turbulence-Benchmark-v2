from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    all_permutations = {''.join(p) for p in permutations(substring)}
    palindromes = {p for p in all_permutations if p == p[::-1] and len(p) >= 3}
    return palindromes