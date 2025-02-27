from itertools import permutations

def palindromes_between_indices(s: str) -> set:
    start, end = (0, 8)
    letters = [char.lower() for char in s[start:end] if char.isalpha()]
    mutations = set(permutations(letters, len(letters)))
    palindromes = {''.join(perm[:3]) + perm[2] + perm[3:][::-1] for perm in mutations if len(perm) >= 6}
    return palindromes