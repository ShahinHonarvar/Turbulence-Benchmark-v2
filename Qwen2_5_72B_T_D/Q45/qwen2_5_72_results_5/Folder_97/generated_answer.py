from itertools import permutations

def palindromes_between_indices(s):
    substr = s[0:5]
    letters = [char.lower() for char in substr if char.isalpha()]
    found_palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in set(permutations(letters, r)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes