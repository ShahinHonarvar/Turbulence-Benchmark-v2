from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[1:8].lower())
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes