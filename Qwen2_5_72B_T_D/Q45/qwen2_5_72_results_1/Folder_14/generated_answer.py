from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:6]
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            candidate = ''.join(perm).lower()
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes