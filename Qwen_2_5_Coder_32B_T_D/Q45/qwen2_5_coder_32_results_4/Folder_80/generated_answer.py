import itertools
    import string

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.lower() in string.ascii_lowercase]
    palindromes = set()
    for perm in itertools.permutations(letters, 7):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes