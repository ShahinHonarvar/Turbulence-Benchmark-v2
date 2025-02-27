from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[8:10] if c.isalpha()]
    if len(letters) < 2:
        return set()
    perms = set((''.join(p) for p in permutations(letters, 2)))
    palindromes = set()
    for perm in perms:
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if perm[0] == c or perm[1] == c:
                p = c + perm + c
                palindromes.add(p)
    return {p for p in palindromes if len(p) >= 3}