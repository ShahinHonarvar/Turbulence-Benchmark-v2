from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes