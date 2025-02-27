from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    letters = [c for c in s[3:7] if c.lower() in ascii_letters]
    perms = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = {p.lower() for p in perms if p.lower() == p.lower()[::-1] and len(p) >= 4}
    return palindromes