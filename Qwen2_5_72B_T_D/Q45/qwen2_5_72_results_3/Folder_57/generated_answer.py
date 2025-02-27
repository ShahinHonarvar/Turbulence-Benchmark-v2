from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if len(candidate) >= 5 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes