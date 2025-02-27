from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:5] if c.lower() in string.ascii_lowercase])
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes