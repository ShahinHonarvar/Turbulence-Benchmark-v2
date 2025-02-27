from itertools import permutations

def palindromes_between_indices(s):
    s = s[:6].lower()
    chars = set(s)
    palindromes = set()
    for r in range(6, len(s) + 1):
        for p in permutations(chars, r):
            half = ''.join(p)
            if half == half[::-1]:
                palindromes.add(half)
    return palindromes