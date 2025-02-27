from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:3] if c.isalpha()])
    count = Counter(letters)
    mid, half = ('', [])
    for char, cnt in count.items():
        half += [char] * (cnt // 2)
        if cnt % 2:
            mid = char
    if len(letters) < 3:
        return set()
    half_perms = set([''.join(p) for p in permutations(half)])
    return {h + mid + h[::-1] for h in half_perms if len(h + mid + h[::-1]) >= 3}