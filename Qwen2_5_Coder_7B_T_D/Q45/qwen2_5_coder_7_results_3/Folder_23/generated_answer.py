from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:7].lower()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes