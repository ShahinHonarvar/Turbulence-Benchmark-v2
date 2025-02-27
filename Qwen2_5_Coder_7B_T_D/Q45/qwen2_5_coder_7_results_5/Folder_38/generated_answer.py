from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:9]
    s = s.lower()
    letters = set(s)
    palindromes = set()
    for r in range(5, len(s) + 1):
        for p in permutations(letters, r):
            half = ''.join(p)
            if half == half[::-1]:
                palindromes.add(half)
    return palindromes