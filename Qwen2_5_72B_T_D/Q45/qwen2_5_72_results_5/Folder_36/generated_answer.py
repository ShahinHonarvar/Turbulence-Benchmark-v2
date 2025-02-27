from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:9].lower()
    found_palindromes = set()
    for permutation in set(permutations(substring)):
        candidate = ''.join(permutation)
        if len(candidate) >= 3 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes