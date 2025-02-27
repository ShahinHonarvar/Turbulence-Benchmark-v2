from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:9].lower()
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 5:
            found_palindromes.add(candidate)
    return found_palindromes