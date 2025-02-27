from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9].lower()
    letters = set(s)
    palindromes = set()
    for r in range(7, len(s) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes