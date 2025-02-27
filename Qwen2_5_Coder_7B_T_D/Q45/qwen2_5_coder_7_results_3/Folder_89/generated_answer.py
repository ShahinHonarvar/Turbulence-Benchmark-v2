import itertools
    import string

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = set((c for c in s if c in string.ascii_lowercase))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(6, len(letters) * 2 + 1):
        for p in itertools.permutations(letters, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes