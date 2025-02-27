from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(s):
    letters_range = set(s[2:6].lower()) if len(s) > 4 else set()
    palindromes = set()
    for perm_length in range(5, min(len(letters_range) + 1, 6)):
        for p in permutations(letters_range, perm_length):
            if p == tuple(reversed(p)):
                palindromes.add(''.join(p))
    return palindromes