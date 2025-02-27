from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:9].lower()
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for permutation in permutations(chars, 6):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes