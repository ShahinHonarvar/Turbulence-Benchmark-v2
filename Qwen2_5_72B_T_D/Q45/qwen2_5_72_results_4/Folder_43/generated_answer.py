from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    valid_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            valid_palindromes.add(candidate)
    return valid_palindromes