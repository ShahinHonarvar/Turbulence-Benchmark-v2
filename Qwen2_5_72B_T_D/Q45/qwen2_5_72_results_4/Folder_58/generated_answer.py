from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:7]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes