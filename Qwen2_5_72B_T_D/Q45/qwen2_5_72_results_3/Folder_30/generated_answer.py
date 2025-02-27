from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        perm_str = ''.join(perm).lower()
        if len(perm_str) >= 4 and perm_str == perm_str[::-1]:
            palindromes.add(perm_str)
    return palindromes