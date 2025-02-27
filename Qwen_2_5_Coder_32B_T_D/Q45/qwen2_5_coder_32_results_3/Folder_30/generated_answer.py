from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:5])).lower()
    counts = Counter(letters)
    half = []
    mid = ''
    for l, c in counts.items():
        half.extend([l] * (c // 2))
        if c % 2 and (not mid):
            mid = l
    perms = set((''.join(p) for p in permutations(half)))
    return {h + mid + h[::-1] for h in perms if len(h + mid + h[::-1]) >= 4}