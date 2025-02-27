from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:9]
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(chars, len(chars)):
        word = ''.join(perm).lower()
        if len(word) >= 4 and word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes