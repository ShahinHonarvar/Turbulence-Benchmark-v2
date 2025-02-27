from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    letters = [char for char in substring if char.isalpha()]
    all_permutations = set([''.join(p) for p in permutations(letters)])
    valid_palindromes = set()
    for p in all_permutations:
        if len(p) >= 3 and p == p[::-1]:
            valid_palindromes.add(p)
    return valid_palindromes