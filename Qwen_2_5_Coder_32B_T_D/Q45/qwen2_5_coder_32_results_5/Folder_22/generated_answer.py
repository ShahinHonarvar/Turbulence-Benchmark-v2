from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = set(s[5:7].lower()).intersection(string.ascii_lowercase)
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes