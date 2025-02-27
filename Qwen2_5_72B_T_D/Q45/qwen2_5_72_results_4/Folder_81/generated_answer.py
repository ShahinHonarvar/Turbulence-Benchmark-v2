from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7]
    letters = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(letters, 3):
        word = ''.join(perm)
        if word.lower() == word[::-1].lower():
            found_palindromes.add(word)
    return found_palindromes