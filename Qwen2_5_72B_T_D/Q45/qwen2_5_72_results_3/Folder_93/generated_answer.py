from itertools import permutations
    from string import ascii_letters

def palindromes_between_indices(s):
    substring = s[2:8]
    valid_chars = [char for char in substring if char in ascii_letters]
    valid_chars = [char.lower() for char in valid_chars]
    found_palindromes = set()
    for perm in permutations(valid_chars, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            found_palindromes.add(word)
    return found_palindromes