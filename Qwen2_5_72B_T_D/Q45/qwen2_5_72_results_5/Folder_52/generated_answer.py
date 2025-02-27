from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm).lower()
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            found_palindromes.add(perm_str)
    return found_palindromes