from itertools import permutations

def palindromes_between_indices(s):
    substring = s[5:8]
    found_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes