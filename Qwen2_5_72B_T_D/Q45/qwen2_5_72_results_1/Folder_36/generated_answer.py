from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        palindromes = set()
        for perm in permutations(chars, 4):
            if perm[0].lower() == perm[3].lower() and perm[1].lower() == perm[2].lower():
                palindromes.add(''.join(perm))
        return palindromes
    substring = s[5:9]
    valid_chars = [ch for ch in substring if ch.isalpha()]
    if len(valid_chars) < 4:
        return set()
    return generate_palindromes(valid_chars)