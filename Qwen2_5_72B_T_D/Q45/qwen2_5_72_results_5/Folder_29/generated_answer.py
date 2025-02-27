from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 6):
        perm_str = ''.join(perm)
        if perm_str.lower() == perm_str.lower()[::-1]:
            found_palindromes.add(perm_str)
    return found_palindromes