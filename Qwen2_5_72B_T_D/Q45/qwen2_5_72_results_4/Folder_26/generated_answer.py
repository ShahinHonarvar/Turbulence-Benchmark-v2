from itertools import permutations

def palindromes_between_indices(s):

    def generate_palindromes(chars):
        palindromes = set()
        for perm in permutations(chars, 3):
            if perm[0].lower() == perm[2].lower():
                palindromes.add(''.join(perm))
        return palindromes
    if len(s) < 7:
        return set()
    chars = [char for char in s[4:7] if char.isalpha()]
    if len(chars) < 3:
        return set()
    return generate_palindromes(chars)