from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7]
    valid_chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(4, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes