from itertools import permutations

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    slice = s[3:5]
    valid_chars = [char for char in slice.lower() if char in english_letters]
    if len(valid_chars) < 3:
        return set()
    all_perms = set([''.join(p) for p in permutations(valid_chars, len(valid_chars))])
    palindromes = {perm for perm in all_perms if perm == perm[::-1]}
    return palindromes