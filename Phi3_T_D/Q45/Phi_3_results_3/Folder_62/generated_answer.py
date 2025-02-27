from itertools import permutations
import string

def palindromes_between_indices(s):
    filtered_chars = ''.join(filter(str.isalpha, s[:9].lower()))
    palindromes_set = set()
    for length in range(7, len(filtered_chars) + 1):
        perms = set([''.join(p) for p in permutations(filtered_chars, length)])
        for perm in perms:
            if perm == perm[::-1]:
                palindromes_set.add(perm)
    return palindromes_set