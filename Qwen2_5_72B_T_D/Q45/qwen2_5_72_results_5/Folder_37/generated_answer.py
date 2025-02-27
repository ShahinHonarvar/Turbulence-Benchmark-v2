from itertools import permutations

def palindromes_between_indices(s):
    subset = s[1:5]
    letters = [char.lower() for char in subset if char.isalpha()]
    found_palindromes = set()
    for length in range(5, len(letters) + 1):
        for perm in permutations(letters, length):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                found_palindromes.add(candidate)
    return found_palindromes