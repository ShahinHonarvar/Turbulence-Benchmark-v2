from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[4:8] if c.lower() in string.ascii_lowercase])
    p = set()
    for l in range(5, len(letters) + 1):
        for k in permutations(letters, l):
            k = ''.join(k)
            if k == k[::-1]:
                p.add(k)
    return p