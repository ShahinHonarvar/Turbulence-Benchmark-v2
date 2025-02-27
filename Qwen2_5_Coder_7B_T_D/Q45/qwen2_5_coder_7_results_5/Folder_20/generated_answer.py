from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:9] if char.isalpha()]
    if len(letters) < 4:
        return set()
    perms = set([''.join(p) for p in permutations(letters, 4) if p == p[::-1]])
    return perms