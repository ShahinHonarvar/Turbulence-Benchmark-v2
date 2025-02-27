from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:8]
    filtered = ''.join([char for char in substring if char.isalpha()])
    found_palindromes = set()
    for perm in permutations(filtered, len(filtered)):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            found_palindromes.add(word)
    return found_palindromes