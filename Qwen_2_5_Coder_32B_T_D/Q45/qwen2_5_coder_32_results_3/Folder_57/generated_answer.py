from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    c = Counter(s)
    chars = ''.join([c * (v // 2) for c, v in c.items()])
    palindromes = set()
    for p in permutations(chars):
        half = ''.join(p)
        full = half + (max(c, key=c.get) if any((v % 2 for v in c.values())) else '') + half[::-1]
        if len(full) >= 5:
            palindromes.add(full)
    return palindromes