from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.lower() in string.ascii_lowercase]
    perms = set(permutations(letters, len(letters)))
    palindromes = set()
    for perm in perms:
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes