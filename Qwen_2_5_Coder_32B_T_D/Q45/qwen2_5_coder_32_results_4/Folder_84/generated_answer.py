from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c.lower() for c in s[4:10] if c.isalpha()])
    l = len(letters)
    if l < 3:
        return set()
    count = Counter(letters)
    if any((v % 2 == 1 for v in count.values())) and sum((v % 2 == 1 for v in count.values())) > 1:
        return set()
    half = []
    mid = ''
    for char, freq in count.items():
        if freq % 2 == 1:
            mid = char
        half.extend(char * (freq // 2))
    res = set()
    for p in permutations(half):
        pal = ''.join(p) + mid + ''.join(reversed(p))
        res.add(pal)
    return res