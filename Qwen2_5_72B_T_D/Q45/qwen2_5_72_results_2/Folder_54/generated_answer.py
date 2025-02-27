from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    chars = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(chars):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            found_palindromes.add(word)
    return found_palindromes