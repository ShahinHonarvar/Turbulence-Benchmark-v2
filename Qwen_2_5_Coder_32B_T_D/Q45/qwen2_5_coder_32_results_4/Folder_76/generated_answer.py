import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:5] if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 4:
            palindromes.add(p)
    return palindromes