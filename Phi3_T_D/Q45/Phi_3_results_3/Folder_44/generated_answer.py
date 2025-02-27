from itertools import permutations

def palindromes_between_indices(s):
    target_str = s[2:8].lower()
    palindromes = {p[0] + p[1] + p[0] for p in permutations(target_str) if p[0] != p[1]}
    return {p for p in palindromes if p == p[::-1]}