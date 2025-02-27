from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    required_length_palindromes = set()
    for permutation in permutations(substring):
        candidate = ''.join(permutation)
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            required_length_palindromes.add(candidate)
    return required_length_palindromes