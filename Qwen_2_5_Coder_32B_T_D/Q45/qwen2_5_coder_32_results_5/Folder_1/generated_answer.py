import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            palindromes.add(p)
    return palindromes