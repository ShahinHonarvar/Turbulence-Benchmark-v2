from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:8].lower()
    letters = ''.join((c for c in substring if c.isalpha()))
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            found_palindromes.add(candidate.lower())
    return found_palindromes