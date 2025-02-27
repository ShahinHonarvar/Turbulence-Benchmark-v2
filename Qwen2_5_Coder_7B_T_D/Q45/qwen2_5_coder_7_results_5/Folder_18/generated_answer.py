from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    letters = set(s)
    palindromes = set()
    for r in range(3, len(s) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes