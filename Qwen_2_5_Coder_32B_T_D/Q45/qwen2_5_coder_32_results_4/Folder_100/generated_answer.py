from itertools import permutations
    from collections import Counter
    import string

def palindromes_between_indices(s):
    letters = Counter(s[:6].lower()) & Counter(string.ascii_lowercase)
    perms = set((''.join(p) for p in permutations(letters.elements())))
    return {p for p in perms if p == p[::-1] and len(p) >= 6}