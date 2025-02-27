from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    alphas = ''.join(filter(str.isalpha, s))
    perms = set((''.join(p) for p in permutations(alphas, len(alphas))))
    palindromes = {p for p in perms if len(p) >= 4 and p == p[::-1]}
    return palindromes