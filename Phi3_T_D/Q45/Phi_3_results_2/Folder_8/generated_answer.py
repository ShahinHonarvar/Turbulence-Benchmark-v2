from itertools import permutations

def palindromes_between_indices(s):
    target = s[1:6].lower()
    letters = [char for char in target if char.isalpha()]
    if len(letters) < 5:
        return set()
    valid_palindromes = set()
    for perm in set(permutations(letters, 5)):
        candidate = ''.join(perm).upper()
        if candidate == candidate[::-1]:
            valid_palindromes.add(candidate)
    return valid_palindromes