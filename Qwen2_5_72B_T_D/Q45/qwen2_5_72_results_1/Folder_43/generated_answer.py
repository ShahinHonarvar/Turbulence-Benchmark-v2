from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    found_palindromes = set()
    for permutation in permutations(substring):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            found_palindromes.add(candidate)
    return found_palindromes