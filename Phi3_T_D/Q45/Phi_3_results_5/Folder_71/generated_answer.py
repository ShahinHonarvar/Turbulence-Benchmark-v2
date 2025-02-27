from itertools import permutations

def palindromes_between_indices(s):
    subset = s[1:4].lower()
    unique_chars = set(subset)
    palindromes = {''.join(p) for p in permutations(unique_chars) if p == p[::-1]}
    return {p for p in palindromes if len(p) >= 4}