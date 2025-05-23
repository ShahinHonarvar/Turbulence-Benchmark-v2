from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 7:
            found_palindromes.add(candidate)
    return found_palindromes