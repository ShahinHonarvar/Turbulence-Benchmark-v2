from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7]
    chars = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for r in range(3, len(chars) + 1):
        for perm in permutations(chars, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes