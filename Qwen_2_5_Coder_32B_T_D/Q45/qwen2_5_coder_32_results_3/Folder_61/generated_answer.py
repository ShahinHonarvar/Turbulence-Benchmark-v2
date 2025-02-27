from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    count = Counter(letters)
    single = [k for k, v in count.items() if v % 2 != 0]
    if len(single) > 1:
        return set()
    half = ''.join((k * (v // 2) for k, v in count.items()))
    result = set()
    for p in permutations(half):
        first_half = ''.join(p)
        mid = single[0] if single else ''
        result.add(first_half + mid + first_half[::-1])
    return result