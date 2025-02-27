from itertools import permutations

def palindromes_between_indices(s):
    subset = s[0:8]
    letters = [ch for ch in subset if ch.isalpha()]
    found_palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes