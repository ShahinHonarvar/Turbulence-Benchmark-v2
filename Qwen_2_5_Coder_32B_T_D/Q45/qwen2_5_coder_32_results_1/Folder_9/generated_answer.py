import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for perm in itertools.permutations(letters, 7):
        p = ''.join(perm)
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes