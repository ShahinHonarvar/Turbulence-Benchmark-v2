from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:8]
    valid_chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(valid_chars, len(valid_chars)):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 5:
            found_palindromes.add(candidate)
    return found_palindromes