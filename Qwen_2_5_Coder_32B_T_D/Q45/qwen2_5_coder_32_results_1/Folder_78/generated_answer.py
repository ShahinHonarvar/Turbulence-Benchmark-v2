from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    t = s[6:9].lower()
    letters = [c for c in t if c in ascii_lowercase]
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if p == p[::-1] and len(p) >= 3:
            palindromes.add(p)
    return palindromes