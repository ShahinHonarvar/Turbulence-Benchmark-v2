from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letters = ''.join([c for c in substring if c.isalpha()])
    found_palindromes = set()
    for r in range(7, len(letters) + 1):
        for perm in permutations(letters, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes