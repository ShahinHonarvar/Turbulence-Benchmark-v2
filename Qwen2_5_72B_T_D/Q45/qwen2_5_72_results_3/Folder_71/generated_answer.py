from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:4]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for permutation in permutations(letters, len(letters)):
        for length in range(4, len(permutation) + 1, 2):
            half = length // 2
            candidate = permutation[:half] + permutation[half - 1::-1]
            found_palindromes.add(''.join(candidate))
    return found_palindromes