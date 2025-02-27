from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm).lower()
        if word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes