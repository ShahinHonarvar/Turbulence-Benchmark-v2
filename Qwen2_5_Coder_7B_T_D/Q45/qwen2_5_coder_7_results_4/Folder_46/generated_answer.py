from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = set(s)
    palindromes = set()
    for r in range(6, len(s) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes