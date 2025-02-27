from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[2:4])).lower()
    perms = set((''.join(p) for p in permutations(letters, 2)))
    palindromes = set()
    for perm in perms:
        for c in set(s).filter(str.isalpha):
            c = c.lower()
            p = perm[0] + c + perm[1]
            if p == p[::-1]:
                palindromes.add(p)
    return {p for p in palindromes if len(p) >= 3}