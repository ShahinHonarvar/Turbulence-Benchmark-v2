from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8]
    s = s.lower()
    letters = set(s)
    palindromes = set()
    for length in range(7, len(s) + 1):
        for perm in permutations(letters, length):
            half = ''.join(perm)
            full = half + half[-2::-1]
            if full in s and full not in palindromes:
                palindromes.add(full)
    return palindromes