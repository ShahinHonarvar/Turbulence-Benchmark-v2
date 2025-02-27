from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    unique_chars = ''.join(set(substring))
    perms = set([''.join(p) for i in range(4, 7) for p in permutations(unique_chars, i)])
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 4}
    return palindromes