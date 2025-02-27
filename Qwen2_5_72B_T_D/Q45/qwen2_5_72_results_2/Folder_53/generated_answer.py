from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(chars, 6):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes