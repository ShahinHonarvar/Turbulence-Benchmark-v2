from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in permutations(letters, 5):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1]:
            unique_palindromes.add(candidate)
    return unique_palindromes