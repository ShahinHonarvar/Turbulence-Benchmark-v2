from itertools import permutations

def palindromes_between_indices(s):
    prefix = s[:6]
    letters = ''.join(sorted(filter(str.isalpha, prefix.lower())))
    unique_perms = set((''.join(p) for p in permutations(letters, 4)))
    palindromes = {''.join(p + p[::-1]) for p in unique_perms}
    return palindromes