from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        palindromes = set()
        for perm in permutations(chars, 5):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 4:
                palindromes.add(candidate)
        return palindromes
    substring = s[5:10]
    chars = [char for char in substring if char.isalpha()]
    return generate_palindromes(chars)