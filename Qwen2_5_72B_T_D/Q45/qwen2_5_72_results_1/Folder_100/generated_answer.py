from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    chars = [char.lower() for char in substring if char.isalpha()]
    unique_palindromes = set()
    for perm in permutations(chars, len(chars)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            unique_palindromes.add(candidate)
    return unique_palindromes