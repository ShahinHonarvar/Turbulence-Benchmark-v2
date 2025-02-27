from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[1:5] if c.isalpha()])
    count = Counter(letters)
    half = []
    middle = set()
    for c, v in count.items():
        half.append(c * (v // 2))
        if v % 2 == 1:
            middle.add(c)
    half = ''.join(half)
    perms = set([''.join(p) for p in permutations(half)])
    palindromes = {h + m + h[::-1] for h in perms for m in middle} | {h + h[::-1] for h in perms if not middle}
    return {p for p in palindromes if len(p) >= 3}