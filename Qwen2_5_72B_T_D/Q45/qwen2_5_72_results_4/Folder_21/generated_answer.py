from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9].lower()
    found_palindromes = set()
    for permutation in permutations(substring):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 7:
            found_palindromes.add(candidate)
    return found_palindromes