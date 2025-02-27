from itertools import permutations

def palindromes_between_indices(s):
    substr = s[2:10]
    letter_counts = [char for char in substr if char.isalpha()]
    possible_palindromes = set()
    for perm in permutations(letter_counts, len(letter_counts)):
        perm_str = ''.join(perm).lower()
        if perm_str == perm_str[::-1] and len(perm_str) >= 6:
            possible_palindromes.add(perm_str)
    return possible_palindromes