from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8].lower()
    possible_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            possible_palindromes.add(candidate)
    return possible_palindromes