from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:5]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 4):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes