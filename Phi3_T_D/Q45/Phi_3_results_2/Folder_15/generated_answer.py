from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:3].lower()
    perms = set((''.join(p) for p in permutations(substr)))
    palindromes = {p[:l] + p[:l][::-1] for l in range(1, min(3, len(substr) + 1)) for p in perms if p[:l] == p[l - 1::-1]}
    return palindromes