from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    all_palindromes = set()
    for perm in permutations(letters, 4):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            all_palindromes.add(candidate)
    return all_palindromes