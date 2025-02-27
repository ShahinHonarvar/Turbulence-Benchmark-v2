import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[5:9])).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes