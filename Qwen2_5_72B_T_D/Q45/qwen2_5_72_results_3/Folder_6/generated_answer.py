from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    found_palindromes = set()
    for permutation in permutations(substring, 4):
        candidate = ''.join(permutation).lower()
        if candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes