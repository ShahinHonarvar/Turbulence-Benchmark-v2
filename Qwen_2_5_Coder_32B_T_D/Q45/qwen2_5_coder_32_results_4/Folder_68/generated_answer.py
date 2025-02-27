from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:9])).lower()
    perms = set((''.join(p) for p in permutations(letters, min(8, len(letters)))))
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes