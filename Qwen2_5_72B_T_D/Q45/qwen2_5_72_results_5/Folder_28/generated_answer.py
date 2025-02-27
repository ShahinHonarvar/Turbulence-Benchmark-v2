from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6]
    char_list = [char for char in substring if char.isalpha()]
    found_palindromes = set()
    for perm in permutations(char_list, len(char_list)):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            found_palindromes.add(word)
    return found_palindromes