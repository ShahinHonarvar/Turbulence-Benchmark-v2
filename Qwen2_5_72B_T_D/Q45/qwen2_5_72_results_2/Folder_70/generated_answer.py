from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:7]
    letters = [char.lower() for char in substring if char.isalpha()]
    possible_palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            possible_palindromes.add(word)
    return possible_palindromes