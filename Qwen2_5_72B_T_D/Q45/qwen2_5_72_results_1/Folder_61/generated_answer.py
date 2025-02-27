from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:8]
    letters = ''.join((ch.lower() for ch in substring if ch.isalpha()))
    found_palindromes = set()
    for perm in permutations(letters, 7):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes