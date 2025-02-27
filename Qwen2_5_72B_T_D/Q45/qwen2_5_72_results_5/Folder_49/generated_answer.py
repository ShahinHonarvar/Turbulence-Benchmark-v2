from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        palindromes = set()
        for perm in permutations(chars):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 3:
                palindromes.add(candidate)
        return palindromes
    chars = s[5:8]
    return generate_palindromes(chars)