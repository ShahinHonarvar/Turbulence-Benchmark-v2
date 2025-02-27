from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:5] if c.isalpha()]
    four_letter_perms = {''.join(p) for p in permutations(letters, 4)}
    palindromes = {perm for perm in four_letter_perms if perm == perm[::-1]}
    return palindromes