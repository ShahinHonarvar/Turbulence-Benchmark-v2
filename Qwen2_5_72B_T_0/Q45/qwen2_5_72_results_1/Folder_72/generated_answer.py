from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 6):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes