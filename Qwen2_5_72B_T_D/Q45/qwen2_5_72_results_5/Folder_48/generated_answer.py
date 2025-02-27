from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    found_palindromes = set()
    for perm in permutations(letters, 3):
        candidate = perm[0] + perm[1] + perm[2] + perm[1] + perm[0]
        if candidate not in found_palindromes:
            found_palindromes.add(candidate)
    return found_palindromes