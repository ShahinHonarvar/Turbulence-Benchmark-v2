from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        palindromes = set()
        for perm in permutations(chars, len(chars)):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 3:
                palindromes.add(candidate)
        return palindromes
    if len(s) < 8:
        return set()
    substring = s[5:8]
    valid_chars = [char for char in substring if char.isalpha()]
    return generate_palindromes(valid_chars)