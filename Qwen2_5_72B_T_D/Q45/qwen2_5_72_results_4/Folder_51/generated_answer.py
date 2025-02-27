from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    found_palindromes = set()
    for perm in set(permutations(substring)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 3:
            found_palindromes.add(candidate)
    return found_palindromes