from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c in string.ascii_letters]
    perms = set([''.join(p) for p in permutations(letters, len(letters))])
    palindromes = {p for p in perms if len(p) >= 5 and p == p[::-1]}
    return palindromes