from itertools import permutations

def palindromes_between_indices(s):

    def is_valid_char(c):
        return c.isalpha()

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[4:10]
    valid_chars = [c.lower() for c in substring if is_valid_char(c)]
    if len(valid_chars) < 3:
        return set()
    possible_combinations = set()
    for length in range(3, len(valid_chars) + 1, 2):
        for perm in permutations(valid_chars, length):
            possible_combinations.add(''.join(perm))
        for perm in permutations(valid_chars, length - 1):
            possible_combinations.add(''.join(perm) + ''.join(perm)[::-1])
    return {char for char in possible_combinations if is_palindrome(char)}