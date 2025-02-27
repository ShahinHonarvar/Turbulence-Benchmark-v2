import itertools
    import string

def palindromes_between_indices(s):
    letters = set(s[2:9].lower()) & set(string.ascii_lowercase)
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for comb in itertools.combinations(letters, r):
            for perm in itertools.permutations(comb):
                p = ''.join(perm)
                if p == p[::-1] and len(p) >= 4:
                    palindromes.add(p)
    return palindromes