from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            perm_str = ''.join(perm).lower()
            if perm_str == perm_str[::-1]:
                found_palindromes.add(perm_str)
    return found_palindromes