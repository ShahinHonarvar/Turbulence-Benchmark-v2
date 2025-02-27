from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:8])).lower()
    l = len(letters)
    if l < 4:
        return set()
    perms = set((''.join(p) for p in permutations(letters, l)))
    palindromes = {p for p in perms if p == p[::-1]}
    return {p for p in palindromes if len(p) >= 4}