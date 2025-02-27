from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6].lower()
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes