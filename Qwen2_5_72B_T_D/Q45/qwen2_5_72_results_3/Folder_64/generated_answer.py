from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, len(letters)):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            found_palindromes.add(word)
    return found_palindromes