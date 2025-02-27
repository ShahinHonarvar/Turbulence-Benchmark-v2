import itertools
    import string

def palindromes_between_indices(s):
    letters = set(s[:4]) & set(string.ascii_letters)
    palindromes = set()
    for perm in itertools.permutations(letters, 3):
        p = ''.join(perm).lower()
        if p == p[::-1]:
            palindromes.add(p)
    return palindromes