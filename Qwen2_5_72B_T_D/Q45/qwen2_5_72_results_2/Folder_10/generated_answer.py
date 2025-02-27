from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for permutation in permutations(letters, len(letters)):
        word = ''.join(permutation).lower()
        if len(word) >= 3 and word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes