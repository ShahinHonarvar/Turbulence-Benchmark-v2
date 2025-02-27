from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:9] if c.isalpha()]
    counts = Counter(letters)
    possible_chars = ''.join((c * (counts[c] // 2) for c in counts if counts[c] // 2 > 0))
    mid_chars = [c for c in counts if counts[c] % 2 == 1]
    res = set()
    for perm in permutations(possible_chars):
        first_half = ''.join(perm)
        for mid in [''] + mid_chars:
            res.add(first_half + mid + first_half[::-1])
    return {p for p in res if len(p) >= 4}