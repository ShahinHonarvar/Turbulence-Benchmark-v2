from collections import Counter
    from itertools import permutations
    import string

def palindromes_between_indices(s):
    letters = Counter([c.lower() for c in s[1:9] if c.lower() in string.ascii_lowercase])
    candidates = ''.join(letters.elements())
    palindromes = set()
    for p in permutations(candidates):
        p = ''.join(p)
        if len(p) >= 7 and p == p[::-1]:
            palindromes.add(p)
    return palindromes