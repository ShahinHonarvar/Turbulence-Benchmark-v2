from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.lower() in string.ascii_lowercase]
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for perm in perms:
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes