from collections import Counter
    from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[1:8])).lower()
    if len(letters) < 6:
        return set()
    count = Counter(letters)
    mid, halves = ('', '')
    for char, cnt in count.items():
        mid += char * (cnt % 2)
        halves += char * (cnt // 2)
    if len(mid) > 1:
        return set()
    result = set()
    for half in set(permutations(halves, len(halves))):
        half = ''.join(half)
        result.add(half + mid + half[::-1])
    return result