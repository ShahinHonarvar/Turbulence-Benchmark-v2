from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:6]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters, 4):
        word = ''.join(perm).lower()
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes