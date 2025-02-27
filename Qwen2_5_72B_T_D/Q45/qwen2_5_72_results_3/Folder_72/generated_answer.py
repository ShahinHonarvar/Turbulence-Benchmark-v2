from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:8]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for permutation in permutations(letters, 6):
        word = ''.join(permutation)
        if word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes