from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10]
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(chars, len(chars)):
        candidate = ''.join(perm).lower()
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes