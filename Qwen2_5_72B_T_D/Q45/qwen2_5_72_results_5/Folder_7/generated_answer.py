from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:10]
    letters = ''.join((ch for ch in substring if ch.isalpha()))
    found_palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes