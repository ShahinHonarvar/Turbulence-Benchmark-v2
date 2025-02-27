from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    unique_chars = set(s)
    palindromes = set()
    for r in range(7, len(unique_chars) + 1):
        for perm in permutations(unique_chars, r):
            half = ''.join(perm)
            if half == half[::-1]:
                palindromes.add(half)
    return palindromes