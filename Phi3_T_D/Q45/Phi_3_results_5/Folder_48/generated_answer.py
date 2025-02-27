from itertools import permutations

def palindromes_between_indices(s):
    sub = s[5:9]
    sub_lower = sub.lower()
    chars = set(sub_lower)
    if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in chars)):
        perms = set([''.join(p) for p in permutations(sub) if len(p) == len(chars) and ''.join(p).lower() == ''.join(reversed(p))])
        palindromes = {p for p in perms if len(p) >= 4}
        return palindromes
    else:
        return set()