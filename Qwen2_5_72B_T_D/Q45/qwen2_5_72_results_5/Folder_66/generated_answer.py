from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:6]
    letters = [char.lower() for char in substring if char.isalpha()]
    all_permutations = set([''.join(p) for p in permutations(letters)])
    palindromes = {word for word in all_permutations if len(word) >= 5 and word == word[::-1]}
    return palindromes