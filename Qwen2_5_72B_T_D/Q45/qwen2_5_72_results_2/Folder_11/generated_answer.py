from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    found_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            found_palindromes.add(candidate)
    return found_palindromes