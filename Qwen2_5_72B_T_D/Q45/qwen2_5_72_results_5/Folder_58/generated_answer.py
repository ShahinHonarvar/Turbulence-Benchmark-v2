from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 6):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower():
            found_palindromes.add(candidate)
    return found_palindromes