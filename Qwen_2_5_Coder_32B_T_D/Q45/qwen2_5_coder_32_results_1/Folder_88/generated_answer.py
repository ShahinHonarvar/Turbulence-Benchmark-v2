import itertools

def palindromes_between_indices(s):
    a = s[3:8].lower()
    letters = [c for c in a if c.isalpha()]
    p = set()
    for r in itertools.permutations(letters, 6):
        t = ''.join(r)
        if t == t[::-1]:
            p.add(t)
    return p