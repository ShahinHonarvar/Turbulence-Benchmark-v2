from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for p in perms:
        candidate = ''.join(p)
        if candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes