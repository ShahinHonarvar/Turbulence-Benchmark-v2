from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:10] if char.isalpha()]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p for p in perms if len(p) >= 5 and p == p[::-1]}
    return palindromes