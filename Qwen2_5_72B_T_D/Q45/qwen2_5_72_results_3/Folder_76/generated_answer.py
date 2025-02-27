from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:5]
    letter_set = {char.lower() for char in substring if char.isalpha()}
    all_palindromes = set()
    for permutation in permutations(letter_set, len(letter_set)):
        candidate = ''.join(permutation)
        if candidate == candidate[::-1] and len(candidate) >= 4:
            all_palindromes.add(candidate)
    return all_palindromes