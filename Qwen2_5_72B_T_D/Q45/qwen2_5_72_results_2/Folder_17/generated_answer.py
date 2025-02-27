from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    possible_palindromes = set()
    for perm in permutations(substring):
        candidate = ''.join(perm)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            possible_palindromes.add(candidate)
    return possible_palindromes