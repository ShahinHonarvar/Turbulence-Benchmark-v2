from itertools import permutations

def palindromes_between_indices(s):
    letters = s[:8].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 4:
        return set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes