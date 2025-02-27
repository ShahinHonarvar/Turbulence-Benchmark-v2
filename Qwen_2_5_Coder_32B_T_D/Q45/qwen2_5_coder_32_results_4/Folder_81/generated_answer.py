from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:7])).lower()
    cnt = Counter(letters)
    mid, half = ('', [])
    for l, c in cnt.items():
        if c % 2:
            mid = l
        half.extend(l * (c // 2))
    halves = set((''.join(p) for p in permutations(half, len(half))))
    return {h + mid + h[::-1] for h in halves if len(h + mid + h[::-1]) >= 3}