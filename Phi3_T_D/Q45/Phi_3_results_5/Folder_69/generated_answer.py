from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[:4].lower()
    c = Counter(s)
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(4, 0, -1):
        for p in permutations(s, i):
            p = ''.join(p)
            if p.lower() == p[::-1].lower():
                palindromes.add(p)
    return palindromes