from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    res = set()
    for p in permutations(letters, 6):
        p_str = ''.join(p)
        if p_str == p_str[::-1]:
            res.add(p_str)
    return res