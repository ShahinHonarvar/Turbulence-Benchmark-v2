from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8]
    letters = [char for char in substring if char.isalpha()]
    possible_palindromes = set()
    for perm in permutations(letters, 3):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1]:
            possible_palindromes.add(candidate)
    return possible_palindromes