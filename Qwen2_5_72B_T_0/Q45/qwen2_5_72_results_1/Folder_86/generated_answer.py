from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes