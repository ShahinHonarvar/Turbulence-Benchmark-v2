from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    desired_chars = s[0:6].lower()
    valid_chars = set((c for c in desired_chars if c in ascii_lowercase))

    def is_palindrome(word):
        return word == word[::-1]
    possible_palindromes = set()
    for length in range(6, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            word = ''.join(perm)
            if is_palindrome(word):
                possible_palindromes.add(word)
    return possible_palindromes