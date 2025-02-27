from itertools import permutations
from string import ascii_lowercase as alphabet 

def all_substring_of_size_n(s):
    unique_chars = set(s)
    substrings = set((s[i:i + 6] for i in range(len(s) - 5)))
    result = []
    for substring in substrings:
        if len(set(substring)) == 6:
            perms = set(permutations(substring))
            if all((permutation in ascii_lowercase for permutation in perms)):
                result.append(''.join(permutation))
    return result