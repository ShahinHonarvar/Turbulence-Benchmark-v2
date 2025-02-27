from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = ''.join(filter(str.isalpha, s))
    seen = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 5:
            seen.add(p)
    return seen