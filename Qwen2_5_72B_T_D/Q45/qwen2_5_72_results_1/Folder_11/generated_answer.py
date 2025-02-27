from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    characters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(characters, len(characters)):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes