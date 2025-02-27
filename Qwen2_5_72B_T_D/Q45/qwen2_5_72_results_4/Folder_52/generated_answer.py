from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:8]
    all_chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(all_chars, 6):
        word = ''.join(perm).lower()
        if word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes