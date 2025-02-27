from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(text):
    substring = text[0:6]
    letter_set = {char.lower() for char in substring if char.isalpha()}
    all_perms = {''.join(p) for i in range(4, len(letter_set) + 1) for p in permutations(letter_set, i)}
    return {perm for perm in all_perms if is_palindrome(perm)}