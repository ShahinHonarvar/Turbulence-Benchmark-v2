from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes