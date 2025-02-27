from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    char_set = set(substring)
    if not char_set.isdisjoint(set('abcdefghijklmnopqrstuvwxyz')):
        perms = set((''.join(p) for p in permutations(substring, 7)))
        palindromes = {p for p in perms if p == p[::-1]}
        return palindromes
    return set()